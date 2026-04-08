"use strict"
const fs = require("fs")
const path = require("path")
const assert = require("assert")
const { runScript: importExtension } = require("./extension_cli_vm.js")

// ---------- Load extension ----------

const code = fs.readFileSync(path.resolve(__dirname, "../extensions/classes.js"), "utf-8")
const ext = importExtension(code, path.resolve(__dirname, "../extensions/classes.js"))

if (!ext) {
    console.error("Failed to load extension - nothing was registered")
    process.exit(1)
}

const {
    VariableManager, ThreadUtil, ScopeStackManager, ScopeStack,
    CONFIG, Cast, CustomType, BaseCallableType, FunctionType, MethodType,
    GetterMethodType, SetterMethodType, OperatorMethodType,
    ClassType, ClassInstanceType, NothingType, Nothing,
} = ext.environment

// ---------- Test runner ----------

let passed = 0
let failed = 0
let suiteDepth = 0

function describe(name, fn) {
    const indent = "  ".repeat(suiteDepth)
    console.log(`\n${indent}${name}`)
    suiteDepth++
    try {
        fn()
    } finally {
        suiteDepth--
    } 
}

function test(name, fn) {
    const indent = "  ".repeat(suiteDepth)
    try {
        fn()
        console.log(`${indent}✓ ${name}`)
        passed++
    } catch (error) {
        console.error(`${indent}✗ ${name}`)
        console.error(`${indent}  ${error.message}`)
        failed++
    }
}

function assertThrows(fn, messageContains = null) {
    let threw = false
    try { fn() } catch (error) {
        threw = true
        if (messageContains && !error.message.toLowerCase().includes(messageContains.toLowerCase())) {
            throw new Error(`Expected error containing "${messageContains}" but got: "${error.message}"`)
        }
    }
    if (!threw) throw new Error("Expected function to throw, but it did not")
}

function assertDoesNotThrow(fn) {
    try { fn() } catch (error) {
        throw new Error(`Expected no throw, but got: ${error.message}`)
    }
}

function runGenerator(gen) {
    let result = gen.next()
    while (!result.done) result = gen.next()
    return result.value
}

function assertGeneratorThrows(gen, messageContains = null) {
    assertThrows(() => runGenerator(gen), messageContains)
}

// Unique variable names to avoid cross-test pollution in the shared global VariableManager
let __varCounter = 0
function v(base = "v") { return `${base}_${++__varCounter}` }

describe("VariableManager", () => {
    describe("constructor", () => {
        test("starts empty", () => {
            const vm = new VariableManager()
            assert.deepEqual(vm.getNames(), [])
            assert.equal(vm.has("x"), false)
        })

        test("initializes from object", () => {
            const vm = new VariableManager({ a: 1, b: "hello" })
            assert.equal(vm.get("a"), 1)
            assert.equal(vm.get("b"), "hello")
        })
    })

    describe("reset", () => {
        test("clears all variables", () => {
            const vm = new VariableManager()
            vm.set("a", 1); vm.set("b", 2)
            vm.reset()
            assert.deepEqual(vm.getNames(), [])
            assert.equal(vm.has("a"), false)
        })
    })

    describe("set", () => {
        test("creates a new variable", () => {
            const vm = new VariableManager()
            vm.set("x", 42)
            assert.equal(vm.has("x"), true)
            assert.equal(vm.get("x"), 42)
        })

        test("overwrites existing value in-place", () => {
            const vm = new VariableManager()
            vm.set("x", 1)
            const holderBefore = vm.getHolder("x")
            vm.set("x", 2)
            assert.strictEqual(vm.getHolder("x"), holderBefore)
            assert.equal(vm.get("x"), 2)
        })
    })

    describe("setHolder", () => {
        describe("shared holder behavior", () => {
            test("shares the same ValueHolder between two managers", () => {
                const vm1 = new VariableManager()
                vm1.set("x", 10)
                const holder = vm1.getHolder("x")
                const vm2 = new VariableManager()
                vm2.setHolder("x", holder)
                vm1.set("x", 99)
                assert.equal(vm2.get("x"), 99)
            })

            test("marks the variable deleted in all managers when shared holder is deleted", () => {
                const vm1 = new VariableManager()
                vm1.set("x", 1)
                const vm2 = new VariableManager()
                vm2.setHolder("x", vm1.getHolder("x"))
                vm1.delete("x")
                assert.equal(vm1.has("x"), false)
                assert.equal(vm2.has("x"), false)
            })
        })

        describe("validation", () => {
            test("throws if variable already exists in same manager", () => {
                const vm = new VariableManager()
                vm.set("x", 1)
                assertThrows(() => vm.setHolder("x", vm.getHolder("x")), "already exists")
            })
        })
    })

    describe("delete", () => {
        test("makes has return false afterwards", () => {
            const vm = new VariableManager()
            vm.set("x", 1)
            vm.delete("x")
            assert.equal(vm.has("x"), false)
        })

        test("is a no-op for non-existent variables", () => {
            const vm = new VariableManager()
            assertDoesNotThrow(() => vm.delete("nope"))
        })
    })

    describe("has", () => {
        test("returns true for existing non-deleted variable", () => {
            const vm = new VariableManager()
            vm.set("x", 1)
            assert.equal(vm.has("x"), true)
        })

        test("returns false for missing variable", () => {
            const vm = new VariableManager()
            assert.equal(vm.has("missing"), false)
        })
    })

    describe("get", () => {
        test("throws for undefined variable", () => {
            const vm = new VariableManager()
            assertThrows(() => vm.get("missing"), "'missing' is not defined")
        })
    })

    describe("safeGet", () => {
        test("returns [true, value] for existing variable", () => {
            const vm = new VariableManager()
            vm.set("x", 99)
            const [found, val] = vm.safeGet("x")
            assert.equal(found, true)
            assert.equal(val, 99)
        })

        test("returns [false, undefined] for missing variable", () => {
            const vm = new VariableManager()
            const [found, val] = vm.safeGet("missing")
            assert.equal(found, false)
            assert.equal(val, undefined)
        })
    })

    describe("getHolder", () => {
        test("returns the holder object for an existing variable", () => {
            const vm = new VariableManager()
            vm.set("x", 123)
            const holder = vm.getHolder("x")
            assert.equal(holder.value, 123)
            assert.equal(holder.isDeleted, false)
        })

        test("throws for missing variable", () => {
            const vm = new VariableManager()
            assertThrows(() => vm.getHolder("missing"), "'missing' is not defined")
        })
    })

    describe("getNames", () => {
        test("lists all live variable names", () => {
            const vm = new VariableManager()
            vm.set("a", 1); vm.set("b", 2); vm.set("c", 3)
            assert.deepEqual(vm.getNames().sort(), ["a", "b", "c"])
        })

        test("excludes deleted variables", () => {
            const vm = new VariableManager()
            vm.set("a", 1); vm.set("b", 2)
            vm.delete("a")
            assert.deepEqual(vm.getNames(), ["b"])
        })
    })
})

