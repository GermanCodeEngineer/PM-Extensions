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
    CustomType, BaseCallableType, FunctionType, MethodType,
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
        if (messageContains && !error.message.includes(messageContains)) {
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
            assertThrows(() => m.popStackFromManager())
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

    describe("enterClassDef", () => {
        test("adds a CLASS_DEF scope with the given class", () => {
            const s = new ScopeStack()
            const cls = { name: "Foo", variables: {} }
            s.enterClassDef(cls)
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
            s.enterClassDef(cls)
            assert.strictEqual(s.getClsOrThrow("test block"), cls)
            s.exitClassDefScope()
        })

        test("throws when not in a class def scope", () => {
            const s = new ScopeStack()
            assertThrows(() => s.getClsOrThrow("test block"), "class definition")
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
            s.enterClassDef({ name: "X", variables: {} })
            s.exitClassDefScope()
            assert.equal(s.getSize(), 1)
            assert.equal(s._getInnermostScope().type, ScopeStack.GLOBALS)
        })

        test("throws when innermost is not a class def scope", () => {
            const s = new ScopeStack()
            assertThrows(() => s.exitClassDefScope())
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
            assertThrows(() => s.exitUserScope())
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

    describe("setNextFuncConfig / getAndResetNextFuncConfig", () => {
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
                s.enterClassDef(cls)
                s.setScopeVar("myProp", "value")
                assert.equal(cls.variables["myProp"], "value")
                s.exitClassDefScope()
            })
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

        test("throws for a missing variable", () => {
            const s = new ScopeStack()
            assertThrows(() => s.safeGetScopeVar("__missing_safe_scope_var__"), "is not defined")
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
                assertThrows(() => s.hasScopeVar("x", true, true))
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

describe("CustomType and subclasses", () => {
    function runGenerator(gen) {
        let result = gen.next()
        while (!result.done) result = gen.next()
        return result.value
    }

    describe("CustomType", () => {
        test("can be subclassed and participates in instanceof", () => {
            class DerivedCustomType extends CustomType {
                toString() { return "<Derived>" }
            }
            const value = new DerivedCustomType()
            assert.ok(value instanceof CustomType)
            assert.equal(value.toString(), "<Derived>")
        })
    })

    describe("BaseCallableType", () => {
        test("evaluateArgs assigns positional and default values", () => {
            const callable = new BaseCallableType(
                "f",
                function* () { return Nothing },
                new ScopeStack(),
                { argNames: ["a", "b", "c"], argDefaults: [2, 3] }
            )
            const args = callable.evaluateArgs([1])
            assert.equal(args.a, 1)
            assert.equal(args.b, 2)
            assert.equal(args.c, 3)
        })

        test("evaluateArgs throws when too many positional args are provided", () => {
            const callable = new BaseCallableType(
                "f",
                function* () { return Nothing },
                new ScopeStack(),
                { argNames: ["a"], argDefaults: [] }
            )
            assertThrows(() => callable.evaluateArgs([1, 2]), "at most")
        })
    })

    describe("FunctionType", () => {
        test("enterContext pushes function call scope with evaluated args", () => {
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

    describe("MethodType", () => {
        test("enterContext pushes method scope with self and args", () => {
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

    describe("Getter/Setter/Operator method types", () => {
        test("have expected className values", () => {
            const stack = new ScopeStack()
            const cfg = { argNames: [], argDefaults: [] }
            assert.equal(new GetterMethodType("g", function* () { return Nothing }, stack, cfg).className, "Getter Method")
            assert.equal(new SetterMethodType("s", function* () { return Nothing }, stack, cfg).className, "Setter Method")
            assert.equal(new OperatorMethodType("o", function* () { return Nothing }, stack, cfg).className, "Operator Method")
        })

        test("SetterMethodType.checkOutputValue enforces Nothing return", () => {
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

    describe("ClassType", () => {
        test("toString includes superclass info when present", () => {
            const base = new ClassType("Base", null)
            const sub = new ClassType("Sub", base)
            assert.equal(base.toString(), "<Class 'Base'>")
            assert.equal(sub.toString(), "<Class 'Sub'(super 'Base')>")
        })

        test("isSubclassOf reflects inheritance chain", () => {
            const base = new ClassType("Base", null)
            const mid = new ClassType("Mid", base)
            const sub = new ClassType("Sub", mid)
            assert.equal(sub.isSubclassOf(base), true)
            assert.equal(base.isSubclassOf(sub), false)
        })
    })

    describe("ClassInstanceType", () => {
        test("requires a ClassType and exposes readable string form", () => {
            assertThrows(() => new ClassInstanceType(null), "no class")
            const cls = new ClassType("Item", null)
            const instance = new ClassInstanceType(cls)
            assert.equal(instance.toString(), "<Instance of 'Item'>")
        })

        test("setAttribute/getAttribute work for plain attributes", () => {
            const cls = new ClassType("Item", null)
            const instance = new ClassInstanceType(cls)
            runGenerator(instance.setAttribute({}, "x", 5))
            const value = runGenerator(instance.getAttribute({}, "x"))
            assert.equal(value, 5)
        })
    })

    describe("NothingType", () => {
        test("has stable textual and JSON representation", () => {
            const n = new NothingType()
            assert.equal(n.toString(), "<Nothing>")
            assert.equal(n.toJSON(), "<Nothing>")
        })

        test("exported Nothing is an instance of NothingType", () => {
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
