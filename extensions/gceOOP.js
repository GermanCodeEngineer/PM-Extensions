// Name: OOP
// ID: gceOOP
// Description: Python-like classes and many features of Object Orientated Programming
// By: GermanCodeEngineer <https://github.com/GermanCodeEngineer/>
// License: MIT
// Made for PenguinMod
// Requires and automatically adds jwArray and dogeiscutObject
// Credit: Inspired by & Based on
//  - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jg_scripts/index.js
//  - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jwArray/index.js
//  - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jwLambda/index.js
//  - https://github.com/PenguinMod/PenguinMod-ExtensionsGallery/blob/main/static/extensions/DogeisCut/dogeiscutObject.js
//  - https://github.com/PenguinMod/PenguinMod-ExtensionsGallery/blob/main/static/extensions/VeryGoodScratcher42/More-Types.js
//  - https://github.com/SharkPool-SP/SharkPools-Extensions/blob/main/extension-code/Temporary-Variables.js

(/** @param {ScratchObject} Scratch */ function(Scratch) {
"use strict"

/**
 * Allow importing this file in a non-Scratch testing environment.
 * When the extension is imported in PenguinMod this is always true
 */
const isRuntimeEnv = !Scratch.extensions.isTestingEnv
if (isRuntimeEnv && !Scratch.extensions.unsandboxed) {
    throw new Error("OOP Extension must run unsandboxed.")
}

/************************************************************************************
*                                Custom Block Shapes                                *
************************************************************************************/

let CUSTOM_SHAPE
if (isRuntimeEnv) {
    try { // If ScratchBlocks is not avaliable, skip
    CUSTOM_SHAPE = {
        emptyInputPath: "m 16 0 h 16 h 12 a 4 4 0 0 1 4 4 l -4 4 l 4 4 l 0 8 l -4 4 l 4 4 a 4 4 0 0 1 -4 4 h -12 h -16 h -12 a 4 4 0 0 1 -4 -4 l 4 -4 l -4 -4 l 0 -8 l 4 -4 l -4 -4 a 4 4 0 0 1 4 -4 z",
        emptyInputWidth: 10 * ScratchBlocks.BlockSvg.GRID_UNIT,
        leftPath: (block) => {
            const edgeWidth = block.height / 2
            const s = edgeWidth / 16
            return [
                `h ${-12*s} `+
                `a ${4*s} ${4*s} 0 0 1 ${-4*s} ${-4*s} `+
                `l ${4*s} ${-4*s} `+
                `l ${-4*s} ${-4*s} `+
                `l 0 ${-8*s} `+
                `l ${4*s} ${-4*s} `+
                `l ${-4*s} ${-4*s} `+
                `a ${4*s} ${4*s} 0 0 1 ${4*s} ${-4*s}`
            ]
        },
        rightPath: (block) => {
            const edgeWidth = block.edgeShapeWidth_
            const s = edgeWidth / 16
            return [
                `h ${12*s} `+
                `a ${4*s} ${4*s} 0 0 1 ${4*s} ${4*s}`+
                `l ${-4*s} ${4*s} `+
                `l ${4*s} ${4*s} `+
                `l 0 ${8*s} `+
                `l ${-4*s} ${4*s} `+
                `l ${4*s} ${4*s} `+
                `a ${4*s} ${4*s} 0 0 1 ${-4*s} ${4*s}`+
                `h ${-12*s}`
            ]
        },
    }
    } catch (error) {
        console.error("[OOP Extension] Failed to create custom shape", error)
    }
}

/************************************************************************************
*                             Wrapping Some PM Internals                            *
************************************************************************************/

/**
 * @param {ScratchObject} Scratch
 */
function applyInternalWrappers(Scratch) {
    const {IRGenerator, JSGenerator} = Scratch.vm.exports
    const {TypedInput, TYPE_UNKNOWN, TYPE_BOOLEAN} = JSGenerator.exports
    const ScriptTreeGenerator = IRGenerator.exports.ScriptTreeGenerator

    // wrap Scratch.Cast.toBoolean to return false for Nothing
    const oldToBoolean = Scratch.Cast.toBoolean
    
    // Avoid multiple wrappings
    if (!oldToBoolean.isGceOOPModified) {
        /**
         * @param {*} value
         * @returns {boolean}
         */
        Scratch.Cast.toBoolean = function modifiedToBoolean(value) {
            if (value instanceof NothingType) return false
            return oldToBoolean(value)
        }
        Scratch.Cast.toBoolean.isGceOOPModified = true
    }

    // Wrap ScriptTreeGenerator.descendInput to make
    // notequals, ltorequal and gtorequal compiled blocks (as the other comparison blocks are)
    // CAN BE REMOVED START: IF THIS IS MERGED: https://github.com/PenguinMod/PenguinMod-Vm/pull/188
    const oldDescendTreeGenInput = ScriptTreeGenerator.prototype.descendInput

    if (!oldDescendTreeGenInput.isGceOOPModified) {
        /**
         * @param {Object} block
         */
        ScriptTreeGenerator.prototype.descendInput = function modifiedDescendInput (block) {
            switch (block.opcode) {
                case "operator_notequal":
                case "operator_gtorequal":
                case "operator_ltorequal":
                    const input = {
                        left: this.descendInputOfBlock(block, "OPERAND1"),
                        right: this.descendInputOfBlock(block, "OPERAND2"),
                    }
                    if      (block.opcode === "operator_notequal") input.kind = "op.notequal"
                    else if (block.opcode === "operator_gtorequal") input.kind = "op.gtorequal"
                    else if (block.opcode === "operator_ltorequal") input.kind = "op.ltorequal"
                    return input
            }
            return oldDescendTreeGenInput.call(this, block)
        }
        ScriptTreeGenerator.prototype.descendInput.isGceOOPModified = true
    }
    // CAN BE REMOVED END


    // Wrap JSGenerator.descendInput for some operator blocks to allow classes to define custom handling
    const oldDescendJSGenInput = JSGenerator.prototype.descendInput

    if (!oldDescendJSGenInput.isGceOOPModified) {
        /**
         * @param {Object} node
         * @param {boolean} visualReport
         */
        JSGenerator.prototype.descendInput = function modifiedDescendInput (node, visualReport = false) {
            let left, right, leftMethod, rightMethod
            switch (node.kind) {
                case "op.add":
                case "op.subtract":
                case "op.multiply":
                case "op.divide":
                case "op.mod":
                case "op.power":
                    left = this.descendInput(node.left).asUnknown()
                    right = this.descendInput(node.right).asUnknown()
                    leftMethod = quote("left " + node.kind.replace("op.", ""))
                    rightMethod = quote("right " + node.kind.replace("op.", ""))

                    if (node.kind === "op.mod") this.descendedIntoModulo = true // ¯\_(ツ)_/¯

                    return new TypedInput(`(yield* runtime.ext_gceOOP._binaryOperator(thread, ${left}, ${right}, `+
                        `${leftMethod}, ${rightMethod}, ${quote(node.kind)}))`, TYPE_UNKNOWN)

                case "op.equals":
                case "op.notequal":
                case "op.greater":
                case "op.gtorequal":
                case "op.less":
                case "op.ltorequal":
                    left = this.descendInput(node.left)
                    right = this.descendInput(node.right)
                    if      (node.kind === "op.equals") leftMethod = "equals"
                    else if (node.kind === "op.notequal") leftMethod = "not equals"
                    else if (node.kind === "op.greater") leftMethod = "greater than"
                    else if (node.kind === "op.gtorequal") leftMethod = "greater or equal"
                    else if (node.kind === "op.less") leftMethod = "less than"
                    else if (node.kind === "op.ltorequal") leftMethod = "less or equal"
                    // Python uses reflected operators: a < b tries b > a as fallback
                    rightMethod = {
                        "equals": "equals",
                        "not equals": "not equals",
                        "greater than": "less than",
                        "greater or equal": "less or equal",
                        "less than": "greater than",
                        "less or equal": "greater or equal",
                    }[leftMethod]
                    // I cannot really use optimizations here
                    return new TypedInput(`(yield* runtime.ext_gceOOP._comparisonOperator(thread, ${left.asUnknown()}, ${right.asUnknown()}, `+
                        `${quote(leftMethod)}, ${quote(rightMethod)}, ${quote(node.kind)}))`, TYPE_BOOLEAN)
            }
            return oldDescendJSGenInput.call(this, node, visualReport)
        }
        JSGenerator.prototype.descendInput.isGceOOPModified = true
    }


    // Wrap Runtime._convertBlockForScratchBlocks to implement hover tooltips
    const oldConvertBlock = runtime._convertBlockForScratchBlocks.bind(runtime);

    if (!oldConvertBlock.isGceOOPModified) {
        /**
         * @param {Object} blockInfo
         * @param {Object} categoryInfo
         */
        runtime._convertBlockForScratchBlocks = function(blockInfo, categoryInfo) {
            const result = oldConvertBlock(blockInfo, categoryInfo);
            if (blockInfo.tooltip) {
                result.json.tooltip = blockInfo.tooltip
            }
            return result;
        }
        runtime._convertBlockForScratchBlocks.isGceOOPModified = true
    }
}

/************************************************************************************
*                            Internal Types and Constants                           *
************************************************************************************/

const TYPEOF_MENU = [
    "Boolean",
    "Number",
    "String",

    "Function (GCE)",
    "Instance Method (GCE)",
    "Getter Method (GCE)",
    "Setter Method (GCE)",
    "Operator Method (GCE)",
    "Class (GCE)",
    "Class Instance (GCE)",
    "Nothing (GCE)",

    "Buffer (AndrewGaming587)",
    "Buffer Pointer (AndrewGaming587)",
    "Date (Old Version) (ddededodediamante)",
    "Date (ddededodediamante)",
    "Effect (Div)",
    "Iterator (Div)",
    "Object (DogeisCut)",
    "Regular Expression (DogeisCut)",
    "Set (DogeisCut)",
    "External Timer (steve0greatness)",
    "Array (jwklong)",
    "Color (jwklong)",
    "Date (jwklong)",
    "Lambda (jwklong)",
    "Number (jwklong)",
    "Target (jwklong)",
    "XML (jwklong)",
    "Canvas (RedMan13)",
    "Paint Utils Colour (Fruits555000)",
    
    "JavaScript Undefined",
    "JavaScript Null",
    "JavaScript BigInt",
    "JavaScript Symbol",
    "JavaScript Function",
    "JavaScript Object (generic)",
    "Unknown (rare)"
]

/**
 * @param {string} s
 * @returns {string}
 */
function quote(s) {
    if (typeof s !== "string") s = String(s)
    s = s.replace(/\\/g, "\\\\").replace(/'/g, "\\'")
    return `'${s}'`
}

/**
 * @param {string} text
 * @returns {string}
 */
function escapeHTML(text) {
    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;")
}

/**
 * @param {string} text
 * @returns {HTMLSpanElement}
 */
function span(text) {
    let element = document.createElement("span")
    element.innerHTML = escapeHTML(text)
    element.style.display = "hidden"
    element.style.width = "100%"
    element.style.textAlign = "center"
    return element
}

/**
 * @param {string} code
 * @param {string} additionalMsg
 * @returns {never}
 */
function throwInternal(code, additionalMsg = "") {
    throw new Error(
        `An internal error occured in the OOP extension. `+
        `Please report it in the PenguinMod discord or on GitHub. ${additionalMsg} [ERROR CODE: ${code}]`
    )
}

/**
 * @template T
 * @param {string} errorCode 
 * @param {new (...args: any[]) => T} type
 * @param {*} value
 * @returns {T}
 */
function assertType(errorCode, type, value) {
    if (!(value instanceof type)) {
        throwInternal(errorCode)
    }
    return value
}

/**
 * Manages variables for a scope. ValueHolder can be referenced from multiple VariableManager instances.
 */
class VariableManager {
    /**
     * Implements a value storage, that can be set from multiple locations.
     */
    ValueHolder = class {
        /**
         * @param {*} value
         */
        constructor(value) {
            this.value = value
            this.isDeleted = false
        }
    }

    /**
     * @param {?Object<string, *>} startVars
     */
    constructor(startVars = null) {
        this.reset()
        if (startVars) {
            for (const [name, value] of Object.entries(startVars)) {
                this.set(name, value)
            }
        }
    }
    reset() {
        if (this._variables !== undefined) {
            this.getNames().forEach((name) => this.delete(name, false))
        }
        this._variables = {}
    }

    /**
     * @param {string} name
     * @param {*} value
     */
    set(name, value) {
        if (this.has(name)) {
            this._variables[name].value = value
        } else {
            this._variables[name] = new this.ValueHolder(value)
        }
    }

    /**
     * @param {string} name
     * @param {VariableManager.ValueHolder} holder
     */
    setHolder(name, holder) {
        if (this.has(name)) {
            throw new Error(`Variable ${quote(name)} already exists in the current scope, can not bind variable with the same name.`)
        }
        this._variables[name] = holder
    }

    /**
     * @param {string} name
     * @param {boolean} throwOnNotFound
     */
    delete(name, throwOnNotFound = true) {
        if (this.has(name)) {
            this._variables[name].isDeleted = true // Mark the variable deleted for all scopes
            delete this._variables[name]
        } else if (throwOnNotFound) {
            throw new Error(`Variable ${quote(name)} is not defined.`)
        }
    }

    /**
     * @param {string} name
     * @returns {boolean}
     */
    has(name) {
        return (name in this._variables) && (!this._variables[name].isDeleted)
    }

    /**
     * @param {string} name
     * @param {boolean} throwOnNotFound
     */
    get(name, throwOnNotFound = true) {
        if (!this.has(name)) {
            if (!throwOnNotFound) return undefined
            throw new Error(`Variable ${quote(name)} is not defined.`)
        }
        return this._variables[name].value
    }

    /**
     * @returns {Object<string, *>}
     */
    getAll() {
        const result = {}
        this.getNames().forEach((name) => {
            result[name] = this.get(name, true)
        })
        return result
    }

    /**
     * @param {string} name
     * @returns {VariableManager.ValueHolder}
     */
    getHolder(name) {
        if (!this.has(name)) {
            throw new Error(`Variable ${quote(name)} is not defined.`)
        }
        return this._variables[name]
    }

    /**
     * @returns {Array<string>} 
     */
    getNames() {
        return Object.keys(this._variables).filter(name => this.has(name))
    }
}

class ThreadUtil {
    /**
     * @param {Thread} thread
     * @returns {ScopeStackManager}
     */
    static getStackManager(thread) {
        thread.gceSSM ??= new ScopeStackManager()
        return thread.gceSSM
    }

    /**
     * @param {Thread} thread
     * @returns {ScopeStack}
     */
    static getCurrentStack(thread) {
        return ThreadUtil.getStackManager(thread).getCurrentStackFromManager()
    }

    /**
     * @param {Thread} thread
     * @param {ScopeStack} stack
     */
    static pushStack(thread, stack) {
        ThreadUtil.getStackManager(thread).pushStackToManager(stack)
    }

    /**
     * @param {Thread} thread
     */
    static popStack(thread) {
        return ThreadUtil.getStackManager(thread).popStackFromManager()
    }
}

// System to switch between multiple ScopeStack's (e.g. for different scopes in function calls)
class ScopeStackManager {
    constructor() {
        /** @type {Array<ScopeStack>} */
        this.stacks = [new ScopeStack()]; // Live default stack
    }

    /**
     * @returns {ScopeStack}
     */
    getCurrentStackFromManager() {
        return this.stacks[this.stacks.length - 1]
    }

    /**
     * @param {ScopeStack} stack
     */
    pushStackToManager(stack) {
        this.stacks.push(stack)
    }

    /**
     * @returns {ScopeStack}
     */
    popStackFromManager() {
        if (this.stacks.length <= 1) {
            throwInternal("stoic-penguin")
        }
        return this.stacks.pop();
    }

    // Enter Scopes

    /**
     * @param {BaseCallableType} callable
     * @param {ContextScope} scope
     */
    insertScopeAndPushStack(callable, scope) {
        const callableStack = callable.stack.shallowCopy()
        callableStack.insertScope(scope)
        this.pushStackToManager(callableStack)
    }

    /**
     * @param {BaseCallableType} callable
     * @param {Object<string, *>} args
     */
    enterFunctionCall(callable, args) {
        this.insertScopeAndPushStack(callable, {
            type: ScopeStack.FUNCTION,
            isCallable: true, supportsVars: true,
            vars: new VariableManager(args),
        })
    }

    /**
     * @param {BaseCallableType} callable
     * @param {ClassInstanceType} self
     * @param {Object<string, *>} args
     */
    enterMethodCall(callable, self, args) {
        this.insertScopeAndPushStack(callable, {
            type: ScopeStack.METHOD,
            supportsSelf: true, isCallable: true,
            supportsVars: true,
            self, vars: new VariableManager(args),
        })
    }

    /**
     * @param {BaseCallableType} callable
     * @param {ClassInstanceType} self
     */
    enterGetterMethodCall(callable, self) {
        this.insertScopeAndPushStack(callable, {
            type: ScopeStack.GETTER_METHOD,
            supportsSelf: true, isCallable: true,
            supportsVars: true,
            self, vars: new VariableManager(),
        })
    }

    /**
     * @param {BaseCallableType} callable
     * @param {ClassInstanceType} self
     * @param {*} setterValue
     */
    enterSetterMethodCall(callable, self, setterValue) {
        this.insertScopeAndPushStack(callable, {
            type: ScopeStack.SETTER_METHOD,
            supportsSelf: true, supportsSetterValue: true, isCallable: true,
            supportsVars: true,
            self, setterValue, vars: new VariableManager(),
        })
    }

    /**
     * @param {BaseCallableType} callable
     * @param {ClassInstanceType} self
     * @param {*} other
     */
    enterOperatorMethodCall(callable, self, other) {
        this.insertScopeAndPushStack(callable, {
            type: ScopeStack.OPERATOR_METHOD,
            supportsSelf: true, supportsOtherValue: true, isCallable: true,
            supportsVars: true,
            self, other, vars: new VariableManager(),
        })
    }

    // Exit Scopes
    prepareReturn() {
        this.getCurrentStackFromManager().assertCanReturn()
        this.popStackFromManager()
    }

    // Measure Scopes

    /**
     * @returns {number}
     */
    getSize() {
        return this.stacks.length
    }

    /**
     * @param {number} size
     */
    trimSize(size) {
        if (size < 0) size = 0
        if (this.stacks.length <= size) return
        this.stacks.splice(0, this.stacks.length - size)
    }
}

// System for storing scope-like data
class ScopeStack {
    static GLOBALS = "GLOBALS"
    static FUNCTION = "FUNCTION"
    static METHOD = "METHOD"
    static GETTER_METHOD = "GETTER_METHOD"
    static SETTER_METHOD = "SETTER_METHOD"
    static OPERATOR_METHOD = "OPERATOR_METHOD"
    static CLASS_DEF = "CLASS_DEF"
    static USER_SCOPE = "USER_SCOPE"

    constructor() {

        /** @type {Array<ContextScope>} */
        this.scopes = [{
            type: ScopeStack.GLOBALS,
            isGlobalScope: true, supportsVars: true,
            vars: extensionClassInstance.globalVariables,
        }] // Item 0 is innermost
        // Use the global variables manager for all global scopes
        this.setNextFuncConfig()
    }

    /**
     * @returns {ScopeStack}
     */
    shallowCopy() { // Keep the same scope instances, but within a new array
        const newStack = new ScopeStack()
        newStack.scopes = [...this.scopes]
        return newStack
    }

    // Enter Scopes

    /**
     * @param {ContextScope} scope
     */
    insertScope(scope) {
        this.scopes.splice(0, 0, scope)
    }

    /**
     * @param {ClassType} cls
     */
    enterClassDefScope(cls) {
        this.insertScope({
            type: ScopeStack.CLASS_DEF,
            supportsCls: true,
            cls,
        })
    }

    enterUserScope() {
        this.insertScope({
            type: ScopeStack.USER_SCOPE,
            isUserScope: true,
            supportsVars: true,
            vars: new VariableManager(),
        })
    }

    // Get Scope

    /**
     * @param {function(ContextScope): boolean} qualified_fn
     * @returns {?ContextScope}
     */
    _getQualifiedScope(qualified_fn) {
        for (let i = 0; i < this.scopes.length; i++) {
            if (qualified_fn(this.scopes[i])) {
                return this.scopes[i]
            }
        }
        return null
    }

    /**
     * @returns {ContextScope}
     */
    _getInnermostScope() {
        const scope = this.scopes[0]
        if (!scope) {
            throwInternal("bold-koala")
        }
        return scope
    }

    /**
     * @returns {ClassInstanceType}
     */
    getSelfOrThrow() {
        const scope = this._getQualifiedScope(scope => scope.supportsSelf)
        if (!scope) {
            throw new Error("self can only be used within an instance, getter or setter method.")
        }
        return scope.self
    }

    /**
     * @returns {*}
     */
    getSetterValueOrThrow() {
        const scope = this._getQualifiedScope(scope => scope.supportsSetterValue)
        if (!scope) {
            throw new Error("setter value can only be used within a setter method.")
        }
        return scope.setterValue
    }

    /**
     * @returns {*}
     */
    getOtherValueOrThrow() {
        const scope = this._getQualifiedScope(scope => scope.supportsOtherValue)
        if (!scope) {
            throw new Error("other value can only be used within an operator method.")
        }
        return scope.other
    }

    /**
     * @param {string} blockText
     * @returns {ClassType}
     */
    getClsOrThrow(blockText) {
        const innermost = this._getInnermostScope()
        if (!innermost.supportsCls) {
            throw new Error(`${blockText} can only be used within a class definition or "on class" block.`)
        }
        return innermost.cls
    }

    // Exit Scopes
    assertCanReturn() {
        const innermost = this._getInnermostScope()
        if (!innermost.isCallable) {
            throw new Error("return can only be used within a function or method.")
        }
    }
    exitClassDefScope() {
        const innermost = this._getInnermostScope()
        if (!innermost.supportsCls) {
            throwInternal("nimble-panda")
        }
        this.scopes.shift()
    }
    exitUserScope() {
        const innermost = this._getInnermostScope()
        if (!innermost.isUserScope) {
            throwInternal("curious-otter")
        }
        this.scopes.shift()
    }

    // Measure Scopes

    /**
     * @returns {number} 
     */
    getSize() {
        return this.scopes.length
    }

    /**
     * @param {number} size
     */
    trimSize(size) {
        if (size < 0) size = 0
        if (this.scopes.length <= size) return
        this.scopes.splice(0, this.scopes.length - size)
    }

    // Function Arguments

    /**
     * @param {?FunctionArgConfig} config
     */
    setNextFuncConfig(config) {
        config = config || ScopeStack.getDefaultFuncConfig()
        if (config.argDefaults.length > config.argNames.length) {
            throw new Error("There can only be as many default values as argument names.")
        }
        this.nextFuncConfig = config
    }

    /**
     * @returns {FunctionArgConfig}
     */
    getAndResetNextFuncConfig() {
        const config = this.nextFuncConfig
        this.setNextFuncConfig()
        return config
    }

    /**
     * @returns {FunctionArgConfig}
     */
    static getDefaultFuncConfig() {
        return {argNames: [], argDefaults: []}
    }

    // Access Scoped Variables

    /**
     * @param {string} name
     * @param {*} value
     */
    setScopeVar(name, value) {
        const innermost = this._getInnermostScope()
        if (!innermost.supportsVars) {
            throw new Error("Can not set a variable in a scope, which does not support variables (e.g. a class definition).")
        }
        innermost.vars.set(name, value)
    }

    /**
     * @param {string} name
     * @param {number} startIndex
     * @param {number} excludeLastIndecies
     * @param {boolean} throwOnNotFound
     * @returns {?ContextScope}
     */
    _getScopeOfVar(name, startIndex = 0, excludeLastIndecies = 0, throwOnNotFound = true) {
        for (let i = startIndex; i < (this.scopes.length - excludeLastIndecies); i++) {
            const scope = this.scopes[i]
            if (!scope.supportsVars) continue
            if (scope.vars.has(name)) return scope
        }
        if (!throwOnNotFound) {
            return null
        }
        // trick to raise:
        (new VariableManager()).get(name, true)
    }

    /**
     * @param {string} name
     * @param {boolean} throwOnNotFound
     * @returns {*}
     */
    getScopeVar(name, throwOnNotFound = true) {
        const varScope = this._getScopeOfVar(name, 0, 0, throwOnNotFound)
        if (!varScope) return undefined
        return varScope.vars.get(name, throwOnNotFound)
    }

    /**
     * @param {string} name
     */
    deleteScopeVar(name) {
        const innermost = this._getInnermostScope()
        if (!innermost.supportsVars) {
            throw new Error("Can not delete a variable in a scope, which does not support variables(e.g. a class definition).")
        }
        innermost.vars.delete(name)
    }

    /**
     * @param {string} name
     */
    bindScopeVarGlobal(name) {
        const globalScope = this._getQualifiedScope(scope => scope.isGlobalScope)
        if (!globalScope) {
            throwInternal("calm-seal")
        }
        if (!globalScope.vars.has(name)) {
            throw new Error(`No global variable named ${quote(name)} found.`)
        }

        const innermost = this._getInnermostScope()
        if (!innermost.supportsVars) {
            throw new Error("Can not bind a variable to a scope, which does not support variables(e.g. a class definition).")
        }
        innermost.vars.setHolder(name, globalScope.vars.getHolder(name))
    }

    /**
     * @param {string} name
     */
    bindScopeVarNonlocal(name) {
        let varScope
        try { // skip innermost(current) and global scope, as nonlocal variables can not be in either
            varScope = this._getScopeOfVar(name, 1, 1)
        } catch {
            throw new Error(`No non-local variable named ${quote(name)} found.`)
        }

        const innermost = this._getInnermostScope()
        if (!innermost.supportsVars) {
            throw new Error("Can not bind a variable to a scope, which does not support variables(e.g. a class definition).")
        }
        innermost.vars.setHolder(name, varScope.vars.getHolder(name))
    }

    /**
     * @param {boolean} onlyCurrentScope - if true, return names only from the innermost scope
     * @param {boolean} onlyGlobalScope - if true, return names only from the global scope
    * @returns {boolean}
     */
    hasScopeVar(name, onlyCurrentScope = false, onlyGlobalScope = false) {
        if (onlyCurrentScope && onlyGlobalScope) {
            throwInternal("bold-raven")
        }
        if (onlyCurrentScope) {
            const innermost = this._getInnermostScope()
            if (!innermost.supportsVars) return false
            return innermost.vars.has(name)
        }
        if (onlyGlobalScope) {
            const globalScope = this._getQualifiedScope(scope => scope.isGlobalScope)
            if (!globalScope) throwInternal("spry-fox")
            if (!globalScope.supportsVars) throwInternal("toic-panda")
            return globalScope.vars.has(name)
        }
        return this._getScopeOfVar(name, 0, 0, false) !== null
    }

    /**
     * Return an array with all variable names visible in the current thread environment.
     * Iterates from outermost to innermost so inner-scope variables override outer ones.
     * @param {boolean} onlyCurrentScope - if true, return names only from the innermost scope
     * @param {boolean} onlyGlobalScope - if true, return names only from the global scope
     * @returns {Array<string>}
     */
    getScopeVarNames(onlyCurrentScope = false, onlyGlobalScope = false) {
        if (onlyCurrentScope && onlyGlobalScope) throwInternal("brave-fox")
        if (onlyCurrentScope) {
            const innermost = this._getInnermostScope()
            if (!innermost.supportsVars) return []
            return innermost.vars.getNames()
        }
        if (onlyGlobalScope) {
            const globalScope = this._getQualifiedScope(scope => scope.isGlobalScope)
            if (!globalScope) throwInternal("mirthful-seal")
            if (!globalScope.supportsVars) throwInternal("quiet-heron")
            return globalScope.vars.getNames()
        }

        const map = new Map()
        for (let i = this.scopes.length - 1; i >= 0; i--) {
            // iterate outermost -> innermost so inner scopes override outer ones
            const scope = this.scopes[i]
            if (!scope.supportsVars) continue
            const names = scope.vars.getNames()
            for (const n of names) {
                if (map.has(n)) map.delete(n)
                map.set(n, true)
            }
        }
        return Array.from(map.keys())
    }
}

const {BlockType, BlockShape, ArgumentType} = Scratch
const runtime = Scratch.vm.runtime

const CONFIG = {
    INIT_METHOD_NAME: "__special_init__",
    AS_STRING_METHOD_NAME: "__special_as_string__",
    INTERNAL_OP_NAMES: {}, // see below
    PUBLIC_OP_NAMES: {}, // see below
};
([
    "left add", "right add",
    "left subtract", "right subtract",
    "left multiply", "right multiply",
    "left divide", "right divide",
    "left power", "right power",
    "left mod", "right mod",

    "equals", "not equals",
    "greater than", "greater or equal",
    "less than", "less or equal",
]).forEach((publicName) => {
    const internalName = `__operator_${publicName.replaceAll(" ", "_")}__`
    CONFIG.INTERNAL_OP_NAMES[publicName] = internalName
    CONFIG.PUBLIC_OP_NAMES[internalName] = publicName
})

const MENU_ITEMS = {
    CLASS_PROPERTY: [
        "instance method",
        "static method",
        "getter method",
        "setter method",
        "operator method",
        "class variable",
    ],
    SPECIAL_METHOD: [
        {text: "init", value: CONFIG.INIT_METHOD_NAME},
        {text: "as string", value: CONFIG.AS_STRING_METHOD_NAME},
    ],
    TYPEOF_MENU: TYPEOF_MENU,
    OPERATOR_METHOD: CONFIG.INTERNAL_OP_NAMES
        ? Object.entries(CONFIG.INTERNAL_OP_NAMES).map(([publicName, internalName]) => ({text: publicName, value: internalName}))
        : [],
}


class TypeChecker {
    // All custom types (using `customId`) one can get from a reporter in PM
    // (PenguinMod-Vm, PenguinMod-ExtensionsGallery, SharkPools-Extensions) (as of 14.04.2026)
    // agBuffer (AndrewGaming587)
    // agBufferPointer (AndrewGaming587)
    // canvasData (RedMan13)
    // ddeDateFormat (ddededodediamante)
    // ddeDateFormatV2 (ddededodediamante)
    // divEffect (Div)
    // divIterator (Div)
    // dogeiscutObject (DogeisCut)
    // dogeiscutRegularExpression (DogeisCut)
    // dogeiscutSet (DogeisCut)
    // externaltimer (steve0greatness)
    // jwArray (jwklong)
    // jwColor (jwklong)
    // jwDate (jwklong)
    // jwLambda (jwklong)
    // jwNum (jwklong)
    // jwTarget (jwklong)
    // jwVector (jwklong)
    // jwXML (jwklong)
    // paintUtilsColour (Fruits555000)

    // My Types
    // FunctionType
    // MethodType
    // ClassType
    // ClassInstanceType
    // NothingType

    static is_agBuffer = TypeChecker._createVMTypeCheck("agBuffer")
    static is_agBufferPointer = TypeChecker._createVMTypeCheck("agBuffer", "PointerType")
    
    /**
     * @param {*} value
     * @returns {boolean}
     */
    static is_canvasData(value) {
        TypeChecker._assertRuntimeEnv()
        if (!runtime._extensionVariables) return false
        const type = runtime._extensionVariables.canvas
        if (!type) return false
        return value instanceof type
    }

    /**
     * @param {*} value
     * @returns {boolean}
     */
    static is_ddeDateFormat(value) {
        TypeChecker._assertRuntimeEnv()
        if (runtime.ext_ddeDateFormat) {
            try {
                const dateType = Object.getPrototypeOf(runtime.ext_ddeDateFormat.currentDate())
                if (value instanceof dateType) return true
            } catch {}
        }
    }
    
    /**
     * @param {*} value
     * @returns {boolean}
     */
    static is_ddeDateFormatV2(value) {
        TypeChecker._assertRuntimeEnv()
        if (runtime.ext_ddeDateFormatV2) {
            try {
                const dateType = Object.getPrototypeOf(runtime.ext_ddeDateFormatV2.currentDate())
                if (value instanceof dateType) return true
            } catch {}
        }
        return false
    }

    static is_divEffect = TypeChecker._createVMTypeCheck("divAlgEffects", "Effect")
    static is_divIterator = TypeChecker._createVMTypeCheck("divIterator")
    static is_dogeiscutObject = TypeChecker._createVMTypeCheck("dogeiscutObject", null, "Object extension was not loaded properly.")
    static is_dogeiscutRegularExpression = TypeChecker._createVMTypeCheck("dogeiscutRegularExpression")
    static is_dogeiscutSet = TypeChecker._createVMTypeCheck("dogeiscutSet")

    /**
     * @param {*} value
     * @returns {boolean}
     */
    static is_externaltimer(value) {
        TypeChecker._assertRuntimeEnv()
        if (!runtime._extensionVariables) return false
        const type = runtime._extensionVariables.externaltimer
        if (!type) return false
        return value instanceof type
    }

    static is_jwArray = TypeChecker._createVMTypeCheck("jwArray", null, "Array extension was not loaded properly.")
    static is_jwColor = TypeChecker._createVMTypeCheck("jwColor")
    static is_jwDate = TypeChecker._createVMTypeCheck("jwDate")
    static is_jwLambda = TypeChecker._createVMTypeCheck("jwLambda")
    static is_jwNum = TypeChecker._createVMTypeCheck("jwNum")
    static is_jwTarget = TypeChecker._createVMTypeCheck("jwTargets")
    static is_jwVector = TypeChecker._createVMTypeCheck("jwVector")
    static is_jwXML = TypeChecker._createVMTypeCheck("jwXML")
    
    /**
     * @param {*} value
     * @returns {boolean}
     */
    static is_paintUtilsColour(value) {
        TypeChecker._assertRuntimeEnv()
        if (!runtime.ext_fruitsPaintUtils || typeof runtime.ext_fruitsPaintUtils.getColour !== "function") return false

        try {
            const proto = Object.getPrototypeOf(runtime.ext_fruitsPaintUtils.getColour({COLOUR_NAME: "orange"}))
            return value instanceof proto
        } catch {
            return false
        }
    }



    static _assertRuntimeEnv() {
        if (!isRuntimeEnv) {
            throw new Error("Type checking for extension types is not available in a non-runtime environment.")
        }
    }

    /**
     * @param {string} typeId
     * @param {?string} overrideTypeProperty
     * @param {string} [errMsg] - optional error message if type missing
     * @returns {(value: *) => boolean}
     */
    static _createVMTypeCheck(typeId, overrideTypeProperty = null, typeMissingErrorMsg = null) {
        return function isType(value) {
            if (!isRuntimeEnv) return false
            const typeInfo = Scratch.vm[typeId]
            if (!typeInfo) {
                if (typeMissingErrorMsg) throw new Error(typeMissingErrorMsg)
                return false
            }

            let typeClass
            try {
                typeClass = overrideTypeProperty ? typeInfo[overrideTypeProperty] : typeInfo.Type
            } catch {
                if (typeMissingErrorMsg) throw new Error(typeMissingErrorMsg)
                return false
            }
            return value instanceof typeClass
        }
    }

    /**
     * @param {*} value
     * @returns {boolean}
     */
    static isMissingValue(value) {
        return ((value === undefined) || (value === null))
    }

    /**
     * @param {*} value
     * @returns {boolean}
     */
    static isClassicScratchValue(value) {
        return ((typeof value === "boolean") || (typeof value === "number") || (typeof value === "string"))
    }

    /**
     * @param {*} value
     * @returns {string}
     */
    static stringTypeof(value) {
        // My Types
        if (value instanceof FunctionType) return "Function (GCE)"
        if (value instanceof MethodType) return "Instance Method (GCE)"
        if (value instanceof GetterMethodType) return "Getter Method (GCE)"
        if (value instanceof SetterMethodType) return "Setter Method (GCE)"
        if (value instanceof OperatorMethodType) return "Operator Method (GCE)"

        if (value instanceof ClassType) return "Class (GCE)"
        if (value instanceof ClassInstanceType) return "Class Instance (GCE)"
        if (value instanceof NothingType) return "Nothing (GCE)"

        // Common/Safe JS data types
        if (value === undefined) return "JavaScript Undefined"
        if (value === null) return "JavaScript Null"
        if (typeof value === "boolean") return "Boolean"
        if (typeof value === "number") return "Number"
        if (typeof value === "string") return "String"

        // Custom Extension Types 
        if (TypeChecker.is_agBuffer(value)) return "Buffer (AndrewGaming587)"
        if (TypeChecker.is_agBufferPointer(value)) return "Buffer Pointer (AndrewGaming587)"
        if (TypeChecker.is_ddeDateFormat(value)) return "Date (Old Version) (ddededodediamante)"
        if (TypeChecker.is_ddeDateFormatV2(value)) return "Date (ddededodediamante)"
        if (TypeChecker.is_divEffect(value)) return "Effect (Div)"
        if (TypeChecker.is_divIterator(value)) return "Iterator (Div)"
        if (TypeChecker.is_dogeiscutObject(value)) return "Object (DogeisCut)"
        if (TypeChecker.is_dogeiscutRegularExpression(value)) return "Regular Expression (DogeisCut)"
        if (TypeChecker.is_dogeiscutSet(value)) return "Set (DogeisCut)"
        if (TypeChecker.is_externaltimer(value)) return "External Timer (steve0greatness)"
        if (TypeChecker.is_jwArray(value)) return "Array (jwklong)"
        if (TypeChecker.is_jwColor(value)) return "Color (jwklong)"
        if (TypeChecker.is_jwDate(value)) return "Date (jwklong)"
        if (TypeChecker.is_jwLambda(value)) return "Lambda (jwklong)"
        if (TypeChecker.is_jwNum(value)) return "Number (jwklong)"
        if (TypeChecker.is_jwTarget(value)) return "Target (jwklong)"
        if (TypeChecker.is_jwVector(value)) return "Vector (jwklong)"
        if (TypeChecker.is_jwXML(value)) return "XML (jwklong)"
        if (TypeChecker.is_canvasData(value)) return "Canvas (RedMan13)"
        if (TypeChecker.is_paintUtilsColour(value)) return "Paint Utils Colour (Fruits555000)"

        // Rare/Overlapping JS data types
        if (typeof value === "bigint") return "JavaScript BigInt"
        if (typeof value === "symbol") return "JavaScript Symbol"
        if (typeof value === "function") return "JavaScript Function"
        if (typeof value === "object") return "JavaScript Object (generic)"

        return "Unknown (rare)"
    }
}


class Cast extends Scratch.Cast {
    static _assertRuntimeEnv() {
        if (!isRuntimeEnv) {
            throw new Error("Casting to extension types is not available in a non-runtime environment.")
        }
    }

    // Foreign

    /**
     * @param {*} value
     * @returns {Scratch.vm.jwArray.Type}
     */
    static toArray(value) {
        Cast._assertRuntimeEnv()
        if (!Scratch.vm.jwArray) throw new Error("Array extension was not loaded properly.")
        return Scratch.vm.jwArray.Type.toArray(value)
    }

    /**
     * @param {*} value
     * @param {boolean} copy
     * @returns {Scratch.vm.dogeiscutObject.Type}
     */
    static toObject(value, copy = false) {
        Cast._assertRuntimeEnv()
        if (!Scratch.vm.dogeiscutObject) throw new Error("Object extension was not loaded properly.")
        return Scratch.vm.dogeiscutObject.Type.toObject(value, copy)
    }

    // Helpers

    /**
     * @param {string} name
     * @param {?Thread} thread
     * @param {boolean} throwOnNotFound
     * @returns {*}
     */
    static _getNamedValue(name, thread = null) {
        if (thread) {
            return ThreadUtil.getCurrentStack(thread).getScopeVar(name, true)
        }
        return extensionClassInstance.globalVariables.get(name, true)
    }

    /**
     * @param {*} value
     * @param {?Thread} thread
     * @param {typeof CustomType} expectedType
     * @param {string} expectedDescription
     * @returns {*}
     */
    static _toTypeFromValueOrVariable(value, thread, expectedType, expectedDescription) {
        if (value instanceof expectedType) return value
        if (TypeChecker.isMissingValue(value)) {
            throw new Error(`Expected a ${expectedDescription}, but got no input value.`)
        }
        if (!(TypeChecker.isClassicScratchValue(value))) { // Allow access to a variable named e.g. 513
            throw new Error(`Expected a ${expectedDescription} not a ${TypeChecker.stringTypeof(value)}.`)
        }
        const name = Cast.toString(value)
        let varValue
        try {
            varValue = Cast._getNamedValue(name, thread)
        } catch {
            throw new Error(`Expected a ${expectedDescription}, but variable ${quote(value)} is not defined.`)
        }
        if (varValue instanceof expectedType) return varValue
        throw new Error(`Expected a ${expectedDescription}, but variable ${quote(value)} is a ${TypeChecker.stringTypeof(varValue)}.`)
    }

    // Own

    /**
     * @param {*} value
     * @param {?Thread} thread
     * @returns {ClassType}
     */
    static toClass(value, thread = null) {
        return Cast._toTypeFromValueOrVariable(value, thread, ClassType, "class or class variable name")
    }

    /**
     * @param {*} value
     * @param {?Thread} thread
     * @returns {ClassInstanceType}
     */
    static toClassInstance(value, thread = null) {
        return Cast._toTypeFromValueOrVariable(value, thread, ClassInstanceType, "class instance or class instance variable name")
    }

    /**
     * @param {*} value
     * @param {?Thread} thread
     * @returns {FunctionType}
     */
    static toFunction(value, thread = null) {
        return Cast._toTypeFromValueOrVariable(value, thread, FunctionType, "function or function variable name")
    }

    // Menus

    static toMenuClassProperty(value) {
        value = Cast.toString(value)
        if (!MENU_ITEMS.CLASS_PROPERTY.includes(value)) {
            throw new Error(`Invalid class property: ${value}`)
        }
        return value
    }

    static toMenuOperatorMethod(value) {
        value = Cast.toString(value)
        if (!MENU_ITEMS.OPERATOR_METHOD.includes(value)) {
            throw new Error(`Invalid operator method: ${value}`)
        }
        return value
    }

    static toMenuSpecialMethod(value) {
        value = Cast.toString(value)
        if (!MENU_ITEMS.SPECIAL_METHOD.includes(value)) {
            throw new Error(`Invalid special method: ${value}`)
        }
        return value
    }

    static toMenuTypeofType(value) {
        value = Cast.toString(value)
        if (!MENU_ITEMS.TYPEOF_MENU.includes(value)) {
            throw new Error(`Invalid typeof type: ${value}`)
        }
        return value
    }
}

/************************************************************************************
*                            Dependencies and Value Types                           *
************************************************************************************/

const jwArrayStub = {
    Type: null,
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: BlockShape.SQUARE,
        forceOutputType: "Array",
        //allowDropAnywhere: true,
        disableMonitor: true
    },
    Argument: {
        shape: BlockShape.SQUARE,
        exemptFromNormalization: true,
        check: ["Array"],
        compilerInfo: {
            jwArrayUnmodified: true
        },
    },
}
const dogeiscutObjectStub = {
    Type: null,
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: BlockShape.PLUS,
        forceOutputType: "Object",
        disableMonitor: true,
    },
    Argument: {
        shape: BlockShape.PLUS,
        exemptFromNormalization: true,
        check: ["Object"],
    },
}

class CustomType {
    toMonitorContent() {
        return span(this.toString())
    }

    // Prevent dogeiscut rendering my custom types as objects
    dogeiscutObjectHandler() {
        return span(this.toString()).outerHTML
    }

    // Render my custom types fully, instead of "Object"
    jwArrayHandler() {
        return span(this.toString()).outerHTML
    }
}

class BaseCallableType extends CustomType {
    className = "Callable"
    // Technically this name will never be shown, as only subclasses actually have instances
    // Should allow s-plural

    /**
     * @param {string} name
     * @param {Function} jsFunc
     * @param {ScopeStack} stack
     * @param {FunctionArgConfig} config
     */
    constructor(name, jsFunc, stack, config) {
        super()
        this.name = name
        this.jsFunc = jsFunc
        this.stack = stack.shallowCopy()
        this.argNames = config.argNames
        this.argDefaults = config.argDefaults
    }

    /**
     * @returns {string}
     */
    toString() {
        return `<${this.className} ${quote(this.name)}>`
    }

    /**
     * @returns {string}
     */
    toJSON() {
        return `${this.className}s can not be serialized.`
    }

    /**
     * @param {Thread} thread
     * @param {...*} paramsForEnterContext - class instance and other shadow values from the block (e.g., instance, posArgs, setter value, other operand)
     * @returns {*} the return value of the method
     */
    *execute(thread, ...paramsForEnterContext) {
        const sizeBefore = ThreadUtil.getCurrentStack(thread).getSize()
        this.enterContext(thread, ...paramsForEnterContext)

        let output
        let finished = false
        try {
            output = (yield* this.jsFunc(thread))
            finished = true
        } finally {
            if (finished) {
                if (sizeBefore !== ThreadUtil.getCurrentStack(thread).getSize()) {
                    throwInternal("clever-badger")
                }
            } else {
                // An error happend, so exit stack frames that where interrupted
                ThreadUtil.getCurrentStack(thread).trimSize(sizeBefore)
            }

        }
        this.checkOutputValue(output)
        return output
    }

    /**
     * @param {Thread} thread
     */
    enterContext(thread) {
        // Allow better subclassing
    }

    /**
     * @param {*} output
     */
    checkOutputValue(output) {
        // Allow better subclassing
    }


    /**
     * @param {Array} posArgs
     * @returns {Object<string, *>}
     */
    evaluateArgs(posArgs) {
        const args = {}
        let name
        let prefix

        if (this instanceof MethodType && (this.name === CONFIG.INIT_METHOD_NAME)) prefix = "Initializing object"
        else if (this instanceof MethodType) prefix = `Calling method ${quote(this.name)}`
        else prefix = `Calling function ${quote(this.name)}`

        // Ensure there are not too many arguments
        if (posArgs.length > this.argNames.length) {
            throw new Error(`${prefix}: expected at most ${this.argNames.length}, but got ${posArgs.length} arguments.`)
        }

        // Count how many arguments do NOT have defaults
        const posOnlyCount = this.argNames.length - this.argDefaults.length

        // Ensure enough positional arguments
        if (posArgs.length < posOnlyCount) {
            throw new Error(`${prefix}: expected at least ${posOnlyCount} positional arguments, but got only ${posArgs.length}.`)
        }

        // Assign positional arguments
        for (let i = 0; i < posArgs.length; i++) {
            name = this.argNames[i]
            args[name] = posArgs[i]
        }

        // Fill in defaults for missing arguments
        const defaultsStartIndex = this.argNames.length - this.argDefaults.length
        for (let i = posArgs.length; i < this.argNames.length; i++) {
            name = this.argNames[i]
            const defaultIndex = i - defaultsStartIndex
            args[name] = this.argDefaults[defaultIndex]
        }

        return args
    }
}

class FunctionType extends BaseCallableType {
    customId = "gceFunction"
    className = "Function"

    /**
     * @param {Thread} thread
     * @param {PositionalFunctionArgs} posArgs
     */
    enterContext(thread, posArgs) {
        // Allow better subclassing
        const args = this.evaluateArgs(posArgs)
        ThreadUtil.getStackManager(thread).enterFunctionCall(this, args)
    }
}

class MethodType extends BaseCallableType {
    customId = "gceMethod"
    className = "Method"

    /**
     * @param {Thread} thread
     * @param {ClassInstanceType} instance
     * @param {PositionalFunctionArgs} posArgs
     */
    enterContext(thread, instance, posArgs) {
        // Allow better subclassing
        const args = this.evaluateArgs(posArgs)
        ThreadUtil.getStackManager(thread).enterMethodCall(this, instance, args)
    }
}

class GetterMethodType extends MethodType {
    customId = "gceGetterMethod"
    className = "Getter Method"

    /**
     * @param {Thread} thread
     * @param {ClassInstanceType} instance
     */
    enterContext(thread, instance) {
        ThreadUtil.getStackManager(thread).enterGetterMethodCall(this, instance)
    }
}
class SetterMethodType extends MethodType {
    customId = "gceSetterMethod"
    className = "Setter Method"

    /**
     * @param {Thread} thread
     * @param {ClassInstanceType} instance
     * @param {*} value
     */
    enterContext(thread, instance, value) {
        ThreadUtil.getStackManager(thread).enterSetterMethodCall(this, instance, value)
    }

    /**
     * @param {*} output
     */
    checkOutputValue(output) {
        if (output !== Nothing) throw new Error(`Setter methods must return ${Nothing}.`)
    }
}

class OperatorMethodType extends MethodType {
    customId = "gceOperatorMethod"
    className = "Operator Method"

    /**
     * @param {Thread} thread
     * @param {ClassInstanceType} instance
     * @param {*} other
     */
    enterContext(thread, instance, other) {
        ThreadUtil.getStackManager(thread).enterOperatorMethodCall(this, instance, other)
    }
}

class ClassType extends CustomType {
    customId = "gceClass"

    /**
     * @param {string} name
     * @param {?ClassType} superCls
     */
    constructor(name, superCls) {
        super()
        this.name = name
        this.superCls = superCls
        this.instanceMethods = {}
        this.staticMethods = {}
        this.getters = {}
        this.setters = {}
        this.operatorMethods = {}
        this.clsVariables = new VariableManager()
    }

    /**
     * @returns string
     */
    toString() {
        const suffix = this.superCls ? `(super ${quote(this.superCls.name)})` : ""
        return `<Class ${quote(this.name)}${suffix}>`
    }

    /**
     * @returns string
     */
    toJSON() {
        return "Classes can not be serialized."
    }

    /**
     * @param {string} name
     * @param {boolean} recursive
     * @param {boolean} preferSetter
     * @returns {{type: ?string, value: *}}
     */
    getMember(name, recursive, preferSetter) {
        if (name in this.instanceMethods) return {type: "instance method", value: this.instanceMethods[name]}
        else if (name in this.staticMethods) return {type: "static method", value: this.staticMethods[name]}
        else if ((name in this.getters) && (name in this.setters)) {
            if (preferSetter) return {type: "setter method", value: this.setters[name]}
            else return {type: "getter method", value: this.getters[name]}
        }
        else if (name in this.getters) return {type: "getter method", value: this.getters[name]}
        else if (name in this.setters) return {type: "setter method", value: this.setters[name]}
        else if (name in this.operatorMethods) return {type: "operator method", value: this.operatorMethods[name]}
        else if (this.clsVariables.has(name)) return {type: "class variable", value: this.clsVariables.get(name)}
        if (recursive) {
            if (!this.superCls) return {type: null}
            return this.superCls.getMember(name, recursive, preferSetter)
        } else {
            return {type: null}
        }
    }

    /**
     * @param {string} name
     * @param {string} expectedMemberType
     * @returns {*}
     */
    getMemberOfType(name, expectedMemberType) {
        const {type, value} = this.getMember(name, true, expectedMemberType === "setter method")
        if (!type) throw new Error(`Undefined ${expectedMemberType} ${quote(name)}.`)
        if (type !== expectedMemberType) throw new Error(`Class Method or Variable ${quote(name)} is not a ${expectedMemberType} but a ${type}.`)
        return value
    }

    /**
     * @returns {Array<Object<string, *>>}
     */
    getAllMembers() {
        let currentCls = this
        /** @type {Array<ClassType>} */
        const classChain = [] // From top superclass to subclass
        while (currentCls) {
            classChain.splice(0, 0, currentCls)
            currentCls = currentCls.superCls
        }
        const instanceMethods = {}
        const staticMethods = {}
        const getterMethods = {}
        const setterMethods = {}
        const operatorMethods = {}
        const clsVariables = {}
        classChain.forEach((cls) => {
            Object.assign(instanceMethods, cls.instanceMethods)
            Object.assign(staticMethods, cls.staticMethods)
            Object.assign(getterMethods, cls.getters)
            Object.assign(setterMethods, cls.setters)
            Object.assign(operatorMethods, cls.operatorMethods)
            Object.assign(clsVariables, cls.clsVariables.getAll())
        })
        return [instanceMethods, staticMethods, getterMethods, setterMethods, operatorMethods, clsVariables]
    }

    /**
     * @param {string} name
     * @param {string} newMemberType
     * @param {*} value
     */
    setMember(name, newMemberType, value) {
        const currentMemberType = this.getMember(name, false, false).type // preference does not matter
        if (currentMemberType && (currentMemberType !== newMemberType) && !(
            ((currentMemberType === "getter method") && (newMemberType === "setter method")) ||
            ((currentMemberType === "setter method") && (newMemberType === "getter method"))
        )) {
            throw new Error(`Can not assign ${newMemberType}: ${currentMemberType} already exists with the same name ${quote(name)}.`)
        }
        if (newMemberType === "instance method") this.instanceMethods[name] = value
        else if (newMemberType === "static method") this.staticMethods[name] = value
        else if (newMemberType === "getter method") this.getters[name] = value
        else if (newMemberType === "setter method") this.setters[name] = value
        else if (newMemberType === "operator method") this.operatorMethods[name] = value
        else if (newMemberType === "class variable") this.clsVariables.set(name, value)
    }

    /**
     * @param {string} name 
     * @param {string} memberType 
     */
    deleteMemberOfType(name, memberType) {
        this.getMemberOfType(name, memberType) // check if member exists and is of the right type, will throw an error if not
        switch (memberType) {
            case "instance method":
                delete this.instanceMethods[name]
                break
            case "static method":
                delete this.staticMethods[name]
                break
            case "getter method":
                delete this.getters[name]
                break
            case "setter method":
                delete this.setters[name]
                break
            case "operator method":
                delete this.operatorMethods[name]
                break
            case "class variable":
                this.clsVariables.delete(name)
                break
        }
    }    

    /**
     * @param {Thread} thread
     * @param {PositionalFunctionArgs} posArgs
     * @returns {ClassInstanceType} the instance
     */
    *createInstance(thread, posArgs) {
        const instance = new ClassInstanceType(this)
        const output = yield* instance.executeInstanceMethod(thread, CONFIG.INIT_METHOD_NAME, posArgs) // an init method always exists
        if (output !== Nothing) throw new Error(`Initialization methods must return ${Nothing}.`)
        return instance
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {PositionalFunctionArgs} posArgs
     * @returns {*}
     */
    *executeStaticMethod(thread, name, posArgs) {
        const methodFunc = this.getStaticMethod(name)
        return yield* methodFunc.execute(thread, posArgs)
    }

    /**
     * @param {string} name 
     * @returns {FunctionType}
     */
    getStaticMethod(name) {
        return assertType("quiet-fox", FunctionType, this.getMemberOfType(name, "static method"))
    }

    /**
     * @param {ClassType} superCls
     * @returns {boolean}
     */
    isSubclassOf(superCls) {
        if (this === superCls) return true
        let currentCls = this
        while (currentCls.superCls) {
            if (currentCls.superCls === superCls) return true
            currentCls = currentCls.superCls
        }
        return false
    }
}

class ClassInstanceType extends CustomType {
    customId = "gceClassInstance"

    /**
     * @param {ClassType} cls
     */
    constructor(cls) {
        super()
        this.cls = cls
        this.attributes = {}
    }
    toString() {
        return `<Instance of ${quote(this.cls.name)}>`
    }
    toJSON() {
        return "Class Instances can not be serialized."
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {PositionalFunctionArgs} posArgs
     * @returns {*} the return value of the method
     */
    *executeInstanceMethod(thread, name, posArgs) {
        /** @type {MethodType} */
        const method = this.cls.getMemberOfType(name, "instance method")
        return yield* method.execute(thread, this, posArgs)
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {PositionalFunctionArgs} posArgs
     * @returns {*} the return value of the method
     */
    *executeSuperMethod(thread, name, posArgs) {
        if (!this.cls.superCls) throw new Error("Can not call super instance method: class has no superclass.")

        /** @type {MethodType} */
        const method = this.cls.superCls.getMemberOfType(name, "instance method")
        return yield* method.execute(thread, this, posArgs)
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {PositionalFunctionArgs} posArgs
     * @returns {*} the return value of the method
     */
    *executeSuperInitMethod(thread, name, posArgs) {
        const output = yield* this.executeSuperMethod(thread, name, posArgs)
        if (output !== Nothing) throw new Error(`Initialization methods must return ${Nothing}.`)
        return output
    }

    /**
     * @param {Thread} thread
     * @param {string} name public operator method name
     * @param {*} other
     * @returns {*} the return value of the operator method
     */
    *executeOperatorMethod(thread, name, other) {
        /** @type {OperatorMethodType} */
        const method = this.cls.getMemberOfType(CONFIG.INTERNAL_OP_NAMES[name], "operator method")
        return yield* method.execute(thread, this, other)
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @returns {*} the attribute value or return value of getter method
     */
    *getAttribute(thread, name) {
        const {type, value} = this.cls.getMember(name, true, false)
        if (type === "getter method") {
            /** @type {GetterMethodType} */
            const getterMethod = value
            return (yield* getterMethod.execute(thread, this))
        }
        if (name in this.attributes) {
            return this.attributes[name]
        }
        throw new Error(`${this} has no attribute or getter method for ${quote(name)}.`)
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {string} value
     */
    *setAttribute(thread, name, value) {
        const methodMember = this.cls.getMember(name, true, true)
        if (methodMember && methodMember.type === "setter method") {
            yield* methodMember.value.execute(thread, this, value)
        } else if (methodMember && methodMember.type === "getter method") {
            throw new Error(`Can not set attribute ${quote(name)} of ${this}: attribute only has a getter method.`)
        } else {
            this.attributes[name] = value
        }
    }

    /**
     * @param {string} name public operator method name
     * @returns {boolean}
     */
    *hasOperatorMethod(name) {
        try {
            this.cls.getMemberOfType(CONFIG.INTERNAL_OP_NAMES[name], "operator method")
            return true
        } catch {
            return false
        }
    }
}

class NothingType extends CustomType {
    customId = "gceNothing"

    toString() {
        return "<Nothing>"
    }
    toJSON() {
        return this.toString()
    }
}
const Nothing = new NothingType()

const gceFunction = {
    Type: FunctionType,
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: BlockShape.ARROW,
        forceOutputType: "gceFunction",
        disableMonitor: true,
    },
    Argument: {
        shape: BlockShape.ARROW,
        exemptFromNormalization: true,
        check: ["gceFunction"],
    },
    ArgumentFunctionOrVarName: {
        type: ArgumentType.STRING,
        defaultValue: "myFunction",
        exemptFromNormalization: true,
    },
}
const gceMethod = {
    Type: MethodType,
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: BlockShape.ARROW,
        forceOutputType: "gceMethod",
        disableMonitor: true,
    },
    Argument: {
        shape: BlockShape.ARROW,
        exemptFromNormalization: true,
        check: ["gceMethod"],
    },
}
const gceClass = {
    Type: ClassType,
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: BlockShape.BUMPED,
        forceOutputType: "gceClass",
        disableMonitor: true,
    },
    Argument: {
        shape: BlockShape.BUMPED,
        exemptFromNormalization: true,
        check: ["gceClass"],
    },
    ArgumentClassOrVarName: {
        type: ArgumentType.STRING,
        defaultValue: "MyClass",
        exemptFromNormalization: true,
    },
}
const gceClassInstance = {
    Type: ClassInstanceType,
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: "gceOOP-doublePlus",
        forceOutputType: "gceClassInstance",
        disableMonitor: true,
    },
    Argument: {
        shape: "gceOOP-doublePlus",
        exemptFromNormalization: true,
        check: ["gceClassInstance"],
    },
}
if (!CUSTOM_SHAPE) {
    delete gceClassInstance.Block.blockShape
    delete gceClassInstance.Argument.shape
}
const gceNothing = {
    Type: NothingType,
    Singleton: Nothing,
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: BlockShape.SCRAPPED,
        forceOutputType: "gceNothing",
        disableMonitor: true,
    },
    Argument: {
        shape: BlockShape.SCRAPPED,
        exemptFromNormalization: true,
        check: ["gceNothing"],
    },
}


const commonArguments = {
    classVarName: {
        type: ArgumentType.STRING,
        defaultValue: "MyClass",
    },
    methodName: {
        type: ArgumentType.STRING,
        defaultValue: "myMethod",
    },
    classVariableName: {
        type: ArgumentType.STRING,
        defaultValue: "myVariable",
    },
    attributeName: {
        type: ArgumentType.STRING,
        defaultValue: "myAttr",
    },
    allowAnything: {
        type: ArgumentType.STRING,
        exemptFromNormalization: true,
    },
}
const commonBlocks = {
    returnsAnything: {
        blockType: BlockType.REPORTER,
        allowDropAnywhere: true,
    },
    returnString: {
        blockType: BlockType.REPORTER,
    },
    returnsBoolean: {
        blockType: BlockType.BOOLEAN,
    },
    command: {
        blockType: BlockType.COMMAND
    },
    commandWithBranch: {
        blockType: BlockType.CONDITIONAL,
        branchCount: 1,
    },
}

/************************************************************************************
*                                  Extension Class                                  *
************************************************************************************/

class GCEOOPBlocks {
    /**
     * @returns {object} metadata for this extension and its blocks.
     */
    getInfo() {
        const makeLabel = (text) => ({blockType: BlockType.LABEL, text: text})
        const info = {
            id: "gceOOP",
            name: "OOP",
            color1: "#428af5",
            menuIconURI: "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICB2aWV3Qm94PSIwIDAgMjAgMjAiCiAgdmVyc2lvbj0iMS4xIgogIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPGNpcmNsZQogICAgY3g9IjEwIgogICAgY3k9IjEwIgogICAgcj0iOSIKICAgIHN0eWxlPSJmaWxsOiM0MjhhZjVmZjsgc3Ryb2tlOiMyZDVmYTg7IHN0cm9rZS13aWR0aDoycHg7IGZpbGwtb3BhY2l0eToxOyBzdHJva2Utb3BhY2l0eToxOyBwYWludC1vcmRlcjpzdHJva2UiIC8+CiAgPHBhdGgKICAgIGQ9Im0gMy41LDEwIDQuNSwtNS41IDEuMiwwLjYgLTMuNyw0LjkgMy43LDQuOSAtMS4yLDAuNiB6CiAgICAgICBtIDEzLDAgLTQuNSwtNS41IC0xLjIsMC42IDMuNyw0LjkgLTMuNyw0LjkgMS4yLDAuNiB6IgogICAgc3R5bGU9ImZpbGw6I2ZmZmZmZiIgLz4KPC9zdmc+",
            blocks: [
                makeLabel("Missing Extensions?"),
                { // BUTTON
                    blockType: BlockType.BUTTON,
                    opcode: "addFuncsScopesExtension",
                    text: "Add Functions & Scopes Extension"
                },
                { // BUTTON
                    blockType: BlockType.BUTTON,
                    opcode: "addArrayExtension",
                    text: "Add Array Extension"
                },
                { // BUTTON
                    blockType: BlockType.BUTTON,
                    opcode: "addObjectExtension",
                    text: "Add Object Extension"
                },
                {
                    ...commonBlocks.command,
                    opcode: "logStacks",
                },
                makeLabel("Define Classes"),
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "createClassAt",
                    text: ["create class at var [NAME] [SHADOW]"],
                    tooltip: "Creates a new class, stores it in the chosen variable.",
                    arguments: {
                        NAME: commonArguments.classVarName,
                        SHADOW: {fillIn: "currentClass"},
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "createSubclassAt",
                    text: ["create subclass at var [NAME] with superclass [SUPERCLASS] [SHADOW]"],
                    tooltip: "Creates a subclass with the given superclass, stores it in a variable.",
                    arguments: {
                        NAME: {...commonArguments.classVarName, defaultValue: "MySubclass"},
                        SUPERCLASS: gceClass.ArgumentClassOrVarName,
                        SHADOW: {fillIn: "currentClass"},
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "createClassNamed",
                    text: ["create class named [NAME] [SHADOW]"],
                    tooltip: "Creates and returns a new class with the given name.",
                    branchCount: 1,
                    arguments: {
                        NAME: commonArguments.classVarName,
                        SHADOW: {fillIn: "currentClass"},
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "createSubclassNamed",
                    text: ["create subclass named [NAME] with superclass [SUPERCLASS] [SHADOW]"],
                    tooltip: "Creates and returns a new subclass with the given superclass.",
                    branchCount: 1,
                    arguments: {
                        NAME: {...commonArguments.classVarName, defaultValue: "MySubclass"},
                        SUPERCLASS: gceClass.ArgumentClassOrVarName,
                        SHADOW: {fillIn: "currentClass"},
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "onClass",
                    text: ["on class [CLASS] [SHADOW]"],
                    tooltip: "Runs the enclosed blocks as if they were inside the selected class definition. "+
                      "This allows you to e.g. add methods to already defined classes.",
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        SHADOW: {fillIn: "currentClass"},
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "currentClass",
                    text: "current class",
                    tooltip: "Returns the class currently being defined.",
                    canDragDuplicate: true,
                    hideFromPalette: true,
                },
                "---",
                makeLabel("Use Classes"),
                {
                    ...commonBlocks.returnsBoolean,
                    opcode: "isSubclass",
                    text: "is [SUBCLASS] a subclass of [SUPERCLASS] ?",
                    tooltip: "Checks whether one class inherits from another.",
                    arguments: {
                        SUBCLASS: {...commonArguments.classVarName, defaultValue: "MySubclass"},
                        SUPERCLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "getSuperclass",
                    text: "get superclass of [CLASS]",
                    tooltip: "Returns the superclass of a class, or Nothing if it has none.",
                    arguments: {
                        CLASS: {...gceClass.ArgumentClassOrVarName, defaultValue: "MySubclass"},
                    },
                },
                "---",
                makeLabel("Class Members"),
                "---",
                makeLabel("Define Instance Methods"),
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineInstanceMethod",
                    text: ["define instance method [NAME] [SHADOW]"],
                    tooltip: "Defines an instance method on the current class.",
                    arguments: {
                        NAME: commonArguments.methodName,
                        SHADOW: {fillIn: "self"},
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineSpecialMethod",
                    text: ["define [SPECIAL_METHOD] instance method [SHADOW]"],
                    tooltip: "Defines a special instance method.",
                    arguments: {
                        SPECIAL_METHOD: {type: ArgumentType.STRING, menu: "specialMethod"},
                        SHADOW: {fillIn: "self"},
                    },
                },
                {
                    ...gceClassInstance.Block,
                    opcode: "self",
                    text: "self",
                    tooltip: "Reports the current instance inside a method.",
                    canDragDuplicate: true,
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "callSuperMethod",
                    text: "call super method [NAME] with positional args [POSARGS]",
                    tooltip: "Calls an instance method from the superclass of the current object.",
                    arguments: {
                        NAME: commonArguments.methodName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                {
                    ...gceNothing.Block,
                    opcode: "callSuperInitMethod",
                    text: "call super init method with positional args [POSARGS]",
                    tooltip: "Calls the superclass init method for the current object.",
                    arguments: {
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                "---",
                makeLabel("Define Getters & Setters"),
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineGetter",
                    text: ["define getter [NAME] [SHADOW]"],
                    tooltip: "Defines a getter method for an attribute on the current class.",
                    arguments: {
                        NAME: commonArguments.attributeName,
                        SHADOW: {fillIn: "self"},
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineSetter",
                    text: ["define setter [NAME] [SHADOW1] [SHADOW2]"],
                    tooltip: "Defines a setter method for an attribute on the current class.",
                    arguments: {
                        NAME: commonArguments.attributeName,
                        SHADOW1: {fillIn: "self"},
                        SHADOW2: {fillIn: "defineSetterValue"},
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "defineSetterValue",
                    text: "value",
                    tooltip: "Reports the incoming value inside a setter method.",
                    hideFromPalette: true,
                    canDragDuplicate: true,
                },
                "---",
                makeLabel("Define Operator Methods"),
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineOperatorMethod",
                    text: ["define operator method [OPERATOR_KIND] [SHADOW]"],
                    tooltip: "Defines custom behavior for an operator on instances of the current class.",
                    arguments: {
                        OPERATOR_KIND: {type: ArgumentType.STRING, menu: "operatorMethod"},
                        SHADOW: {fillIn: "operatorOtherValue"},
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "operatorOtherValue",
                    text: "other value",
                    tooltip: "Reports the other operand inside an operator method.",
                    hideFromPalette: true,
                    canDragDuplicate: true,
                },
                "---",
                makeLabel("Define Static Methods & Class Variables"),
                {
                    ...commonBlocks.command,
                    opcode: "setClassVariable",
                    text: "on [CLASS] set class var [NAME] to [VALUE]",
                    tooltip: "Sets a class variable on the selected class.",
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        NAME: commonArguments.classVariableName,
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "getClassVariable",
                    text: "get class var [NAME] of [CLASS]",
                    tooltip: "Gets a class variable from the selected class.",
                    arguments: {
                        NAME: commonArguments.classVariableName,
                        CLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                {
                    ...commonBlocks.command,
                    opcode: "deleteClassVariable",
                    text: "on [CLASS] delete class var [NAME]",
                    tooltip: "Deletes a class variable from the selected class.",
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        NAME: commonArguments.classVariableName,
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineStaticMethod",
                    text: ["define static method [NAME]"],
                    tooltip: "Defines a static method on the current class.",
                    arguments: {
                        NAME: commonArguments.methodName,
                    },
                },
                {
                    ...jwArrayStub.Block,
                    opcode: "propertyNamesOfClass",
                    text: "[PROPERTY] names of class [CLASS]",
                    tooltip: "Returns the names of members of the selected type for a class.",
                    arguments: {
                        PROPERTY: {type: ArgumentType.STRING, menu: "classProperty"},
                        CLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                "---",
                makeLabel("Working with Instances"),
                "---",
                makeLabel("Create & Inspect"),
                {
                    ...gceClassInstance.Block,
                    opcode: "createInstance",
                    text: "create instance of class [CLASS] with positional args [POSARGS]",
                    tooltip: "Creates an instance of a class and passes the given positional arguments to its init method.",
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                {
                    ...commonBlocks.returnsBoolean,
                    opcode: "isInstance",
                    text: "is [INSTANCE] an instance of [CLASS] ?",
                    tooltip: "Checks whether an instance belongs to a class or one of its subclasses.",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                        CLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "getClassOfInstance",
                    text: "get class of [INSTANCE]",
                    tooltip: "Returns the class that created an instance.",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                    },
                },
                "---",
                makeLabel("Attributes"),
                {
                    ...commonBlocks.command,
                    opcode: "setAttribute",
                    text: "on [INSTANCE] set attribute [NAME] to [VALUE]",
                    tooltip: "Sets an attribute on an instance or calls its setter if one exists.",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                        NAME: commonArguments.attributeName,
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "getAttribute",
                    text: "attribute [NAME] of [INSTANCE]",
                    tooltip: "Gets an attribute from an instance or calls its getter if one exists.",
                    arguments: {
                        NAME: commonArguments.attributeName,
                        INSTANCE: gceClassInstance.Argument,
                    },
                },
                {
                    ...dogeiscutObjectStub.Block,
                    opcode: "getAllAttributes",
                    text: "all attributes of [INSTANCE]",
                    tooltip: "Returns all direct instance attributes as an object.",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                    },
                },
                "---",
                makeLabel("Call Methods"),
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "callMethod",
                    text: "on [INSTANCE] call method [NAME] with positional args [POSARGS]",
                    tooltip: "Calls an instance method on an object with positional arguments.",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                        NAME: commonArguments.methodName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "callStaticMethod",
                    text: "on [CLASS] call static method [NAME] with positional args [POSARGS]",
                    tooltip: "Calls a static method on a class with positional arguments.",
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        NAME: commonArguments.methodName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                {
                    ...gceFunction.Block,
                    opcode: "getStaticMethodFunc",
                    text: "get static method [NAME] of [CLASS] as function",
                    tooltip: "Returns a static method from a class as a callable function value.",
                    arguments: {
                        NAME: commonArguments.methodName,
                        CLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
            ],
            menus: {
                classProperty: {
                    acceptReporters: true,
                    items: MENU_ITEMS.CLASS_PROPERTY,
                },
                operatorMethod: {
                    acceptReporters: false,
                    items: MENU_ITEMS.OPERATOR_METHOD,
                },
                specialMethod: {
                    acceptReporters: false,
                    items: MENU_ITEMS.SPECIAL_METHOD,
                },
                typeofMenu: {
                    acceptReporters: true,
                    items: MENU_ITEMS.TYPEOF_MENU,
                },
            },
        }
        return info
    }

    /**
     * @param {boolean} includeOOPBlocks
     * @param {boolean} includeFuncScopesBlocks
     * @returns {object} compilation information and implementation for some blocks of the selected extensions
     */
    getCompileInfo(includeOOPBlocks = true, includeFuncScopesBlocks = true) {
        const createIRGenerator = (kind, inputs, fields, yieldRequired = false) => ((generator, block) => {
            if (yieldRequired) generator.script.yields = true
            const result = { kind }

            inputs.forEach(inputName => {
                result[inputName] = inputName === "SUBSTACK"
                    ? generator.descendSubstack(block, inputName)
                    : generator.descendInputOfBlock(block, inputName)
            })

            fields.forEach(fieldName => {
                result[fieldName] = block.fields[fieldName].value
            })
            return result
        })

        const EXTENSION_PREFIX = "runtime.ext_gceOOP"
        const ENV_PREFIX = `${EXTENSION_PREFIX}.environment`
        const THREAD_UTIL_PREFIX = `${EXTENSION_PREFIX}.ThreadUtil`
        const CURRENT_STACK = `${THREAD_UTIL_PREFIX}.getCurrentStack(thread)`
        const STACK_MANAGER = `${THREAD_UTIL_PREFIX}.getStackManager(thread)`
        const CAST_PREFIX = `${EXTENSION_PREFIX}.Cast`

        const createClassCore = (node, compiler, setVariable, superClsCode = null) => {
            const nameCode = compiler.descendInput(node.NAME).asString()
            const clsLocal = compiler.localVariables.next()
            const superClass = superClsCode ? `${CAST_PREFIX}.toClass(${superClsCode}, thread)`: `${ENV_PREFIX}.commonSuperClass`

            return {
                setup: `const ${clsLocal} = new ${ENV_PREFIX}.ClassType(${nameCode}, ${superClass});` +
                    (setVariable ? `${CURRENT_STACK}.setScopeVar(${clsLocal}.name, ${clsLocal});` : "") +
                    `${CURRENT_STACK}.enterClassDefScope(${clsLocal});`,
                cleanup: `${CURRENT_STACK}.exitClassDefScope();`,
                clsLocal
            }
        }

        const createWrappedGenerator = (setupCode, stackCode, cleanup, returnVar = null) => {
            return `(yield* (function*() {${setupCode}${stackCode}${cleanup}${returnVar ? `return ${returnVar};` : ""}})())`
        }

        const createMethodDefinition = (
            node, compiler, imports,
            nameCode, classId, memberType,
            disableFuncConfig,
        ) => {
            const nameLocal = compiler.localVariables.next()

            compiler.source += `const ${nameLocal} = ${nameCode};` +
                `${CURRENT_STACK}.getClsOrThrow("define method").setMember(${nameLocal}, ${quote(memberType)}, `+
                `new ${ENV_PREFIX}.${classId}(${nameLocal}, function* (thread) {`
            addSubstackCode(compiler, node.SUBSTACK, imports)
            compiler.source += `${STACK_MANAGER}.prepareReturn();` +
                // Nothing is indepedent of function context, so we can exit context before
                `return ${ENV_PREFIX}.Nothing;` +
                `}, ${CURRENT_STACK}, ` +
                `${CURRENT_STACK}.` + (disableFuncConfig ? "constructor.getDefaultFuncConfig()" : "getAndResetNextFuncConfig()") + "));\n"
        }

        const createCallCode = (castMethod, castArgs, m, ...args) => {
            return `(yield* ${CAST_PREFIX}.${castMethod}(${castArgs.join(", ")}).${m}(thread, ${args.join(", ")}))`
        }

        const addSubstackCode = (compiler, substack, imports) => {
            compiler.descendStack(substack, new imports.Frame(false, undefined, true))
        }

        const getSubstackCode = (compiler, substack, imports) => {
            const oldSource = compiler.source
            compiler.source = ""
            addSubstackCode(compiler, substack, imports)
            const substackCode = compiler.source
            compiler.source = oldSource
            return substackCode
        }

        let irInfo = {}
        let jsInfo = {}

        if (includeOOPBlocks) {
            Object.assign(irInfo, {
                // Define Classes
                createClassAt: createIRGenerator("stack", ["NAME", "SUBSTACK"], [], true),
                createSubclassAt: createIRGenerator("stack", ["NAME", "SUPERCLASS", "SUBSTACK"], [], true),
                createClassNamed: createIRGenerator("input", ["NAME", "SUBSTACK"], [], true),
                createSubclassNamed: createIRGenerator("input", ["NAME", "SUPERCLASS", "SUBSTACK"], [], true),

                // Define Instance Methods
                defineInstanceMethod: createIRGenerator("stack", ["NAME", "SUBSTACK"], []),
                defineSpecialMethod: createIRGenerator("stack", ["SUBSTACK"], ["SPECIAL_METHOD"]),
                callSuperMethod: createIRGenerator("input", ["NAME", "POSARGS"], [], true),
                callSuperInitMethod: createIRGenerator("input", ["POSARGS"], [], true),

                // Define Getters & Setters
                defineGetter: createIRGenerator("stack", ["NAME", "SUBSTACK"], []),
                defineSetter: createIRGenerator("stack", ["NAME", "SUBSTACK"], []),

                // Define Operator Methods
                defineOperatorMethod: createIRGenerator("stack", ["SUBSTACK"], ["OPERATOR_KIND"]),

                // Define Static Methods & Class Variables
                defineStaticMethod: createIRGenerator("stack", ["NAME", "SUBSTACK"], []),


                // Create & Inspect
                createInstance: createIRGenerator("input", ["CLASS", "POSARGS"], [], true),

                // Attributes
                setAttribute: createIRGenerator("stack", ["INSTANCE", "NAME", "VALUE"], [], true),
                getAttribute: createIRGenerator("input", ["INSTANCE", "NAME"], [], true),

                // Call Methods
                callMethod: createIRGenerator("input", ["INSTANCE", "NAME", "POSARGS"], [], true),
                callStaticMethod: createIRGenerator("input", ["CLASS", "NAME", "POSARGS"], [], true),
            })
            Object.assign(jsInfo, {
                // Define Classes
                createClassAt: (node, compiler, imports) => {
                    const { setup, cleanup } = createClassCore(node, compiler, true)
                    compiler.source += setup
                    addSubstackCode(compiler, node.SUBSTACK, imports)
                    compiler.source += cleanup + "\n"
                },
                createSubclassAt: (node, compiler, imports) => {
                    const superClsCode = compiler.descendInput(node.SUPERCLASS).asUnknown()
                    const { setup, cleanup } = createClassCore(node, compiler, true, superClsCode)
                    compiler.source += setup
                    addSubstackCode(compiler, node.SUBSTACK, imports)
                    compiler.source += cleanup + "\n"
                },
                createClassNamed: (node, compiler, imports) => {
                    const { setup, cleanup, clsLocal } = createClassCore(node, compiler, false)
                    const substackCode = getSubstackCode(compiler, node.SUBSTACK, imports)
                    const generatedCode = createWrappedGenerator(setup, substackCode, cleanup, clsLocal)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
                createSubclassNamed: (node, compiler, imports) => {
                    const superClsCode = compiler.descendInput(node.SUPERCLASS).asUnknown()
                    const { setup, cleanup, clsLocal } = createClassCore(node, compiler, false, superClsCode)
                    const substackCode = getSubstackCode(compiler, node.SUBSTACK, imports)
                    const generatedCode = createWrappedGenerator(setup, substackCode, cleanup, clsLocal)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Define Instance Methods
                defineInstanceMethod: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    createMethodDefinition(node, compiler, imports, nameCode, "MethodType", "instance method", false)
                },
                defineSpecialMethod: (node, compiler, imports) => {
                    const nameCode = `${CAST_PREFIX}.toMenuSpecialMethod(${quote(node.SPECIAL_METHOD)})`
                    createMethodDefinition(node, compiler, imports, nameCode, "MethodType", "instance method", false)
                },
                callSuperMethod: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = `(yield* ${CURRENT_STACK}.getSelfOrThrow().executeSuperMethod(thread, ${nameCode}, ${posArgsCode}))`
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
                callSuperInitMethod: (node, compiler, imports) => {
                    const nameCode = quote(CONFIG.INIT_METHOD_NAME)
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = `(yield* ${CURRENT_STACK}.getSelfOrThrow().executeSuperInitMethod(thread, ${nameCode}, ${posArgsCode}))`
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Define Getters & Setters
                defineGetter: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    createMethodDefinition(node, compiler, imports, nameCode, "GetterMethodType", "getter method", true)
                },
                defineSetter: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    createMethodDefinition(node, compiler, imports, nameCode, "SetterMethodType", "setter method", true)
                },

                // Define Operator Methods
                defineOperatorMethod: (node, compiler, imports) => {
                    const nameCode = `${CAST_PREFIX}.toMenuOperatorMethod(${quote(node.OPERATOR_KIND)})`
                    createMethodDefinition(node, compiler, imports, quote(node.OPERATOR_KIND), "OperatorMethodType", "operator method", true)
                },

                // Define Static Methods & Class Variables
                defineStaticMethod: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    createMethodDefinition(node, compiler, imports, nameCode, "FunctionType", "static method", false)
                },


                // Create & Inspect
                createInstance: (node, compiler, imports) => {
                    const classCode = compiler.descendInput(node.CLASS).asUnknown()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = createCallCode("toClass", [classCode, "thread"], "createInstance", posArgsCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Attributes
                setAttribute: (node, compiler, imports) => {
                    const instanceCode = compiler.descendInput(node.INSTANCE).asUnknown()
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const valueCode = compiler.descendInput(node.VALUE).asUnknown()
                    compiler.source += createCallCode("toClassInstance", [instanceCode, "thread"], "setAttribute", nameCode, valueCode) + ";\n"
                },
                getAttribute: (node, compiler, imports) => {
                    const instanceCode = compiler.descendInput(node.INSTANCE).asUnknown()
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const generatedCode = createCallCode("toClassInstance", [instanceCode, "thread"], "getAttribute", nameCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Call Methods
                callMethod: (node, compiler, imports) => {
                    const instanceCode = compiler.descendInput(node.INSTANCE).asUnknown()
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = createCallCode("toClassInstance", [instanceCode, "thread"], "executeInstanceMethod", nameCode, posArgsCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
                callStaticMethod: (node, compiler, imports) => {
                    const classCode = compiler.descendInput(node.CLASS).asUnknown()
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = createCallCode("toClass", [classCode, "thread"], "executeStaticMethod", nameCode, posArgsCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
            })
        }
        
        if (includeFuncScopesBlocks) {
            Object.assign(irInfo, {
                // Define
                createFunctionAt: createIRGenerator("stack", ["NAME", "SUBSTACK"], []),
                createFunctionNamed: createIRGenerator("input", ["NAME", "SUBSTACK"], []),

                // Inside Functions & Methods
                returnValue: createIRGenerator("stack", ["VALUE"], []),

                // Use Functions
                callFunction: createIRGenerator("input", ["FUNC", "POSARGS"], [], true),


                // Utilities
                objectAsString: createIRGenerator("input", ["VALUE"], [], true),
            })
            Object.assign(jsInfo, {
                // Define
                createFunctionAt: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const nameLocal = compiler.localVariables.next()

                    compiler.source += `const ${nameLocal} = ${nameCode};` +
                        `${CURRENT_STACK}.setScopeVar(${nameLocal}, new ${ENV_PREFIX}.FunctionType(${nameLocal}, function* (thread) {`
                    addSubstackCode(compiler, node.SUBSTACK, imports)
                    compiler.source += `${STACK_MANAGER}.prepareReturn();` +
                        // Nothing is indepedent of function context, so we can exit context before
                        `return ${ENV_PREFIX}.Nothing;` +
                        `}, ${CURRENT_STACK},`+
                        `${CURRENT_STACK}.getAndResetNextFuncConfig()));\n`
                },
                createFunctionNamed: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const generatedCode = `(new ${ENV_PREFIX}.FunctionType(${nameCode}, function* (thread) {`+
                        getSubstackCode(compiler, node.SUBSTACK, imports)+
                        `${STACK_MANAGER}.prepareReturn();` +
                        // Nothing is indepedent of function context, so we can exit context before
                        `return ${ENV_PREFIX}.Nothing;` +
                        `}, ${CURRENT_STACK},` +
                        `${CURRENT_STACK}.getAndResetNextFuncConfig()))`
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Inside Functions & Methods
                returnValue: (node, compiler, imports) => {
                    const returnValueLocal = compiler.localVariables.next()
                    // We need to cache the return value before exiting context, as it might depend on it
                    compiler.source += `const ${returnValueLocal} = ${compiler.descendInput(node.VALUE).asUnknown()};` +
                        `${STACK_MANAGER}.prepareReturn();` +
                        `return ${returnValueLocal};\n`
                },

                // Use Functions
                callFunction: (node, compiler, imports) => {
                    const funcCode = compiler.descendInput(node.FUNC).asUnknown()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = createCallCode("toFunction", [funcCode, "thread"], "execute", posArgsCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },


                // Utilities
                objectAsString: (node, compiler, imports) => {
                    const objectCode = compiler.descendInput(node.VALUE).asUnknown()
                    const generatedCode = `(yield* ${EXTENSION_PREFIX}._objectAsString(${objectCode}, thread))`
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
            })
        }

        return {ir: irInfo, js: jsInfo}
    }

    constructor() {
        // to allow other extensions access from the extension class
        if (isRuntimeEnv) {
            Object.assign(Scratch.vm, {gceFunction, gceMethod, gceClass, gceClassInstance, gceNothing})
        }
        this.Cast = Cast
        this.ThreadUtil = ThreadUtil
        // to allow other extensions access to all internal classes
        this.environment = {
            doublePlusShape: CUSTOM_SHAPE, applyInternalWrappers,
            quote, escapeHTML, span, throwInternal, assertType,
            VariableManager, ThreadUtil, ScopeStackManager, ScopeStack, CONFIG,
            TypeChecker, Cast, CustomType, BaseCallableType, FunctionType,
            MethodType, GetterMethodType, SetterMethodType, OperatorMethodType,
            ClassType, commonSuperClass: null, ClassInstanceType, NothingType, Nothing,
            gceFunction, gceMethod, gceClass, gceClassInstance, gceNothing,
        }
        
        if (isRuntimeEnv) {
            runtime.registerSerializer(
                "gceNothing",
                v => (v instanceof NothingType ? v.toJSON() : null),
                v => Nothing,
            )
            Scratch.gui.getBlockly().then(ScratchBlocks => {
                ScratchBlocks.BlockSvg.registerCustomShape("gceOOP-doublePlus", CUSTOM_SHAPE)
            })
            
            applyInternalWrappers(Scratch)
        }

        this.globalVariables = new VariableManager()
    }

    setup() {
        if (!isRuntimeEnv) return
        
        this.addFuncsScopesExtension()
        this.addArrayExtension()
        this.addObjectExtension()

        const commonSuperClass = new ClassType("Superclass", null)
        commonSuperClass.instanceMethods[CONFIG.INIT_METHOD_NAME] = new MethodType(
            CONFIG.INIT_METHOD_NAME,
            function* (thread) {
                ThreadUtil.getStackManager(thread).prepareReturn()
                // Nothing is indepedent of function context, so we can exit context before
                return Nothing
            },
            new ScopeStack(),
            ScopeStack.getDefaultFuncConfig(),
        )
        this.environment.commonSuperClass = commonSuperClass
    }

    /************************************************************************************
    *                                       Blocks                                      *
    ************************************************************************************/

    addFuncsScopesExtension() {
        if (isRuntimeEnv &&!Scratch.vm.extensionManager.isExtensionLoaded("gceFuncsScopes")) {
            Scratch.vm.extensionManager.loadExtensionURL(
                "http://localhost:5173/extensions/gceFuncsScopes.js",
            )
        }
    }
    
    addArrayExtension() {
        if (isRuntimeEnv &&!Scratch.vm.extensionManager.isExtensionLoaded("jwArray")) {
            Scratch.vm.extensionManager.loadExtensionIdSync("jwArray")
        }
    }

    addObjectExtension() {
        if (isRuntimeEnv &&!Scratch.vm.extensionManager.isExtensionLoaded("dogeiscutObject")) {
            Scratch.vm.extensionManager.loadExtensionURL(
                "https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutObject.js"
            )
        }
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    logStacks(args, util) {
        console.log("Current thread stacks:", JSON.stringify([...ThreadUtil.getStackManager(util.thread).stacks], null, 2))
    }

    /******************** Scoped Variables ********************/

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    setScopeVar(args, util) {
        const name = Cast.toString(args.NAME)
        ThreadUtil.getCurrentStack(util.thread).setScopeVar(name, args.VALUE)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    getScopeVar(args, util) {
        const name = Cast.toString(args.NAME)
        return ThreadUtil.getCurrentStack(util.thread).getScopeVar(name)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    scopeVarExists(args, util) {
        const name = Cast.toString(args.NAME)
        const currentStack = ThreadUtil.getCurrentStack(util.thread)
        let hasVar
        switch (args.KIND) {
            case "all scopes":
                hasVar = currentStack.hasScopeVar(name, false, false)
                break
            case "local scope":
                hasVar = currentStack.hasScopeVar(name, true, false)
                break
            case "global scope":
                hasVar = currentStack.hasScopeVar(name, false, true)
                break
        }
        return Cast.toBoolean(hasVar)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    deleteScopeVar(args, util) {
        const name = Cast.toString(args.NAME)
        ThreadUtil.getCurrentStack(util.thread).deleteScopeVar(name)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    allVariables(args, util) {
        const currentStack = ThreadUtil.getCurrentStack(util.thread)
        let varNames
        switch (args.KIND) {
            case "all scopes":
                varNames = currentStack.getScopeVarNames(false, false)
                break
            case "local scope":
                varNames = currentStack.getScopeVarNames(true, false)
                break
            case "global scope":
                varNames = currentStack.getScopeVarNames(false, true)
                break
        }
        return Cast.toArray(varNames)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    createVarScope(args, util) {
        ThreadUtil.getCurrentStack(util.thread).enterUserScope()
        util.startBranch(1, false, () => {
            ThreadUtil.getCurrentStack(util.thread).exitUserScope()
        })
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    bindVarToScope(args, util) {
        const name = Cast.toString(args.NAME)
        switch (args.KIND) {
            case "non-local":
                ThreadUtil.getCurrentStack(util.thread).bindScopeVarNonlocal(name)
                break
            case "global":
                ThreadUtil.getCurrentStack(util.thread).bindScopeVarGlobal(name)
                break
        }
    }

    /******************** Classes ********************/

    // Define Classes
    createClassAt = this._isACompiledBlock
    createSubclassAt = this._isACompiledBlock
    createClassNamed = this._isACompiledBlock
    createSubclassNamed = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    onClass(args, util) {
        const cls = Cast.toClass(args.CLASS, util.thread)
        ThreadUtil.getCurrentStack(util.thread).enterClassDefScope(cls)
        util.startBranch(1, false, () => {
            ThreadUtil.getCurrentStack(util.thread).exitClassDefScope()
        })
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    currentClass(args, util) {
        return ThreadUtil.getCurrentStack(util.thread).getClsOrThrow("current class")
    }

    // Use Classes

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    isSubclass(args, util) {
        const subCls = Cast.toClass(args.SUBCLASS, util.thread)
        const superCls = Cast.toClass(args.SUPERCLASS, util.thread)
        return Cast.toBoolean(subCls.isSubclassOf(superCls))
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    getSuperclass(args, util) {
        const cls = Cast.toClass(args.CLASS, util.thread)
        if (cls.superCls) {
            return assertType("calm-hare", ClassType, cls.superCls)
        } else {
            return Nothing
        }
    }

    /******************** Class Members ********************/

    // Define Instance Methods
    defineInstanceMethod = this._isACompiledBlock
    defineSpecialMethod = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    self(args, util) {
        const value =  ThreadUtil.getCurrentStack(util.thread).getSelfOrThrow()
        return assertType("mirthful-dolphin", ClassInstanceType, value)
    }
    callSuperMethod = this._isACompiledBlock
    callSuperInitMethod = this._isACompiledBlock

    // Define Getters & Setters
    defineGetter = this._isACompiledBlock
    defineSetter = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    defineSetterValue(args, util) {
        return ThreadUtil.getCurrentStack(util.thread).getSetterValueOrThrow()
    }

    // Define Operator Methods
    defineOperatorMethod = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    operatorOtherValue(args, util) {
        return ThreadUtil.getCurrentStack(util.thread).getOtherValueOrThrow()
    }

    // Define Static Methods & Class Variables

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    setClassVariable(args, util) {
        const cls = Cast.toClass(args.CLASS, util.thread)
        const name = Cast.toString(args.NAME)
        const value = args.VALUE
        cls.setMember(name, value, "class variable")
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    getClassVariable(args, util) {
        const cls = Cast.toClass(args.CLASS, util.thread)
        const name = Cast.toString(args.NAME)
        const value = cls.getMemberOfType(name, "class variable")
        return value
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    deleteClassVariable(args, util) {
        const cls = Cast.toClass(args.CLASS, util.thread)
        const name = Cast.toString(args.NAME)
        cls.deleteMemberOfType(name, "class variable")
    }
    defineStaticMethod = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    propertyNamesOfClass(args, util) {
        const property = Cast.toMenuClassProperty(args.PROPERTY)
        const cls = Cast.toClass(args.CLASS, util.thread)
        const [instanceMethods, staticMethods, getterMethods, setterMethods, operatorMethods, classVariables] = cls.getAllMembers()
        let values = []
        switch (property) {
            case "instance method":
                values = instanceMethods; break
            case "static method":
                values = staticMethods; break
            case "getter method":
                values = getterMethods; break
            case "setter method":
                values = setterMethods; break
            case "operator method":
                values = operatorMethods; break
            case "class variable":
                values = classVariables; break
        }
        let names = Object.keys(values)
        if (property == "instance method") {
            let index
            index = names.indexOf(CONFIG.INIT_METHOD_NAME)
            if (index !== -1) names[index] = "[special] init"
            index = names.indexOf(CONFIG.AS_STRING_METHOD_NAME)
            if (index !== -1) names[index] = "[special] as string"
        }
        else if (property === "operator method") {
            names = names.map(name => CONFIG.PUBLIC_OP_NAMES[name])
        }
        return Cast.toArray(names)
    }

    /******************** Working with Instances ********************/

    // Create & Inspect
    createInstance = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    isInstance(args, util) {
        const instance = Cast.toClassInstance(args.INSTANCE, util.thread)
        const cls = Cast.toClass(args.CLASS, util.thread)
        return Cast.toBoolean(instance.cls.isSubclassOf(cls))
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    getClassOfInstance(args, util) {
        const instance = Cast.toClassInstance(args.INSTANCE, util.thread)
        const value = instance.cls
        return assertType("calm-weasel", ClassType, value)
    }

    // Attributes
    setAttribute = this._isACompiledBlock
    getAttribute = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    getAllAttributes(args, util) {
        const instance = Cast.toClassInstance(args.INSTANCE, util.thread)
        return Cast.toObject(instance.attributes)
    }

    // Call Methods
    callMethod = this._isACompiledBlock
    callStaticMethod = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    getStaticMethodFunc(args, util) {
        const cls = Cast.toClass(args.CLASS, util.thread)
        const name = Cast.toString(args.NAME)
        const value = cls.getStaticMethod(name)
        return assertType("nimble-heron", FunctionType, value)
    }

    /******************** Functions ********************/

    // Configure Before Define

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    configureNextFunctionArgs(args, util) {
        const argNames = Cast.toArray(args.ARGNAMES).array.map(name => Cast.toString(name))
        const argDefaults = Cast.toArray(args.ARGDEFAULTS).array
        ThreadUtil.getCurrentStack(util.thread).setNextFuncConfig({argNames, argDefaults})
    }

    // Define
    createFunctionAt = this._isACompiledBlock
    createFunctionNamed = this._isACompiledBlock

    // Inside Functions & Methods
    returnValue = this._isACompiledBlock

    // Use Functions
    callFunction = this._isACompiledBlock

    /******************** Utilities ********************/
    objectAsString = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    typeofValue(args, util) {
        return TypeChecker.stringTypeof(args.VALUE)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    typeofValueIsMenu(args, util) {
        return (TypeChecker.stringTypeof(args.VALUE) === Cast.toMenuTypeofType(args.TYPE))
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    checkIdentity(args, util) {
        return Object.is(args.VALUE1, args.VALUE2)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    nothing(args, util) {
        return Nothing
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    executeExpression(args, util) {
        // do nothing
    }

    /************************************************************************************
    *                        Implementation (Helpers) for Blocks                        *
    ************************************************************************************/

    /**
     * @param {*} object
     * @param {Thread} thread
     * @returns {string} the return value of the as string method
     */
    *_objectAsString(object, thread) {
        if (!(object instanceof ClassInstanceType)) return object.toString()
        let method
        try {
            /** @type {MethodType} */
            method = object.cls.getMemberOfType(CONFIG.AS_STRING_METHOD_NAME, "instance method")
        } catch {}
        if (!method) return object.toString()
        const output = yield* method.execute(thread, object, [])
        if (typeof output !== "string") throw new Error(`As String methods must always return a string.`)
        return output
    }

    // Copied from PenguinMod-Vm/src/compiler/jexecute.js
    _mod(n, modulus) {
        let result = n % modulus;
        if (result / modulus < 0) result += modulus;
        return result;
    }

    /**
     * @param {Thread} thread
     * @param {*} left
     * @param {*} right
     * @param {string} leftMethod
     * @param {string} rightMethod
     * @param {string} nodeKind
     * @returns {*}
     */
    *_binaryOperator(thread, left, right, leftMethod, rightMethod, nodeKind) {
        if ((left instanceof ClassInstanceType) && left.hasOperatorMethod(leftMethod)) {
            return yield* left.executeOperatorMethod(thread, leftMethod, right)
        } else if ((right instanceof ClassInstanceType) && right.hasOperatorMethod(rightMethod)) {
            return yield* right.executeOperatorMethod(thread, rightMethod, left)
        }
        // default implementation
        left = Cast.toNumber(left)
        right = Cast.toNumber(right)
        switch (nodeKind) {
            case "op.add": return left + right
            case "op.subtract": return left - right
            case "op.multiply": return left * right
            case "op.divide": return left / right
            case "op.mod":
                return this._mod(left, right)
            case "op.power": return Math.pow(left, right)
        }
        return null
    }

    /**
     * @param {Thread} thread
     * @param {*} left
     * @param {*} right
     * @param {string} method
     * @param {string} oppositeMethod
     * @param {string} nodeKind
     * @returns {boolean|null}
     */
    *_comparisonOperator(thread, left, right, method, oppositeMethod, nodeKind) {
        let foundMethod = false
        let output = undefined
        if ((left instanceof ClassInstanceType) && left.hasOperatorMethod(method)) {
            foundMethod = true
            output = yield* left.executeOperatorMethod(thread, method, right)
        } else if ((right instanceof ClassInstanceType) && right.hasOperatorMethod(oppositeMethod)) {
            foundMethod = true
            output = yield* right.executeOperatorMethod(thread, oppositeMethod, left)
        }
        if (foundMethod) {
            if (typeof output !== "boolean") throw new Error(`Comparison Operator methods must always return a boolean.`)
            return output
        }
        // default implementation(see scratch3_operators.js)
        const compareResult = Cast.compare(left, right)
        switch (nodeKind) {
            case "op.equals": return compareResult === 0
            case "op.notequal": return compareResult !== 0
            case "op.greater": return compareResult > 0
            case "op.gtorequal": return compareResult >= 0
            case "op.less": return compareResult < 0
            case "op.ltorequal": return compareResult <= 0
        }
        return null
    }

    /************************************************************************************
    *                                      Helpers                                      *
    ************************************************************************************/

    _isACompiledBlock() {
        throwInternal("spry-hare")
    }
}

const extensionClassInstance = new GCEOOPBlocks()
extensionClassInstance.setup()
Scratch.extensions.register(extensionClassInstance)
if (isRuntimeEnv) {
    runtime.registerCompiledExtensionBlocks("gceOOP", extensionClassInstance.getCompileInfo(true, false))
    runtime.registerCompiledExtensionBlocks("gceFuncsScopes", extensionClassInstance.getCompileInfo(false, true))
}
if (!isRuntimeEnv) {
    console.log("Imported OOP extension in non-runtime environment")
}
})(Scratch)

/************************************************************************************
*                                 Type Definitions                                  *
************************************************************************************/

/**
 * A thread is a running stack context and all the metadata needed.
 * @typedef {Object} Thread
 * @property {ScopeStackManager} [gceSSM]
 */

/**
 * @typedef {Object} ExtensionManager
 * @property {function(string): boolean} isExtensionLoaded
 * @property {function(string): void} loadExtensionIdSync
 * @property {function(string): void} loadExtensionURL
 */

/**
 * @typedef {Object} jwStyleExtensionType
 * @property {Object} Type
 */

/**
 * @typedef {Object} VirtualMachine
 * @property {Object} exports
 * @property {Runtime} runtime
 * @property {ExtensionManager} extensionManager
 * 
 * @property {jwStyleExtensionType} dogeiscutObject - Object Type from extension
 * @property {jwStyleExtensionType} dogeiscutSet - Set Type from extension
 * @property {jwStyleExtensionType} jwArray - Array Type from extension
 * @property {jwStyleExtensionType} jwColor - Color Type from extension
 * @property {jwStyleExtensionType} jwDate - One possible Date Type from extension
 * @property {jwStyleExtensionType} jwLambda - Lambda Type from extension
 * @property {jwStyleExtensionType} jwNum - UnlimitedNum Type from extension
 * @property {jwStyleExtensionType} jwTargets - Target Type (not internal one) from extension
 * @property {jwStyleExtensionType} jwXML - XML Type from extension
 */

/**
 * @typedef {Object} Runtime
 * @property {function(object, object): object} _convertBlockForScratchBlocks
 * @property {function(string, object): void} registerCompiledExtensionBlocks
 * @property {function(string, Function, Function): void} registerSerializer
 * 
 * @property {Object} ext_ddeDateFormat
 * @property {Object} ext_ddeDateFormatV2
 * @property {GCEOOPBlocks} ext_gceOOP
 * @property {GCEFuncsScopesBlocks} [ext_gceFuncsScopes]
 */

/**
 * @typedef {Object} ScratchExtensions
 * @property {boolean} unsandboxed
 * @property {Function} register
 * @property {boolean} isPenguinMod
 * @property {boolean} [isTestingEnv]
 */

/**
 * @typedef {Object} ScratchCast
 * @property {function(*): number} toNumber
 * @property {function(*): boolean} toBoolean
 * @property {function(*): string} toString - Hint to avoid confusion: Cast.toString converts a Scratch value to a string, it does NOT stringify a Cast instance.
 * @property {function(*): Array.<number>} toRgbColorList
 * @property {function(*): {r: number, g: number, b: number, a: number}} toRgbColorObject
 * @property {function(*, number, boolean): (number|string)} toListIndex
 * @property {function(*, *): number} compare
 */

/**
 * @typedef {Object} ScratchObject
 * @property {Object<string, string>} ArgumentType
 * @property {Object<string, ?string>} ArgumentAlignment
 * @property {Object<string, string>} BlockType
 * @property {Object<string, number>} BlockShape
 * @property {Object<string, string>} NotchShape
 * @property {Object<string, string>} TargetType
 * @property {ScratchExtensions} extensions
 * @property {Function} translate
 * @property {VirtualMachine} vm
 * @property {ScratchCast} Cast
 * @property {Object} Clone
 * @property {Object} Color
 */

/**
 * @typedef {Object} ContextScope
 * @property {string} type
 * @property {boolean} [isGlobalScope]
 * @property {boolean} [isUserScope]
 * @property {boolean} [isCallable]
 * @property {boolean} [supportsVars]
 * @property {boolean} [supportsSelf]
 * @property {boolean} [supportsSetterValue]
 * @property {boolean} [supportsOtherValue]
 * @property {boolean} [supportsCls]
 * @property {VariableManager} [vars]
 * @property {ClassInstanceType} [self]
 * @property {*} [setterValue]
 * @property {*} [other]
 * @property {ClassType} [cls]
 */

/**
 * @typedef {Object} FunctionArgConfig
 * @property {Array<string>} argNames
 * @property {PositionalFunctionArgs} argDefaults
 */

/**
 * @typedef {Array<*>} PositionalFunctionArgs
 */

/**
 * @typedef {Object<string, *>} BlockArgs
 */

/**
 * @typedef {Object} BlockUtil
 * @property {Thread} thread
 * @property {function(number, boolean, function(): void): void} startBranch
 */


/**
 * TODO
 *
 * + HIGH PRIORITY
 * + - finish project tests
 * + - consider different architecture for storing block implementations
 * + - consider splitting "OOP" extension again
 *
 * + MID PRIORITY
 * + - maybe reorganize block cagegories
 * + - option to exclude super classes when asking for members
 * + - implement right-click switch options for similar blocks
 * + - name of class/function block
 * + - add "all current variable names" or similar block to function definitions
 * + - possibly make "self", "other" and "value" available as a variable in methods
 * + - "delete member of class" block
 * + - reconsider to standardize stacks and scopes index order style
 * + - convert call super init method to call super special method
 *
 * + LOW PRIORITY (optional in future)
 * + - button on blocks that opens a section in the documentation about that block
 * + - implement translations
 * + - change font of blocks and inputs?
 * + - define toReporterContent e.g. on ClassInstanceType for better visualization
 * + - investigate why inputs are not supported in shadow blocks
 * + - make as string work for arrays, objects too
 * + - "all variables that are classes/functions" block
 * 
 * + QUICK TASKS
 *
 * + DURING TESTING (do not forget):
 * + - test and/or rework enterClassDefScope
 * + - add project tests for TypeChecker, Cast
 * + - specially test special cases of propertyNamesOfClass
 * + - ensure scopeVarExists is tested properly, especially with multiple scopes
 * + - ensure allVariables is tested properly, especially with multiple scopes
 * + - ensure bindVarToScope is tested properly
 * + - ensure getSuperclass is tested properly
 * + - ensure propertyNamesOfClass edge cases are tested
 * + - test that createVarScope and onClass branch callbacks execute even on error
 *
 * + ON RELEASE / AFTER TESTING:
 * + - remove temporary logStacks block
 * + - change both localhost URLs to extensions.penguinmod URL
 *
 * + DOC NOTES TO REMEMBER
 */