describe("ThreadUtil", () => {
    describe("getStackManager", () => {
        test("creates a ScopeStackManager on first call", () => {
            const thread = {}
            assert.ok(ThreadUtil.getStackManager(thread) instanceof ScopeStackManager)
        })

        test("returns the same instance on repeated calls", () => {
            const thread = {}
            assert.strictEqual(ThreadUtil.getStackManager(thread), ThreadUtil.getStackManager(thread))
        })
    })

    describe("getCurrentStack", () => {
        test("returns a ScopeStack", () => {
            const thread = {}
            assert.ok(ThreadUtil.getCurrentStack(thread) instanceof ScopeStack)
        })
    })

    describe("pushStack", () => {
        test("increases manager size", () => {
            const thread = {}
            const manager = ThreadUtil.getStackManager(thread)
            ThreadUtil.pushStack(thread, new ScopeStack())
            assert.equal(manager.getSize(), 2)
            manager.popStackFromManager()
        })
    })

    describe("popStack", () => {
        test("pops and returns the top stack", () => {
            const thread = {}
            const pushed = new ScopeStack()
            ThreadUtil.pushStack(thread, pushed)
            assert.strictEqual(ThreadUtil.popStack(thread), pushed)
            assert.equal(ThreadUtil.getStackManager(thread).getSize(), 1)
        })
    })
})

describe("ScopeStackManager", () => {
    describe("constructor", () => {
        test("starts with exactly one stack", () => {
            const m = new ScopeStackManager()
            assert.equal(m.getSize(), 1)
        })
    })

    describe("getCurrentStackFromManager", () => {
        test("returns the current top stack instance", () => {
            const m = new ScopeStackManager()
            const initial = m.getCurrentStackFromManager()

            assert.ok(initial instanceof ScopeStack)

            const pushed = new ScopeStack()
            m.pushStackToManager(pushed)
            assert.strictEqual(m.getCurrentStackFromManager(), pushed)
            assert.notStrictEqual(m.getCurrentStackFromManager(), initial)

            m.popStackFromManager()
            assert.strictEqual(m.getCurrentStackFromManager(), initial)
        })
    })

    describe("pushStackToManager", () => {
        test("increases size by one", () => {
            const m = new ScopeStackManager()
            m.pushStackToManager(new ScopeStack())
            assert.equal(m.getSize(), 2)
        })
    })

    describe("popStackFromManager", () => {
        test("returns the most recently pushed stack", () => {
            const m = new ScopeStackManager()
            const s = new ScopeStack()
            m.pushStackToManager(s)
            assert.strictEqual(m.popStackFromManager(), s)
            assert.equal(m.getSize(), 1)
        })

        test("throws when only one stack remains", () => {
            const m = new ScopeStackManager()
            assertThrows(() => m.popStackFromManager(), "Internal error")
        })
    })

    describe("insertScopeAndPushStack", () => {
        test("pushes a copied stack with the inserted scope", () => {
            const m = new ScopeStackManager()
            const callableStack = new ScopeStack()
            callableStack.enterUserScope()
            const outerName = v("outer")
            callableStack.setScopeVar(outerName, "visible")
            const callable = { stack: callableStack }
            const scope = {
                type: ScopeStack.FUNCTION,
                isCallable: true,
                supportsVars: true,
                vars: new VariableManager({ inner: 1 }),
            }

            const beforeSize = m.getSize()
            const beforeCurrent = m.getCurrentStackFromManager()
            m.insertScopeAndPushStack(callable, scope)

            assert.equal(m.getSize(), beforeSize + 1)
            const pushed = m.getCurrentStackFromManager()
            assert.notStrictEqual(pushed, callableStack)
            assert.equal(pushed.getScopeVar("inner"), 1)
            assert.equal(pushed.getScopeVar(outerName), "visible")
            assert.equal(callableStack.getScopeVar(outerName), "visible")

            m.popStackFromManager()
            assert.strictEqual(m.getCurrentStackFromManager(), beforeCurrent)
        })
    })

    describe("enterFunctionCall", () => {
        describe("call scope creation", () => {
            test("pushes a new FUNCTION scope with args as variables", () => {
                const m = new ScopeStackManager()
                m.enterFunctionCall({ stack: new ScopeStack() }, { myArg: "hello" })
                assert.equal(m.getSize(), 2)
                const inner = m.getCurrentStackFromManager()._getInnermostScope()
                assert.equal(inner.type, ScopeStack.FUNCTION)
                assert.equal(inner.isCallable, true)
                assert.equal(inner.vars.get("myArg"), "hello")
            })

            test("preserves outer scopes of the callable via shallow copy", () => {
                const outerStack = new ScopeStack()
                outerStack.enterUserScope()
                const name = v("captured")
                outerStack.setScopeVar(name, "visible")

                const m = new ScopeStackManager()
                m.enterFunctionCall({ stack: outerStack }, {})
                assert.equal(m.getCurrentStackFromManager().getScopeVar(name), "visible")
            })
        })
    })

    describe("enterMethodCall", () => {
        test("pushes a method-call scope and exposes self plus args", () => {
            const m = new ScopeStackManager()
            const callable = { stack: new ScopeStack() }
            const self = { customId: "gceClassInstance" }

            m.enterMethodCall(callable, self, { myArg: "hello" })

            const stack = m.getCurrentStackFromManager()
            assert.equal(m.getSize(), 2)
            assert.strictEqual(stack.getSelfOrThrow(), self)
            assert.equal(stack.getScopeVar("myArg"), "hello")

            m.popStackFromManager()
        })
    })

    describe("enterGetterMethodCall", () => {
        test("pushes a getter-method scope and exposes self", () => {
            const m = new ScopeStackManager()
            const callable = { stack: new ScopeStack() }
            const self = { customId: "gceClassInstance" }

            m.enterGetterMethodCall(callable, self)

            const stack = m.getCurrentStackFromManager()
            assert.equal(m.getSize(), 2)
            assert.strictEqual(stack.getSelfOrThrow(), self)

            m.popStackFromManager()
        })
    })

    describe("enterSetterMethodCall", () => {
        test("pushes a setter-method scope and exposes self plus setter value", () => {
            const m = new ScopeStackManager()
            const callable = { stack: new ScopeStack() }
            const self = { customId: "gceClassInstance" }

            m.enterSetterMethodCall(callable, self, "next")

            const stack = m.getCurrentStackFromManager()
            assert.equal(m.getSize(), 2)
            assert.strictEqual(stack.getSelfOrThrow(), self)
            assert.equal(stack.getSetterValueOrThrow(), "next")

            m.popStackFromManager()
        })
    })

    describe("enterOperatorMethodCall", () => {
        test("pushes an operator-method scope and exposes self plus other value", () => {
            const m = new ScopeStackManager()
            const callable = { stack: new ScopeStack() }
            const self = { customId: "gceClassInstance" }

            m.enterOperatorMethodCall(callable, self, 42)

            const stack = m.getCurrentStackFromManager()
            assert.equal(m.getSize(), 2)
            assert.strictEqual(stack.getSelfOrThrow(), self)
            assert.equal(stack.getOtherValueOrThrow(), 42)

            m.popStackFromManager()
        })
    })

    describe("prepareReturn", () => {
        test("pops the callable stack", () => {
            const m = new ScopeStackManager()
            m.enterFunctionCall({ stack: new ScopeStack() }, {})
            assert.equal(m.getSize(), 2)
            m.prepareReturn()
            assert.equal(m.getSize(), 1)
        })

        test("throws when not inside a callable scope", () => {
            const m = new ScopeStackManager()
            assertThrows(() => m.prepareReturn(), "return can only be used")
        })
    })

    describe("getSize", () => {
        test("returns current number of stacks", () => {
            const m = new ScopeStackManager()
            assert.equal(m.getSize(), 1)
            m.pushStackToManager(new ScopeStack())
            assert.equal(m.getSize(), 2)
        })
    })

    describe("trimSize", () => {
        test("reduces stack count to given size", () => {
            const m = new ScopeStackManager()
            m.pushStackToManager(new ScopeStack())
            m.pushStackToManager(new ScopeStack())
            assert.equal(m.getSize(), 3)
            m.trimSize(1)
            assert.equal(m.getSize(), 1)
        })

        test("is a no-op when already at or below target size", () => {
            const m = new ScopeStackManager()
            m.trimSize(10)
            assert.equal(m.getSize(), 1)
        })

        test("collapses to empty for zero", () => {
            const m = new ScopeStackManager()
            m.trimSize(0)
            assert.equal(m.getSize(), 0)
        })
    })
})

describe("ScopeStack", () => {
    describe("constructor", () => {
        test("creates one GLOBALS scope as the innermost scope", () => {
            const s = new ScopeStack()
            assert.equal(s.getSize(), 1)
            const scope = s._getInnermostScope()
            assert.equal(scope.type, ScopeStack.GLOBALS)
            assert.equal(scope.isGlobalScope, true)
        })
    })

    describe("shallowCopy", () => {
        test("creates an independent scopes array", () => {
            const s = new ScopeStack()
            const copy = s.shallowCopy()
            copy.enterUserScope()
            assert.equal(s.getSize(), 1)
            assert.equal(copy.getSize(), 2)
        })

        test("shares the same underlying scope objects", () => {
            const s = new ScopeStack()
            const copy = s.shallowCopy()
            assert.strictEqual(
                s.scopes[s.scopes.length - 1],
                copy.scopes[copy.scopes.length - 1]
            )
        })
    })

    describe("enterClassDefScope", () => {
        test("adds a CLASS_DEF scope with the given class", () => {
            const s = new ScopeStack()
            const cls = { name: "Foo", variables: {} }
            s.enterClassDefScope(cls)
            const inner = s._getInnermostScope()
            assert.equal(inner.type, ScopeStack.CLASS_DEF)
            assert.strictEqual(inner.cls, cls)
            s.exitClassDefScope()
        })
    })

    describe("enterUserScope", () => {
        test("adds a USER_SCOPE at the front", () => {
            const s = new ScopeStack()
            s.enterUserScope()
            assert.equal(s.getSize(), 2)
            const inner = s._getInnermostScope()
            assert.equal(inner.type, ScopeStack.USER_SCOPE)
            assert.equal(inner.isUserScope, true)
            assert.ok(inner.vars instanceof VariableManager)
            s.exitUserScope()
        })
    })

    describe("_getQualifiedScope", () => {
        test("returns the first scope matching the predicate", () => {
            const s = new ScopeStack()
            s.enterUserScope()
            const found = s._getQualifiedScope(scope => scope.isUserScope)
            assert.ok(found !== null)
            assert.equal(found.type, ScopeStack.USER_SCOPE)
            s.exitUserScope()
        })

        test("returns null when no scope matches", () => {
            const s = new ScopeStack()
            const found = s._getQualifiedScope(scope => scope.isUserScope)
            assert.strictEqual(found, null)
        })
    })

    describe("_getInnermostScope", () => {
        test("returns the scope at index 0", () => {
            const s = new ScopeStack()
            s.enterUserScope()
            const inner = s._getInnermostScope()
            assert.equal(inner.type, ScopeStack.USER_SCOPE)
            s.exitUserScope()
        })

        test("returns GLOBALS when no other scope is pushed", () => {
            const s = new ScopeStack()
            assert.equal(s._getInnermostScope().type, ScopeStack.GLOBALS)
        })
    })

    describe("getSelfOrThrow", () => {
        test("returns self when a supportsSelf scope is active", () => {
            const m = new ScopeStackManager()
            const self = { customId: "gceClassInstance" }
            m.enterMethodCall({ stack: new ScopeStack() }, self, {})
            const s = m.getCurrentStackFromManager()
            assert.strictEqual(s.getSelfOrThrow(), self)
            m.popStackFromManager()
        })

        test("throws when no method scope is active", () => {
            const s = new ScopeStack()
            assertThrows(() => s.getSelfOrThrow(), "self can only be used")
        })
    })

    describe("getSetterValueOrThrow", () => {
        test("returns the setter value when in a setter scope", () => {
            const m = new ScopeStackManager()
            const self = {}
            m.enterSetterMethodCall({ stack: new ScopeStack() }, self, "newVal")
            const s = m.getCurrentStackFromManager()
            assert.equal(s.getSetterValueOrThrow(), "newVal")
            m.popStackFromManager()
        })

        test("throws when not in a setter scope", () => {
            const s = new ScopeStack()
            assertThrows(() => s.getSetterValueOrThrow(), "setter value can only be used")
        })
    })

    describe("getOtherValueOrThrow", () => {
        test("returns the other operand when in an operator method scope", () => {
            const m = new ScopeStackManager()
            const self = {}
            m.enterOperatorMethodCall({ stack: new ScopeStack() }, self, 42)
            const s = m.getCurrentStackFromManager()
            assert.equal(s.getOtherValueOrThrow(), 42)
            m.popStackFromManager()
        })

        test("throws when not in an operator method scope", () => {
            const s = new ScopeStack()
            assertThrows(() => s.getOtherValueOrThrow(), "other value can only be used")
        })
    })

    describe("getClsOrThrow", () => {
        test("returns the class when inside a class def scope", () => {
            const s = new ScopeStack()
            const cls = { name: "Bar" }
            s.enterClassDefScope(cls)
            assert.strictEqual(s.getClsOrThrow("test block"), cls)
            s.exitClassDefScope()
        })

        test("throws when not in a class def scope", () => {
            const s = new ScopeStack()
            s.enterClassDefScope({ name: "Bar"})
            s.enterUserScope()
            assertThrows(() => s.getClsOrThrow("test block"), "class definition")
            s.exitUserScope()
            s.exitClassDefScope()
        })
    })

    describe("assertCanReturn", () => {
        test("does not throw inside a callable scope", () => {
            const m = new ScopeStackManager()
            m.enterFunctionCall({ stack: new ScopeStack() }, {})
            const s = m.getCurrentStackFromManager()
            assertDoesNotThrow(() => s.assertCanReturn())
            m.popStackFromManager()
        })

        test("throws when no callable scope is active", () => {
            const s = new ScopeStack()
            assertThrows(() => s.assertCanReturn(), "return can only be used")
        })
    })

    describe("exitClassDefScope", () => {
        test("removes the class def scope", () => {
            const s = new ScopeStack()
            s.enterClassDefScope({ name: "X", variables: {} })
            s.exitClassDefScope()
            assert.equal(s.getSize(), 1)
            assert.equal(s._getInnermostScope().type, ScopeStack.GLOBALS)
        })

        test("throws when innermost is not a class def scope", () => {
            const s = new ScopeStack()
            assertThrows(() => s.exitClassDefScope(), "Internal error")
        })
    })

    describe("exitUserScope", () => {
        test("removes the innermost user scope", () => {
            const s = new ScopeStack()
            s.enterUserScope()
            s.exitUserScope()
            assert.equal(s.getSize(), 1)
            assert.equal(s._getInnermostScope().type, ScopeStack.GLOBALS)
        })

        test("throws when innermost is not a user scope", () => {
            const s = new ScopeStack()
            assertThrows(() => s.exitUserScope(), "Internal error")
        })
    })

    describe("getSize", () => {
        test("returns current number of scopes", () => {
            const s = new ScopeStack()
            assert.equal(s.getSize(), 1)
            s.enterUserScope()
            assert.equal(s.getSize(), 2)
            s.exitUserScope()
        })
    })

    describe("trimSize", () => {
        test("reduces scope count to given size", () => {
            const s = new ScopeStack()
            s.enterUserScope()
            s.enterUserScope()
            assert.equal(s.getSize(), 3)
            s.trimSize(1)
            assert.equal(s.getSize(), 1)
        })
    })

    describe("setNextFuncConfig", () => {
        describe("config handling", () => {
            test("stores the provided function config", () => {
                const s = new ScopeStack()
                s.setNextFuncConfig({ argNames: ["a", "b"], argDefaults: [1] })

                assert.deepEqual(s.nextFuncConfig.argNames, ["a", "b"])
                assert.deepEqual(s.nextFuncConfig.argDefaults, [1])
            })

            test("falls back to the default config when omitted", () => {
                const s = new ScopeStack()
                s.setNextFuncConfig({ argNames: ["a"], argDefaults: [] })

                s.setNextFuncConfig()

                assert.deepEqual(s.nextFuncConfig.argNames, [])
                assert.deepEqual(s.nextFuncConfig.argDefaults, [])
            })

            test("throws when there are more default values than argument names", () => {
                const s = new ScopeStack()
                assertThrows(
                    () => s.setNextFuncConfig({ argNames: ["a"], argDefaults: [1, 2] }),
                    "as many default values as argument names"
                )
            })
        })
    })

    describe("getAndResetNextFuncConfig", () => {
        test("round-trips and resets to defaults", () => {
            const s = new ScopeStack()
            s.setNextFuncConfig({ argNames: ["a", "b"], argDefaults: [1] })
            const config = s.getAndResetNextFuncConfig()
            assert.deepEqual(config.argNames, ["a", "b"])
            assert.deepEqual(config.argDefaults, [1])
            const reset = s.getAndResetNextFuncConfig()
            assert.deepEqual(reset.argNames, [])
            assert.deepEqual(reset.argDefaults, [])
        })
    })

    describe("getDefaultFuncConfig", () => {
        test("always returns empty argNames and argDefaults", () => {
            const s = new ScopeStack()
            const config = s.getDefaultFuncConfig()
            assert.deepEqual(config.argNames, [])
            assert.deepEqual(config.argDefaults, [])
        })
    })

    describe("setScopeVar", () => {
        describe("storage behavior", () => {
            test("stores and retrieves in the global scope", () => {
                const s = new ScopeStack()
                const name = v("global")
                s.setScopeVar(name, 42)
                assert.equal(s.getScopeVar(name), 42)
            })

            test("writes directly to cls.variables inside a class def scope", () => {
                const s = new ScopeStack()
                const cls = { name: "X", variables: {} }
                s.enterClassDefScope(cls)
                s.setScopeVar("myProp", "value")
                assert.equal(cls.variables["myProp"], "value")
                s.exitClassDefScope()
            })
        })
    })

    describe("_getScopeOfVar", () => {
        test("returns the innermost matching variable scope", () => {
            const s = new ScopeStack()
            const name = v("scope_lookup")
            s.setScopeVar(name, "global")
            s.enterUserScope()
            s.setScopeVar(name, "local")

            const foundScope = s._getScopeOfVar(name)

            assert.strictEqual(foundScope, s._getInnermostScope())
            assert.strictEqual(foundScope.vars.get(name), "local")
            s.exitUserScope()
        })

        test("respects startIndex by skipping the innermost matching scope", () => {
            const s = new ScopeStack()
            const name = v("shadowed")
            s.enterUserScope()
            s.setScopeVar(name, "outer")
            const outerScope = s._getInnermostScope()
            s.enterUserScope()
            s.setScopeVar(name, "inner")

            const foundScope = s._getScopeOfVar(name, 1)

            assert.strictEqual(foundScope, outerScope)
            assert.strictEqual(foundScope.vars.get(name), "outer")
            s.exitUserScope()
            s.exitUserScope()
        })

        test("respects excludeLastIndecies by excluding the global scope", () => {
            const s = new ScopeStack()
            const name = v("global_only")
            s.setScopeVar(name, "global")
            s.enterUserScope()

            assertThrows(() => s._getScopeOfVar(name, 0, 1), "is not defined")
            assert.strictEqual(s._getScopeOfVar(name, 0, 1, false), null)

            s.exitUserScope()
        })

        test("supports throwOnNotFound=false without throwing for missing variables", () => {
            const s = new ScopeStack()

            assertDoesNotThrow(() => {
                const foundScope = s._getScopeOfVar("__missing_explicit__", 0, 0, false)
                assert.strictEqual(foundScope, null)
            })

            assertThrows(() => s._getScopeOfVar("__missing_explicit__", 0, 0, true), "is not defined")
        })
    })

    describe("getScopeVar", () => {
        describe("scope resolution", () => {
            test("prefers the user scope over a shadowed global variable", () => {
                const s = new ScopeStack()
                const name = v("shadow")
                s.setScopeVar(name, "global")
                s.enterUserScope()
                s.setScopeVar(name, "local")
                assert.equal(s.getScopeVar(name), "local")
                s.exitUserScope()
                assert.equal(s.getScopeVar(name), "global")
            })
        })

        describe("validation", () => {
            test("throws for an unknown variable", () => {
                const s = new ScopeStack()
                assertThrows(() => s.getScopeVar("__definitely_not_set__"), "is not defined")
            })
        })
    })

    describe("safeGetScopeVar", () => {
        test("returns [true, value] for existing variable", () => {
            const s = new ScopeStack()
            const name = v("safe")
            s.setScopeVar(name, 77)
            const [found, value] = s.safeGetScopeVar(name)
            assert.equal(found, true)
            assert.equal(value, 77)
        })

        test("returns [false, undefined] for a missing variable", () => {
            const s = new ScopeStack()
            const [found, value] = s.safeGetScopeVar("__missing_safe_scope_var__")
            assert.equal(found, false)
            assert.equal(value, undefined)
        })
    })

    describe("deleteScopeVar", () => {
        test("removes the variable from its scope", () => {
            const s = new ScopeStack()
            const name = v("del")
            s.setScopeVar(name, 1)
            s.deleteScopeVar(name)
            assert.equal(s.hasScopeVar(name), false)
        })
    })

    describe("bindScopeVarGlobal", () => {
        describe("holder binding", () => {
            test("reflects mutations from local scope back into global scope", () => {
                const s = new ScopeStack()
                const name = v("bind_g")
                s.setScopeVar(name, 10)
                s.enterUserScope()
                s.bindScopeVarGlobal(name)
                s.setScopeVar(name, 99)
                s.exitUserScope()
                assert.equal(s.getScopeVar(name), 99)
            })
        })

        describe("validation", () => {
            test("throws for a variable not present in global scope", () => {
                const s = new ScopeStack()
                s.enterUserScope()
                assertThrows(() => s.bindScopeVarGlobal("__no_such_global__"), "No global variable")
                s.exitUserScope()
            })
        })
    })

    describe("bindScopeVarNonlocal", () => {
        describe("holder binding", () => {
            test("reflects mutations from inner scope into enclosing scope", () => {
                const s = new ScopeStack()
                s.enterUserScope()
                const name = v("bind_nl")
                s.setScopeVar(name, 5)
                s.enterUserScope()
                s.bindScopeVarNonlocal(name)
                s.setScopeVar(name, 55)
                s.exitUserScope()
                assert.equal(s.getScopeVar(name), 55)
                s.exitUserScope()
            })
        })

        describe("validation", () => {
            test("throws for a variable not found in any outer non-global scope", () => {
                const s = new ScopeStack()
                s.enterUserScope()
                s.enterUserScope()
                assertThrows(() => s.bindScopeVarNonlocal("__no_such_outer__"), "No non-local variable")
                s.exitUserScope()
                s.exitUserScope()
            })
        })
    })

    describe("hasScopeVar", () => {
        describe("scope filters", () => {
            test("returns true when var exists in any scope", () => {
                const s = new ScopeStack()
                const name = v("any")
                s.setScopeVar(name, 1)
                s.enterUserScope()
                assert.equal(s.hasScopeVar(name), true)
                s.exitUserScope()
            })

            test("onlyCurrentScope=true ignores outer scopes", () => {
                const s = new ScopeStack()
                const name = v("curonly")
                s.setScopeVar(name, 1)
                s.enterUserScope()
                assert.equal(s.hasScopeVar(name, true, false), false)
                assert.equal(s.hasScopeVar(name, false, false), true)
                s.exitUserScope()
            })

            test("onlyGlobalScope=true only checks global scope", () => {
                const s = new ScopeStack()
                const name = v("globonly")
                s.enterUserScope()
                s.setScopeVar(name, 1)
                assert.equal(s.hasScopeVar(name, false, true), false)
                s.exitUserScope()
                s.setScopeVar(name, 1)
                s.enterUserScope()
                assert.equal(s.hasScopeVar(name, false, true), true)
                s.exitUserScope()
            })
        })

        describe("validation", () => {
            test("throws when both onlyCurrentScope and onlyGlobalScope are true", () => {
                const s = new ScopeStack()
                assertThrows(() => s.hasScopeVar("x", true, true), "Internal error")
            })
        })
    })

    describe("getScopeVarNames", () => {
        describe("aggregation", () => {
            test("includes variables from all active scopes", () => {
                const s = new ScopeStack()
                const g = v("gn_g"); const l = v("gn_l")
                s.setScopeVar(g, 1)
                s.enterUserScope()
                s.setScopeVar(l, 2)
                const names = s.getScopeVarNames()
                assert.ok(names.includes(g))
                assert.ok(names.includes(l))
                s.exitUserScope()
            })

            test("keeps a shadowed variable only once", () => {
                const s = new ScopeStack()
                const name = v("dup")
                s.setScopeVar(name, "global")
                s.enterUserScope()
                s.setScopeVar(name, "local")
                const names = s.getScopeVarNames()
                assert.equal(names.filter(n => n === name).length, 1)
                s.exitUserScope()
            })
        })

        describe("scope filters", () => {
            test("onlyCurrentScope=true returns only innermost scope vars", () => {
                const s = new ScopeStack()
                const g = v("gno_g"); const l = v("gno_l")
                s.setScopeVar(g, 1)
                s.enterUserScope()
                s.setScopeVar(l, 2)
                const names = s.getScopeVarNames(true, false)
                assert.ok(!names.includes(g))
                assert.ok(names.includes(l))
                s.exitUserScope()
            })

            test("onlyGlobalScope=true returns only global scope vars", () => {
                const s = new ScopeStack()
                const g = v("gog_g"); const l = v("gog_l")
                s.setScopeVar(g, 1)
                s.enterUserScope()
                s.setScopeVar(l, 2)
                const names = s.getScopeVarNames(false, true)
                assert.ok(names.includes(g))
                assert.ok(!names.includes(l))
                s.exitUserScope()
            })
        })
    })
})

describe("Cast", () => {
    describe("_safeGetNamedValue", () => {
        test("reads the innermost named value from the current thread", () => {
            const thread = {}
            const s = ThreadUtil.getCurrentStack(thread)
            const name = v("named_value")

            s.setScopeVar(name, "global")
            s.enterUserScope()
            s.setScopeVar(name, "local")

            const [found, value] = Cast._safeGetNamedValue(name, thread)

            assert.strictEqual(found, true)
            assert.strictEqual(value, "local")
            s.exitUserScope()
        })

        test("falls back to globals when no thread is provided", () => {
            const name = v("global_named_value")
            const globalStack = new ScopeStack()
            globalStack.setScopeVar(name, 42)

            const [found, value] = Cast._safeGetNamedValue(name)

            assert.strictEqual(found, true)
            assert.strictEqual(value, 42)
        })

        test("returns [false, undefined] for missing names", () => {
            const [found, value] = Cast._safeGetNamedValue("__missing_named_value__", {})
            assert.strictEqual(found, false)
            assert.strictEqual(value, undefined)
        })
    })

    describe("_toTypeFromValueOrVariable", () => {
        test("returns matching instances unchanged", () => {
            const cls = new ClassType("DirectClass", null)
            assert.strictEqual(
                Cast._toTypeFromValueOrVariable(cls, {}, ClassType, "class or class variable name"),
                cls
            )
        })

        test("resolves named values through the current thread", () => {
            const thread = {}
            const s = ThreadUtil.getCurrentStack(thread)
            const name = v("shared_resolver")
            const fn = new FunctionType(
                "sharedFn",
                function* () { return Nothing },
                new ScopeStack(),
                { argNames: [], argDefaults: [] }
            )
            s.setScopeVar(name, fn)

            assert.strictEqual(
                Cast._toTypeFromValueOrVariable(name, thread, FunctionType, "function or function variable name"),
                fn
            )
        })

        test("throws for missing variable names", () => {
            assertThrows(
                () => Cast._toTypeFromValueOrVariable("__missing_class__", {}, ClassType, "class or class variable name"),
                "is not defined"
            )
        })

        test("throws when a named variable has the wrong type", () => {
            const thread = {}
            const s = ThreadUtil.getCurrentStack(thread)
            const name = v("wrong_type")
            s.setScopeVar(name, 123)

            assertThrows(
                () => Cast._toTypeFromValueOrVariable(name, thread, ClassType, "class or class variable name"),
                "is a Number"
            )
        })
    })

    describe("toClass", () => {
        test("accepts class values and resolves named class variables", () => {
            const thread = {}
            const s = ThreadUtil.getCurrentStack(thread)
            const cls = new ClassType("DirectClass", null)
            const name = v("class_lookup")

            s.setScopeVar(name, cls)

            assert.strictEqual(Cast.toClass(cls), cls)
            assert.strictEqual(Cast.toClass(name, thread), cls)
        })
    })

    describe("toClassInstance", () => {
        test("accepts instance values and resolves named instance variables", () => {
            const thread = {}
            const s = ThreadUtil.getCurrentStack(thread)
            const instance = new ClassInstanceType(new ClassType("Thing", null))
            const name = v("instance_lookup")

            s.setScopeVar(name, instance)

            assert.strictEqual(Cast.toClassInstance(instance, {}), instance)
            assert.strictEqual(Cast.toClassInstance(name, thread), instance)
        })
    })

    describe("toFunction", () => {
        test("accepts function values and resolves named function variables", () => {
            const thread = {}
            const s = ThreadUtil.getCurrentStack(thread)
            const fn = new FunctionType(
                "directFn",
                function* () { return Nothing },
                new ScopeStack(),
                { argNames: [], argDefaults: [] }
            )
            const name = v("fn_lookup")

            s.setScopeVar(name, fn)

            assert.strictEqual(Cast.toFunction(fn), fn)
            assert.strictEqual(Cast.toFunction(name, thread), fn)
        })
    })
})

describe("CustomType", () => {
    describe("subclassing", () => {
        test("can be subclassed and participates in instanceof", () => {
            class DerivedCustomType extends CustomType {
                toString() { return "<Derived>" }
            }
            const value = new DerivedCustomType()
            assert.ok(value instanceof CustomType)
            assert.equal(value.toString(), "<Derived>")
        })
    })
})

describe("BaseCallableType", () => {
    describe("execute", () => {
        test("runs the callable and restores the stack after return", () => {
            const thread = {}
            const callable = new FunctionType(
                "runMe",
                function* (thread) {
                    const stack = ThreadUtil.getCurrentStack(thread)
                    assert.strictEqual(stack.getScopeVar("value"), 123)
                    ThreadUtil.getStackManager(thread).prepareReturn()
                    return "done"
                },
                new ScopeStack(),
                { argNames: ["value"], argDefaults: [] }
            )
            const manager = ThreadUtil.getStackManager(thread)
            const sizeBefore = manager.getSize()

            const output = runGenerator(callable.execute(thread, [123]))

            assert.strictEqual(output, "done")
            assert.strictEqual(manager.getSize(), sizeBefore)
        })

        test("trims interrupted inner scopes when the callable throws", () => {
            const thread = {}
            const callable = new FunctionType(
                "broken",
                function* (thread) {
                    const stack = ThreadUtil.getCurrentStack(thread)
                    stack.enterUserScope()
                    stack.setScopeVar("temp", 1)
                    throw new Error("boom")
                },
                new ScopeStack(),
                { argNames: [], argDefaults: [] }
            )

            assertGeneratorThrows(callable.execute(thread, []), "boom")
            assert.strictEqual(ThreadUtil.getCurrentStack(thread).getSize(), 1)
            assert.strictEqual(ThreadUtil.getCurrentStack(thread).hasScopeVar("temp"), false)
        })
    })

    describe("evaluateArgs", () => {
        test("assigns positional and default values", () => {
            const callable = new BaseCallableType(
                "f",
                function* () { return Nothing },
                new ScopeStack(),
                { argNames: ["a", "b", "c"], argDefaults: [2, 3] }
            )
            const args = callable.evaluateArgs([1])
            assert.strictEqual(args.a, 1)
            assert.strictEqual(args.b, 2)
            assert.strictEqual(args.c, 3)
        })

        test("throws when too many positional args are provided", () => {
            const callable = new BaseCallableType(
                "f",
                function* () { return Nothing },
                new ScopeStack(),
                { argNames: ["a"], argDefaults: [] }
            )
            assertThrows(() => callable.evaluateArgs([1, 2]), "at most")
        })

        test("throws when required positional args are missing", () => {
            const callable = new BaseCallableType(
                "f",
                function* () { return Nothing },
                new ScopeStack(),
                { argNames: ["a", "b"], argDefaults: [2] }
            )
            assertThrows(() => callable.evaluateArgs([]), "at least 1 positional")
        })
    })
})

describe("FunctionType", () => {
    describe("enterContext", () => {
        test("pushes function call scope with evaluated args", () => {
            const fn = new FunctionType(
                "myFn",
                function* () { return Nothing },
                new ScopeStack(),
                { argNames: ["x"], argDefaults: [] }
            )
            const thread = {}
            const manager = ThreadUtil.getStackManager(thread)
            const sizeBefore = manager.getSize()

            fn.enterContext(thread, [123])
            assert.equal(manager.getSize(), sizeBefore + 1)
            assert.equal(ThreadUtil.getCurrentStack(thread).getScopeVar("x"), 123)

            manager.popStackFromManager()
        })
    })
})

describe("MethodType", () => {
    describe("enterContext", () => {
        test("pushes method scope with self and args", () => {
            const method = new MethodType(
                "myMethod",
                function* () { return Nothing },
                new ScopeStack(),
                { argNames: ["x"], argDefaults: [] }
            )
            const thread = {}
            const manager = ThreadUtil.getStackManager(thread)
            const self = new ClassInstanceType(new ClassType("C", null))
            const sizeBefore = manager.getSize()

            method.enterContext(thread, self, [7])
            const stack = ThreadUtil.getCurrentStack(thread)
            assert.equal(manager.getSize(), sizeBefore + 1)
            assert.strictEqual(stack.getSelfOrThrow(), self)
            assert.equal(stack.getScopeVar("x"), 7)

            manager.popStackFromManager()
        })
    })
})

describe("GetterMethodType", () => {
    describe("className", () => {
        test("uses the expected className", () => {
            const method = new GetterMethodType(
                "g",
                function* () { return Nothing },
                new ScopeStack(),
                { argNames: [], argDefaults: [] }
            )
            assert.equal(method.className, "Getter Method")
        })
    })
})

describe("SetterMethodType", () => {
    describe("className", () => {
        test("uses the expected className", () => {
            const method = new SetterMethodType(
                "s",
                function* () { return Nothing },
                new ScopeStack(),
                { argNames: [], argDefaults: [] }
            )
            assert.equal(method.className, "Setter Method")
        })
    })

    describe("checkOutputValue", () => {
        test("enforces Nothing return", () => {
            const setter = new SetterMethodType(
                "setX",
                function* () { return Nothing },
                new ScopeStack(),
                { argNames: [], argDefaults: [] }
            )
            assertDoesNotThrow(() => setter.checkOutputValue(Nothing))
            assertThrows(() => setter.checkOutputValue("not-nothing"), "must return")
        })
    })
})

describe("OperatorMethodType", () => {
    describe("className", () => {
        test("uses the expected className", () => {
            const method = new OperatorMethodType(
                "o",
                function* () { return Nothing },
                new ScopeStack(),
                { argNames: [], argDefaults: [] }
            )
            assert.equal(method.className, "Operator Method")
        })
    })
})

describe("ClassType", () => {
    describe("toString", () => {
        test("includes superclass info when present", () => {
            const base = new ClassType("Base", null)
            const sub = new ClassType("Sub", base)
            assert.equal(base.toString(), "<Class 'Base'>")
            assert.equal(sub.toString(), "<Class 'Sub'(super 'Base')>")
        })
    })

    describe("isSubclassOf", () => {
        test("reflects inheritance chain", () => {
            const base = new ClassType("Base", null)
            const mid = new ClassType("Mid", base)
            const sub = new ClassType("Sub", mid)
            assert.equal(sub.isSubclassOf(base), true)
            assert.equal(base.isSubclassOf(sub), false)
        })
    })

    describe("getAllMembers", () => {
        test("merges inherited members and keeps subclass overrides", () => {
            const base = new ClassType("Base", null)
            const sub = new ClassType("Sub", base)

            base.setMember("baseOnly", "class variable", 1)
            base.setMember("shared", "class variable", "base")
            sub.setMember("shared", "class variable", "sub")
            sub.setMember("subOnly", "class variable", 2)

            const [, , , , , variables] = sub.getAllMembers()
            assert.deepStrictEqual({ ...variables }, {
                baseOnly: 1,
                shared: "sub",
                subOnly: 2,
            })
            assert.strictEqual(sub.getClassVariable("baseOnly"), 1)
        })
    })

    describe("setMember", () => {
        test("rejects incompatible redefinitions with the same name", () => {
            const cls = new ClassType("C", null)
            cls.setMember("thing", "instance method", { tag: "method" })
            assertThrows(() => cls.setMember("thing", "class variable", 99), "same name")
        })
    })

    describe("createInstance", () => {
        test("executes init and returns an instance", () => {
            const cls = new ClassType("Widget", null)
            cls.setMember(
                CONFIG.INIT_METHOD_NAME,
                "instance method",
                new MethodType(
                    CONFIG.INIT_METHOD_NAME,
                    function* (thread) {
                        const stack = ThreadUtil.getCurrentStack(thread)
                        const self = stack.getSelfOrThrow()
                        self.attributes.label = stack.getScopeVar("label")
                        ThreadUtil.getStackManager(thread).prepareReturn()
                        return Nothing
                    },
                    new ScopeStack(),
                    { argNames: ["label"], argDefaults: [] }
                )
            )

            const instance = runGenerator(cls.createInstance({}, ["hello"]))
            assert.ok(instance instanceof ClassInstanceType)
            assert.strictEqual(instance.attributes.label, "hello")
        })
    })

    describe("executeStaticMethod", () => {
        test("calls the stored static function", () => {
            const cls = new ClassType("Toolbox", null)
            cls.setMember(
                "make",
                "static method",
                new FunctionType(
                    "make",
                    function* (thread) {
                        const value = ThreadUtil.getCurrentStack(thread).getScopeVar("x")
                        ThreadUtil.getStackManager(thread).prepareReturn()
                        return value * 2
                    },
                    new ScopeStack(),
                    { argNames: ["x"], argDefaults: [] }
                )
            )

            const output = runGenerator(cls.executeStaticMethod({}, "make", [21]))
            assert.strictEqual(output, 42)
        })
    })
})

describe("ClassInstanceType", () => {
    describe("constructor / toString", () => {
        test("requires a ClassType and exposes readable string form", () => {
            assertThrows(() => new ClassInstanceType(null), "no class")
            const cls = new ClassType("Item", null)
            const instance = new ClassInstanceType(cls)
            assert.equal(instance.toString(), "<Instance of 'Item'>")
        })
    })

    describe("getAttribute", () => {
        test("works for plain attributes", () => {
            const cls = new ClassType("Item", null)
            const instance = new ClassInstanceType(cls)
            runGenerator(instance.setAttribute({}, "x", 5))
            const value = runGenerator(instance.getAttribute({}, "x"))
            assert.equal(value, 5)
        })

        test("executes getter methods", () => {
            const cls = new ClassType("Item", null)
            cls.setMember(
                "name",
                "getter method",
                new GetterMethodType(
                    "name",
                    function* (thread) {
                        const self = ThreadUtil.getCurrentStack(thread).getSelfOrThrow()
                        ThreadUtil.getStackManager(thread).prepareReturn()
                        return `value:${self.attributes.raw}`
                    },
                    new ScopeStack(),
                    { argNames: [], argDefaults: [] }
                )
            )
            const instance = new ClassInstanceType(cls)
            instance.attributes.raw = "secret"

            const value = runGenerator(instance.getAttribute({}, "name"))
            assert.strictEqual(value, "value:secret")
        })
    })

    describe("setAttribute", () => {
        test("delegates to setter methods", () => {
            const cls = new ClassType("Item", null)
            cls.setMember(
                "name",
                "setter method",
                new SetterMethodType(
                    "name",
                    function* (thread) {
                        const stack = ThreadUtil.getCurrentStack(thread)
                        const self = stack.getSelfOrThrow()
                        self.attributes.saved = stack.getSetterValueOrThrow()
                        ThreadUtil.getStackManager(thread).prepareReturn()
                        return Nothing
                    },
                    new ScopeStack(),
                    { argNames: [], argDefaults: [] }
                )
            )
            const instance = new ClassInstanceType(cls)

            runGenerator(instance.setAttribute({}, "name", 42))
            assert.strictEqual(instance.attributes.saved, 42)
        })

        test("throws when an attribute only has a getter", () => {
            const cls = new ClassType("ReadOnly", null)
            cls.setMember(
                "value",
                "getter method",
                new GetterMethodType(
                    "value",
                    function* (thread) {
                        ThreadUtil.getStackManager(thread).prepareReturn()
                        return 1
                    },
                    new ScopeStack(),
                    { argNames: [], argDefaults: [] }
                )
            )
            const instance = new ClassInstanceType(cls)

            assertGeneratorThrows(instance.setAttribute({}, "value", 10), "only has a getter")
        })
    })

    describe("executeSuperMethod", () => {
        test("calls the superclass implementation", () => {
            const base = new ClassType("Base", null)
            const sub = new ClassType("Sub", base)
            base.setMember(
                "speak",
                "instance method",
                new MethodType(
                    "speak",
                    function* (thread) {
                        const word = ThreadUtil.getCurrentStack(thread).getScopeVar("word")
                        ThreadUtil.getStackManager(thread).prepareReturn()
                        return `base:${word}`
                    },
                    new ScopeStack(),
                    { argNames: ["word"], argDefaults: [] }
                )
            )
            sub.setMember(
                "speak",
                "instance method",
                new MethodType(
                    "speak",
                    function* (thread) {
                        const word = ThreadUtil.getCurrentStack(thread).getScopeVar("word")
                        ThreadUtil.getStackManager(thread).prepareReturn()
                        return `sub:${word}`
                    },
                    new ScopeStack(),
                    { argNames: ["word"], argDefaults: [] }
                )
            )
            const instance = new ClassInstanceType(sub)

            assert.strictEqual(runGenerator(instance.executeInstanceMethod({}, "speak", ["hi"])), "sub:hi")
            assert.strictEqual(runGenerator(instance.executeSuperMethod({}, "speak", ["hi"])), "base:hi")
        })
    })

    describe("executeOperatorMethod / hasOperatorMethod", () => {
        test("use the public operator name mapping", () => {
            const cls = new ClassType("Counter", null)
            cls.setMember(
                CONFIG.INTERNAL_OP_NAMES["left add"],
                "operator method",
                new OperatorMethodType(
                    CONFIG.INTERNAL_OP_NAMES["left add"],
                    function* (thread) {
                        const stack = ThreadUtil.getCurrentStack(thread)
                        const self = stack.getSelfOrThrow()
                        const other = stack.getOtherValueOrThrow()
                        ThreadUtil.getStackManager(thread).prepareReturn()
                        return self.attributes.base + other
                    },
                    new ScopeStack(),
                    { argNames: [], argDefaults: [] }
                )
            )
            const instance = new ClassInstanceType(cls)
            instance.attributes.base = 5

            assert.strictEqual(runGenerator(instance.hasOperatorMethod("left add")), true)
            assert.strictEqual(runGenerator(instance.hasOperatorMethod("right add")), false)
            assert.strictEqual(runGenerator(instance.executeOperatorMethod({}, "left add", 7)), 12)
        })
    })
})

describe("NothingType", () => {
    describe("toString / toJSON", () => {
        test("has stable textual and JSON representation", () => {
            const n = new NothingType()
            assert.equal(n.toString(), "<Nothing>")
            assert.equal(n.toJSON(), "<Nothing>")
        })
    })

    describe("Nothing instance", () => {
        test("exports Nothing as an instance of NothingType", () => {
            assert.ok(Nothing instanceof NothingType)
            assert.equal(Nothing.toString(), "<Nothing>")
        })
    })
})

// =============================================================
// Summary
// =============================================================
console.log(`\n${passed} passed, ${failed} failed out of ${passed + failed} tests`)
if (failed > 0) process.exit(1)
