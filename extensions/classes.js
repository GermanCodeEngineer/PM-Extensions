// Name: Classes
// ID: gceClassesOOP
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

(function(Scratch) {
"use strict"

if (!Scratch.extensions.unsandboxed) {
    throw new Error("Classes Extension must run unsandboxed.")
}

/************************************************************************************
*                                Custom Block Shapes                                *
************************************************************************************/

let CUSTOM_SHAPE
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
    console.error("[Classes Extension] Failed to create custom shape", error)
}


/************************************************************************************
*                             Wrapping Some PM Internals                            *
************************************************************************************/

function applyHacks(Scratch) {
    const {IRGenerator, JSGenerator} = Scratch.vm.exports
    const {TypedInput, TYPE_UNKNOWN, TYPE_BOOLEAN} = JSGenerator.exports
    const ScriptTreeGenerator = IRGenerator.exports.ScriptTreeGenerator
    
    // wrap Scratch.Cast.toBoolean to return false for Nothing
    const oldToBoolean = Scratch.Cast.toBoolean
    Scratch.Cast.toBoolean = function modifiedToBoolean(value) {
        if (value instanceof NothingType) return false
        return oldToBoolean(value)
    }
    
    // Wrap ScriptTreeGenerator.descendInput to make 
    // notequals, ltorequal and gtorequal compiled blocks (as the other comparison blocks are)
    const oldDescendTreeGenInput = ScriptTreeGenerator.prototype.descendInput
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

    // Wrap JSGenerator.descendInput for some operator blocks to allow classes to define custom handling
    const oldDescendJSGenInput = JSGenerator.prototype.descendInput
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

                return new TypedInput(`(yield* runtime.ext_gceClassesOOP._binaryOperator(thread, ${left}, ${right}, `+
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
                return new TypedInput(`(yield* runtime.ext_gceClassesOOP._comparisonOperator(thread, ${left.asUnknown()}, ${right.asUnknown()}, `+
                    `${quote(leftMethod)}, ${quote(rightMethod)}, ${quote(node.kind)}))`, TYPE_BOOLEAN)
        }
        return oldDescendJSGenInput.call(this, node, visualReport)
    }
    
}

/************************************************************************************
*                            Internal Types and Constants                           *
************************************************************************************/

function quote(s) {
    if (typeof s !== "string") s = s.toString()
    s = s.replace(/\\/g, "\\\\").replace(/'/g, "\\'")
    return `'${s}'`
}
function escapeHTML(text) {
    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;")
}
function span(text) {
    let element = document.createElement("span")
    element.innerHTML = escapeHTML(text)
    element.style.display = "hidden"
    element.style.width = "100%"
    element.style.textAlign = "center"
    return element
}

function raiseInternal(code, additionalMsg = "") {
    throw new Error(
        `An internal error occured in the classes extension. `+
        `Please report it. ${additionalMsg} [ERROR CODE: ${code}]`
    )
}

/**
 * Manages variables for a scope. ValueHolder can be referenced from multiple VariableManager instances.
 */
class VariableManager {
    /**
     * Implements a value storage, that can be set from multiple locations.
     */
    ValueHolder = class {
        constructor(value) {
            this.value = value
            this.isDeleted = false
        }
    }

    constructor() {
        this.reset()
    }
    reset() {
        if (this.variables !== undefined) {
            this.getNames().forEach((name) => this.delete(name))
        }
        this.variables = {}
    }
    set(name, value) {
        if (this.has(name)) {
            this.variables[name].value = value
        } else {
            this.variables[name] = new this.ValueHolder(value)
        }
    }
    setHolder(name, holder) {
        if (this.has(name)) {
            throw new Error(`Variable ${quote(name)} already exists in the current scope, can not bind variable with the same name.`)
        }
        this.variables[name] = holder
    }
    delete(name) {
        if (this.has(name)) {
            this.variables[name].isDeleted = true // Mark the variable deleted for all scopes
            delete this.variables[name]
        }
    }
    has(name) {
        return (name in this.variables) && (!this.variables[name].isDeleted)
    }
    get(name) {
        if (!this.has(name)) {
            throw new Error(`Variable ${quote(name)} is not defined.`)
        }
        return this.variables[name].value
    }
    getHolder(name) {
        if (!this.has(name)) {
            throw new Error(`Variable ${quote(name)} is not defined.`)
        }
        return this.variables[name]
    }
    getNames() {
        return Object.keys(this.variables)
    }
}

// System for storing data for a block, which will automatically be deleted when its thread is finished or stopped
class SpecialBlockStorageManager {
    constructor() {
        this.threads = new Map()
    }    
    storeBlockData(blockId, thread, data) {
        if (!this.threads.has(thread)) {
            this.threads.set(thread, {})
        }
        const threadBlockDatas = this.threads.get(thread)
        threadBlockDatas[blockId] = data
    }
    getBlockData(blockId, thread) {
        if (!this.threads.has(thread)) return
        const threadBlockDatas = this.threads.get(thread)
        return threadBlockDatas[blockId]
    }
    deleteThreadStorage(thread) {
        this.threads.delete(thread) // does not ever throw
    }
}

// System for storing environment data on a thread
class ThreadEnvManager {
    static GLOBALS = "GLOBALS"
    static FUNCTION = "FUNCTION"
    static METHOD = "METHOD"
    static GETTER_METHOD = "GETTER_METHOD"
    static SETTER_METHOD = "SETTER_METHOD"
    static OPERATOR_METHOD = "OPERATOR_METHOD"
    static CLASS_CTX = "CLASS_CTX"
    static USER_SCOPE = "USER_SCOPE"
    
    constructor() {
        this.scopes = [{type: ThreadEnvManager.GLOBALS, vars: new VariableManager()}]
        this.setNextFuncConfig()
    }
    
    // Enter Scopes
    enterFunction(args) {
        this.scopes.splice(0, 0, {type: ThreadEnvManager.FUNCTION, args, vars: new VariableManager()})
    }
    enterMethod(self, args) {
        this.scopes.splice(0, 0, {type: ThreadEnvManager.METHOD, self, args, vars: new VariableManager()})
    }
    enterGetterMethod(self) {
        this.scopes.splice(0, 0, {type: ThreadEnvManager.GETTER_METHOD, vars: new VariableManager()})
    }
    enterSetterMethod(self, setterValue) {
        this.scopes.splice(0, 0, {type: ThreadEnvManager.SETTER_METHOD, self, setterValue, vars: new VariableManager()})
    }
    enterOperatorMethod(self, other) {
        this.scopes.splice(0, 0, {type: ThreadEnvManager.OPERATOR_METHOD, self, other, vars: new VariableManager()})
    }
    enterClassContext(cls) {
        this.scopes.splice(0, 0, {type: ThreadEnvManager.CLASS_CTX, cls})
    }
    enterUserScope() {
        this.scopes.splice(0, 0, {type: ThreadEnvManager.USER_SCOPE, vars: new VariableManager()})
    }

    // Get Scope Variables
    _getScopeOfTypes(allowedTypes) {
        for (let i = 0; i < this.scopes.length; i++) {
            if (allowedTypes.includes(this.scopes[i].type)) return this.scopes[i]
        }
        return null
    }
    _getInnermostScope() {
        const scope = this.scopes[0]
        if (!scope) {
            raiseInternal("bold-koala")
        }
        return scope
    }
    
    getArgsOrThrow() {
        const scope = this._getScopeOfTypes([ThreadEnvManager.FUNCTION, ThreadEnvManager.METHOD])
        if (!scope) {
            throw new Error("Function arguments can only be used within a function or method.")
        }
        return scope.args
    }
    getSelfOrThrow() {
        const scope = this._getScopeOfTypes([ThreadEnvManager.METHOD, ThreadEnvManager.GETTER_METHOD, ThreadEnvManager.SETTER_METHOD, ThreadEnvManager.OPERATOR_METHOD])
        if (!scope) {
            throw new Error("self can only be used within an instance, getter or setter method.")
        }
        return scope.self
    }
    getSetterValueOrThrow() {
        const scope = this._getScopeOfTypes([ThreadEnvManager.SETTER_METHOD])
        if (!scope) {
            throw new Error("setter value can only be used within a setter method.")
        }
        return scope.setterValue
    }
    getOtherValueOrThrow() {
        const scope = this._getScopeOfTypes([ThreadEnvManager.OPERATOR_METHOD])
        if (!scope) {
            throw new Error("other value can only be used within an operator method.")
        }
        return scope.other
    }
    getClsOrThrow(blockText) {
        const innermost = this._getInnermostScope()
        if (innermost.type !== ThreadEnvManager.CLASS_CTX) {
            throw new Error(`${blockText} can only be used within a class definition or "on class" block.`)
        }
        return innermost.cls
    }
    
    // Exit Scopes
    prepareReturn() {
        const innermost = this._getInnermostScope()
        if (!([ThreadEnvManager.FUNCTION, ThreadEnvManager.METHOD, ThreadEnvManager.GETTER_METHOD, ThreadEnvManager.SETTER_METHOD, ThreadEnvManager.OPERATOR_METHOD].includes(innermost.type))) {
            throw new Error("return can only be used within a function or method.")
        }
        this.scopes.shift()
    }
    exitClassContext() {
        const innermost = this._getInnermostScope()
        if (innermost.type !== ThreadEnvManager.CLASS_CTX) {
            raiseInternal("nimble-panda")
        }
        this.scopes.shift()
    }
    exitUserScope() {
        const innermost = this._getInnermostScope()
        if (innermost.type !== ThreadEnvManager.USER_SCOPE) {
            raiseInternal("curious-otter")
        }
        this.scopes.shift()
    }
    
    // Measure Scopes
    getSize() {
        return this.scopes.length
    }

    trimSize(size) {
        if (size < 0) size = 0
        if (this.scopes.length <= size) return
        this.scopes.splice(0, this.scopes.length - size)
    }

    // Function Arguments
    setNextFuncConfig(config = {argNames: [], argDefaults: []}) {
        this.nextFuncConfig = config
    }
    getAndResetNextFuncConfig() {
        const config = this.nextFuncConfig
        this.setNextFuncConfig()
        return config
    }
    getDefaultFuncConfig() {
        return {argNames: [], argDefaults: []}
    }

    // Access Scoped Variables
    setScopeVar(name, value) {
        const innermost = this._getInnermostScope()
        if (innermost.type === ThreadEnvManager.CLASS_CTX) {
            // TODO: implement set class variable here
        } else {
            innermost.vars.set(name, value)
        }
    }
    _getScopeOfVar(name, startIndex = 0, excludeLastIndecies = 0) {
        for (let i = startIndex; i < (this.scopes.length - excludeLastIndecies); i++) {
            if (this.scopes[i].type === ThreadEnvManager.CLASS_CTX) continue
            if (this.scopes[i].vars.has(name)) return this.scopes[i]
        }
        // trick to raise:
        (new VariableManager()).get(name)
    }
    getScopeVar(name) {
        const varScope = this._getScopeOfVar(name)
        return varScope.vars.get(name)
    }
    deleteScopeVar(name) {
        const varScope = this._getScopeOfVar(name)
        varScope.vars.delete(name)
    }
    bindScopeVarGlobal(name) {
        const globalScope = this._getScopeOfTypes([ThreadEnvManager.GLOBALS])
        if (!globalScope) {
            raiseInternal("calm-seal")
        }
        if (!globalScope.vars.has(name)) {
            throw new Error(`No global variable named ${quote(name)} found.`)
        }

        const innermost = this._getInnermostScope()
        if (innermost.type === ThreadEnvManager.CLASS_CTX) {
            throw new Error(`Can not bind a variable to a class scope.`)
        }
        innermost.vars.setHolder(name, globalScope.vars.getHolder(name))
    }
    bindScopeVarNonlocal(name) {
        let varScope
        try { // skip innermost(current) and global scope, as nonlocal variables can not be in either
            varScope = this._getScopeOfVar(name, 1, 1)
        } catch {
            throw new Error(`No non-local variable named ${quote(name)} found.`)
        }

        const innermost = this._getInnermostScope()
        if (innermost.type === ThreadEnvManager.CLASS_CTX) {
            throw new Error(`Can not bind a variable to a class scope.`)
        }
        innermost.vars.setHolder(name, varScope.vars.getHolder(name))
    }
    hasScopeVar(name, onlyCurrentScope = false) {
        if (onlyCurrentScope) {
            const innermost = this._getInnermostScope()
            if (innermost.type === ThreadEnvManager.CLASS_CTX) return false
            return innermost.vars.has(name)
        }
        try {
            this._getScopeOfVar(name)
            return true
        } catch {
            return false
        }
    }
    /**
     * Return an array with all variable names visible in the current thread environment.
     * Iterates from outermost to innermost so inner-scope variables override outer ones.
     * @param {boolean} onlyCurrentScope - if true, return names only from the innermost scope
     * @returns {Array<string>}
     */
    getScopeVarNames(onlyCurrentScope = false) {
        if (onlyCurrentScope) {
            const innermost = this._getInnermostScope()
            if (innermost.type === ThreadEnvManager.CLASS_CTX) return []
            return innermost.vars.getNames()
        }

        const map = new Map()
        for (let i = this.scopes.length - 1; i >= 0; i--) {
            // iterate outermost -> innermost so inner scopes override outer ones
            if (this.scopes[i].type === ThreadEnvManager.CLASS_CTX) continue
            const names = this.scopes[i].vars.getNames()
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
    HIDE_ARGUMENT_DEFAULTS: false,
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


class TypeChecker {
    // All custom types one can get from a reporter in PM
    // (PenguinMod-Vm, PenguinMod-ExtensionsGallery) (as of 28.10.2025)
    // - Array
    // - Object
    // - Date
    // - Set
    // - Lambda
    // - Color
    // - UnlimitedNum (really Num, to avoid confusion)
    // - Target
    // - XML
    
    static isArray(value) {
        if (!Scratch.vm.jwArray) throw new Error("Array extension was not loaded properly.")
        return value instanceof Scratch.vm.jwArray.Type
    }
    
    static isObject(value) {
        if (!Scratch.vm.dogeiscutObject) throw new Error("Object extension was not loaded properly.")
        return value instanceof Scratch.vm.dogeiscutObject.Type
    }
    
    static isDate(value) { // There are three date extension
        if (Scratch.vm.jwDate && (value instanceof Scratch.vm.jwDate.Type)) return true
        if (runtime.ext_ddeDateFormat) {
            const dateType = Object.getPrototypeOf(runtime.ext_ddeDateFormat.currentDate())
            if (value instanceof dateType) return true
        }
        if (runtime.ext_ddeDateFormatV2) {
            const dateType = Object.getPrototypeOf(runtime.ext_ddeDateFormatV2.currentDate())
            if (value instanceof dateType) return true
        }
        return false
    }
    
    static isSet(value) {
        if (!Scratch.vm.dogeiscutSet) return false
        return value instanceof Scratch.vm.dogeiscutSet.Type
    }
    
    static isLambda(value) {
        if (!Scratch.vm.jwLambda) return false
        return value instanceof Scratch.vm.jwLambda.Type
    }
    
    static isColor(value) {
        if (!Scratch.vm.jwColor) return false
        return value instanceof Scratch.vm.jwColor.Type
    }
    
    static isUnlimitedNum(value) {
        if (!Scratch.vm.jwNum) return false
        return value instanceof Scratch.vm.jwNum.Type
    }

    static isTarget(value) {
        if (!Scratch.vm.jwTargets) return false
        return value instanceof Scratch.vm.jwTargets.Type
    }
    
    static isXML(value) {
        if (!Scratch.vm.jwXML) return false
        return value instanceof Scratch.vm.jwXML.Type
    }
}


class Cast extends Scratch.Cast {
    // Foreign
    /** @returns {Scratch.vm.jwArray.Type} */
    static toArray(value) {
        if (!Scratch.vm.jwArray) throw new Error("Array extension was not loaded properly.")
        return Scratch.vm.jwArray.Type.toArray(value)
    }
    
    /** @returns {Scratch.vm.dogeiscutObject.Type} */
    static toObject(value, copy = false) {
        if (!Scratch.vm.dogeiscutObject) throw new Error("Object extension was not loaded properly.")
        return Scratch.vm.dogeiscutObject.Type.toObject(value, copy)
    }
    
    // Own
    /** @returns {ClassType} */
    static toClass(value) {
        if (value instanceof ClassType) return value
        else if ((typeof value) === "string") return extensionClassInstance.classVars.get(value)
        else throw new Error("Expected a class or class variable name.")
    }

    /** @returns {ClassInstanceType} */
    static toClassInstance(value) {
        if (value instanceof ClassInstanceType) return value
        else throw new Error("Expected a class instance.")
    }

    /** @returns {FunctionType} */
    static toFunction(value) {
        if (value instanceof FunctionType) return value
        else if ((typeof value) === "string") return extensionClassInstance.funcVars.get(value)
        else throw new Error("Expected a function or function variable name.")
    }
}

/************************************************************************************
*                            Dependencies and Value Types                           *
************************************************************************************/

if (!Scratch.vm.jwArray) Scratch.vm.extensionManager.loadExtensionIdSync("jwArray")
if (!Scratch.vm.dogeiscutObject) Scratch.vm.extensionManager.loadExtensionURL(
    "https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutObject.js"
)

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
    className = "Callable" // Should allow s-plural

    /**
     * @param {string} name 
     * @param {Function} jsFunc
     * @param {Array<string>} argNames
     * @param {Array<string>} argDefaults
     */
    constructor(name, jsFunc, {argNames, argDefaults}) {
        super()
        this.name = name
        this.jsFunc = jsFunc
        this.argNames = argNames
        this.argDefaults = argDefaults
    }

    toString() {
        return `<${this.className} ${quote(this.name)}>`
    }
    toJSON() {
        return `${this.className}s can not be serialized.`
    }
    
    /**
     * @param {Thread} thread
     * @param {...any} args - class instance and other shadow values from the block (e.g., instance, posArgs, setter value, other operand)
     * @returns {any} the return value of the method
     */
    *execute(thread, ...args) {
        thread.gceEnv ??= new ThreadEnvManager()
        const sizeBefore = thread.gceEnv.getSize()
        this.enterContext(thread, ...args)
        
        let output
        let finished = false
        try {
            output = (yield* this.jsFunc(thread))
            finished = true
        } finally {
            if (finished) {
                if (sizeBefore !== thread.gceEnv.getSize()) {
                    raiseInternal("clever-badger")
                }
            } else {
                // An error happend, so exit stack frames that where interrupted
                thread.gceEnv.trimSize(sizeBefore)
            }

        }
        this.checkOutputValue(output)
        return output
    }

    enterContext(thread) {
        // Allow better subclassing
    }

    checkOutputValue(output) {
        // Allow better subclassing
    }
}

class FunctionType extends BaseCallableType {
    className = "Function"

    enterContext(thread, posArgs) {
        // Allow better subclassing
        const args = extensionClassInstance._evaluateArgs(this, posArgs)
        thread.gceEnv.enterFunction(args)
    }
}

class MethodType extends BaseCallableType {
    className = "Method"

    enterContext(thread, instance, posArgs = []) {
        // Allow better subclassing
        const args = extensionClassInstance._evaluateArgs(this, posArgs)
        thread.gceEnv.enterMethod(instance, args)
    }
}

class GetterMethodType extends MethodType {
    className = "Getter Method"
    
    enterContext(thread, instance, value) {
        thread.gceEnv.enterGetterMethod(instance, value)
    }
}
class SetterMethodType extends MethodType {
    className = "Setter Method"
    
    enterContext(thread, instance, value) {
        thread.gceEnv.enterSetterMethod(instance, value)
    }

    checkOutputValue(output) {
        if (output !== Nothing) throw new Error(`Setter methods must return ${Nothing}.`)
    }
}

class OperatorMethodType extends MethodType {
    className = "Operator Method"

    enterContext(thread, instance, other) {
        thread.gceEnv.enterOperatorMethod(instance, other)
    }
}

class ClassType extends CustomType {
    customId = "gceClass"

    /**
     * @param {string} name
     * @param {ClassType} superCls
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
        this.variables = {}
    }
    toString() {
        const suffix = this.superCls ? `(super ${quote(this.superCls.name)})` : ""
        return `<Class ${quote(this.name)}${suffix}>`
    }
    toJSON() {
        return "Classes can not be serialized."
    }

    /**
     * @param {string} name
     * @param {boolean} recursive
     * @param {boolean} preferSetter
     * @returns {?{type: string, value: any}}
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
        else if (name in this.variables) return {type: "class variable", value: this.variables[name]}
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
     * @returns {any}
     */
    getMemberOfType(name, expectedMemberType) {
        const {type, value} = this.getMember(name, true, expectedMemberType === "setter method")
        if (!type) throw new Error(`Undefined ${expectedMemberType} ${quote(name)}.`)
        if (type !== expectedMemberType) throw new Error(`Class Method or Variable ${quote(name)} is not a ${expectedMemberType} but a ${type}.`)
        return value
    }

    /**
     * @returns {Array<Object>}
     */
    getAllMembers() {
        let currentCls = this
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
        const variables = {}
        classChain.forEach((cls) => {
            Object.assign(instanceMethods, cls.instanceMethods)
            Object.assign(staticMethods, cls.staticMethods)
            Object.assign(getterMethods, cls.getters)
            Object.assign(setterMethods, cls.setters)
            Object.assign(operatorMethods, cls.operatorMethods)
            Object.assign(variables, cls.variables)
        })
        return [instanceMethods, staticMethods, getterMethods, setterMethods, operatorMethods, variables]
    }

    /**
     * @param {string} name
     * @param {string} newMemberType
     * @param {any} method
     */
    setMember(name, newMemberType, value) {
        const currentMemberType = this.getMember(name, false, false).type // preference does not matter
        if (currentMemberType && (currentMemberType !== newMemberType) && !(
            ((currentMemberType === "getter method") && (newMemberType === "setter method")) || 
            ((currentMemberType === "setter method") && (newMemberType === "getter method"))
        )) {
            throw new Error(`Can not assign ${newMemberType}: ${currentMemberType} alredy exists with the same name ${quote(name)}.`)
        }
        if (newMemberType === "instance method") this.instanceMethods[name] = value
        else if (newMemberType === "static method") this.staticMethods[name] = value
        else if (newMemberType === "getter method") this.getters[name] = value
        else if (newMemberType === "setter method") this.setters[name] = value
        else if (newMemberType === "operator method") this.operatorMethods[name] = value
        else if (newMemberType === "class variable") this.variables[name] = value
    }
    
    /**
     * @param {Thread} thread 
     * @param {array} posArgs
     * @returns {ClassInstanceType} the instance
     */
    *createInstance(thread, posArgs) {
        const instance = new ClassInstanceType(this) 
        const output = yield* instance.executeInstanceMethod(thread, CONFIG.INIT_METHOD_NAME, posArgs) // an init method always exists
        if (output !== Nothing) throw new Error(`Initialization methods must return ${Nothing}.`)
        return instance
    }
    *executeStaticMethod(thread, name, posArgs) {
        const methodFunc = this.getMemberOfType(name, "static method")
        return yield* methodFunc.execute(thread, posArgs)
    }
    
    getClassVariable(name) {
        const member = this.getMember(name, true, false) // preference does not matter
        if (!member || member.type !== "class variable") {
            throw new Error(`Undefined class variable ${quote(name)}.`)
        }
        return member.value
    }
    
    getStaticMethod(name) {
        return this.getMemberOfType(name, "static method")
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
const commonSuperClass = new ClassType("Superclass", null)
commonSuperClass.instanceMethods[CONFIG.INIT_METHOD_NAME] = new MethodType(
    CONFIG.INIT_METHOD_NAME, 
    function* (thread) {
        thread.gceEnv ??= new ThreadEnvManager()
        thread.gceEnv.prepareReturn()
        // Nothing is indepedent of function context, so we can exit context before
        return Nothing
    }, 
    {argNames: [], argDefaults: []}
)

class ClassInstanceType extends CustomType {
    customId = "gceClassInstance"

    /**
     * @param {ClassType} cls 
     */
    constructor(cls) {
        super()
        if (!(cls instanceof ClassType)) throw new Error("Cannot create class instance with no class given.")
        this.cls = cls
        this.attributes = {}
    }
    toString() {
        return `<Instance of ${quote(this.cls.name)}>`
    }
    toJSON() {
        return "Class Instances can not be serialized."
    }
    // OPTIONAL FUTURE TODO: define toReporterContent for better visualization

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {array} posArgs
     * @returns {any} the return value of the method
     */
    *executeInstanceMethod(thread, name, posArgs) {
        const method = this.cls.getMemberOfType(name, "instance method")
        return yield* method.execute(thread, this, posArgs)
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {array} posArgs
     * @returns {any} the return value of the method
     */
    *executeSuperMethod(thread, name, posArgs) {
        if (!this.cls.superCls) throw new Error("Can not call super instance method: class has no superclass.")
        const method = this.cls.superCls.getMemberOfType(name, "instance method")
        return yield* method.execute(thread, this, posArgs)
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {array} posArgs
     * @returns {any} the return value of the method
     */
    *executeSuperInitMethod(thread, name, posArgs) {
        const output = yield* this.executeSuperMethod(thread, name, posArgs)
        if (output !== Nothing) throw new Error(`Initialization methods must return ${Nothing}.`)
        return output
    }

    /**
     * @param {Thread} thread
     * @param {string} name public operator method name
     * @param {any} other
     * @returns {any} the return value of the operator method
     */
    *executeOperatorMethod(thread, name, other) {
        const method = this.cls.getMemberOfType(CONFIG.INTERNAL_OP_NAMES[name], "operator method")
        return yield* method.execute(thread, this, other)
    }
 
    /**
     * @param {Thread} thread
     * @param {string} name
     * @returns {any} the attribute value or return value of getter method
     */
    *getAttribute(thread, name) {
        const methodMember = this.cls.getMember(name, true, false)
        if (methodMember && methodMember.type === "getter method") {
            return (yield* methodMember.value.execute(thread, this, []))
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
        defaultValue: "Function1",
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
        blockShape: "gceClassesOOP-doublePlus",
        forceOutputType: "gceClassInstance",
        disableMonitor: true,
    },
    Argument: {
        shape: "gceClassesOOP-doublePlus",
        exemptFromNormalization: true,
        check: ["gceClassInstance", "dogeiscutObject"],
    },
}
if (!CUSTOM_SHAPE) {
    delete gceClassInstance.Block.blockShape
    delete gceClassInstance.Argument.shape
}
const gceNothing = {
    Type: NothingType,
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
    variableName: {
        type: ArgumentType.STRING,
        defaultValue: "myVar",
    },
    classVarName: {
        type: ArgumentType.STRING,
        defaultValue: "MyClass",
    },
    methodName: {
        type: ArgumentType.STRING,
        defaultValue: "myMethod",
    },
    argumentName: {
        type: ArgumentType.STRING,
        defaultValue: "myArg",
    },
    classVariableName: {
        type: ArgumentType.STRING,
        defaultValue: "myVariable",
    },
    funcName: {
        type: ArgumentType.STRING,
        defaultValue: "Function1",
    },
    attributeName: {
        type: ArgumentType.STRING,
        defaultValue: "myAttr",
    },
    argNames: {
        type: ArgumentType.STRING,
        exemptFromNormalization: true,
        defaultValue: '["name"]',
    },
    argDefaults: {
        type: ArgumentType.STRING,
        exemptFromNormalization: true,
        defaultValue: "[]",
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

class GCEClassBlocks {
    /**
     * @returns {object} metadata for this extension and its blocks.
     */
    getInfo() {
        const makeLabel = (text) => ({blockType: Scratch.BlockType.LABEL, text: text})
        const info = {
            id: "gceClassesOOP",
            name: "Classes",
            color1: "#428af5ff",
            menuIconURI: "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICB2aWV3Qm94PSIwIDAgMjAgMjAiCiAgdmVyc2lvbj0iMS4xIgogIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPGNpcmNsZQogICAgY3g9IjEwIgogICAgY3k9IjEwIgogICAgcj0iOSIKICAgIHN0eWxlPSJmaWxsOiM0MjhhZjVmZjsgc3Ryb2tlOiMyZDVmYTg7IHN0cm9rZS13aWR0aDoycHg7IGZpbGwtb3BhY2l0eToxOyBzdHJva2Utb3BhY2l0eToxOyBwYWludC1vcmRlcjpzdHJva2UiIC8+CiAgPHBhdGgKICAgIGQ9Im0gMy41LDEwIDQuNSwtNS41IDEuMiwwLjYgLTMuNyw0LjkgMy43LDQuOSAtMS4yLDAuNiB6CiAgICAgICBtIDEzLDAgLTQuNSwtNS41IC0xLjIsMC42IDMuNyw0LjkgLTMuNyw0LjkgMS4yLDAuNiB6IgogICAgc3R5bGU9ImZpbGw6I2ZmZmZmZiIgLz4KPC9zdmc+",
            blocks: [
                makeLabel("Scoped Variables"),
                {
                    ...commonBlocks.command,
                    opcode: "setScopeVar",
                    text: "set local var [NAME] to [VALUE]",
                    arguments: {
                        NAME: commonArguments.variableName,
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "getScopeVar",
                    text: "get var [NAME]",
                    arguments: {
                        NAME: commonArguments.variableName,
                    },
                },
                {
                    ...commonBlocks.returnsBoolean,
                    opcode: "hasScopeVar",
                    text: "var [NAME] exists in [KIND]?",
                    arguments: {
                        NAME: commonArguments.variableName,
                        KIND: {type: ArgumentType.STRING, menu: "variableAvailableKind"},
                    },
                },
                {
                    ...commonBlocks.command,
                    opcode: "deleteScopeVar",
                    text: "delete var [NAME]",
                    arguments: {
                        NAME: commonArguments.variableName,
                    },
                },
                {
                    ...jwArrayStub.Block,
                    opcode: "allVariables",
                    text: "all variables in [KIND]",
                    arguments: {
                        KIND: {type: ArgumentType.STRING, menu: "variableAvailableKind"},
                    },

                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "createVarScope",
                    text: ["create local variable scope"],
                },
                {
                    ...commonBlocks.command,
                    opcode: "bindVarToScope",
                    text: "bind [KIND] variable [NAME] to local scope",
                    arguments: {
                        KIND: {type: ArgumentType.STRING, menu: "bindVarOriginKind"},
                        NAME: commonArguments.variableName,
                    },
                },
                makeLabel("Define Classes"),
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "createClassAt",
                    text: ["create class at var [NAME] [SHADOW]"],
                    arguments: {
                        NAME: commonArguments.classVarName,
                        SHADOW: {fillIn: "classBeingCreated"},
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "createSubclassAt",
                    text: ["create subclass at var [NAME] with superclass [SUPERCLASS] [SHADOW]"],
                    arguments: {
                        NAME: {...commonArguments.classVarName, defaultValue: "MySubclass"},
                        SUPERCLASS: gceClass.ArgumentClassOrVarName,
                        SHADOW: {fillIn: "classBeingCreated"},
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "createClassNamed",
                    text: ["create class named [NAME] [SHADOW]"],
                    branchCount: 1,
                    arguments: {
                        NAME: commonArguments.classVarName,
                        SHADOW: {fillIn: "classBeingCreated"},
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "createSubclassNamed",
                    text: ["create subclass named [NAME] with superclass [SUPERCLASS] [SHADOW]"],
                    branchCount: 1,
                    arguments: {
                        NAME: {...commonArguments.classVarName, defaultValue: "MySubclass"},
                        SUPERCLASS: gceClass.ArgumentClassOrVarName,
                        SHADOW: {fillIn: "classBeingCreated"},
                    },
                },                
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "onClass",
                    text: ["on class [CLASS] [SHADOW]"],
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        SHADOW: {fillIn: "classBeingCreated"},
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "classBeingCreated",
                    text: "class being created",
                    canDragDuplicate: true,
                    hideFromPalette: true,
                },
                {
                    ...commonBlocks.command,
                    opcode: "setClass",
                    text: "set class [NAME] to [CLASS]",
                    arguments: {
                        NAME: commonArguments.classVarName,
                        CLASS: gceClass.Argument,
                    },
                },
                "---",
                makeLabel("Use Classes"),
                {
                    ...gceClass.Block,
                    opcode: "getClass",
                    text: "get class [NAME]",
                    arguments: {
                        NAME: commonArguments.classVarName,
                    },
                },
                {
                    ...commonBlocks.returnsBoolean,
                    opcode: "classExists",
                    text: "class [NAME] exists?",
                    arguments: {
                        NAME: commonArguments.classVarName,
                    },
                },
                {
                    ...jwArrayStub.Block,
                    opcode: "allClasses",
                    text: "all classes",
                },
                {
                    ...commonBlocks.command,
                    opcode: "deleteClass",
                    text: "delete class [NAME]",
                    arguments: {
                        NAME: commonArguments.classVarName,
                    },
                },
                {
                    ...commonBlocks.command,
                    opcode: "deleteAllClasses",
                    text: "delete all classes",
                },
                {
                    ...commonBlocks.returnsBoolean,
                    opcode: "isSubclass",
                    text: "is [SUBCLASS] a subclass of [SUPERCLASS] ?",
                    arguments: {
                        SUBCLASS: gceClass.ArgumentClassOrVarName,
                        SUPERCLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "getSuperclass",
                    text: "get superclass of [CLASS]",
                    arguments: {
                        CLASS: {...gceClass.ArgumentClassOrVarName, defaultValue: "MySubclass"},
                    },
                },
                "---",
                "---",
                makeLabel("Class Members (use within class)"),
                "---",
                makeLabel("Define Instance Methods"),
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineInstanceMethod",
                    text: ["define instance method [NAME] [SHADOW1] [SHADOW2]"],
                    arguments: {
                        NAME: commonArguments.methodName,
                        SHADOW1: {fillIn: "self"},
                        SHADOW2: {fillIn: "allFunctionArgs"},
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineSpecialMethod",
                    text: ["define [SPECIAL_METHOD] method [SHADOW1] [SHADOW2]"],
                    arguments: {
                        SPECIAL_METHOD: {type: ArgumentType.STRING, menu: "specialMethod"},
                        SHADOW1: {fillIn: "self"},
                        SHADOW2: {fillIn: "allFunctionArgs"},
                    },
                },
                {
                    ...gceClassInstance.Block,
                    opcode: "self",
                    text: "self",
                    canDragDuplicate: true,
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "callSuperMethod",
                    text: "call super method [NAME] with positional args [POSARGS]",
                    arguments: {
                        NAME: commonArguments.methodName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                {
                    ...gceNothing.Block,
                    opcode: "callSuperInitMethod",
                    text: "call super init method with positional args [POSARGS]",
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
                    arguments: {
                        NAME: commonArguments.attributeName,
                        SHADOW: {fillIn: "self"},
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineSetter",
                    text: ["define setter [NAME] [SHADOW1] [SHADOW2]"],
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
                    hideFromPalette: true,
                    canDragDuplicate: true,
                },
                "---",
                makeLabel("Define Operator Methods"),
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineOperatorMethod",
                    text: ["define operator method [OPERATOR_KIND] [SHADOW]"],
                    arguments: {
                        OPERATOR_KIND: {type: ArgumentType.STRING, menu: "operatorMethod"},
                        SHADOW: {fillIn: "operatorOtherValue"},
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "operatorOtherValue",
                    text: "other value",
                    hideFromPalette: true,
                    canDragDuplicate: true,
                },
                "---",
                makeLabel("Define Static Methods & Class Variables"),
                {
                    ...commonBlocks.command,
                    opcode: "setClassVariable",
                    text: "on [CLASS] set class variable [NAME] to [VALUE]",
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        NAME: commonArguments.classVariableName,
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "getClassVariable",
                    text: "get class variable [NAME] of [CLASS]",
                    arguments: {
                        NAME: commonArguments.classVariableName,
                        CLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                {
                    ...commonBlocks.command,
                    opcode: "deleteClassVariable",
                    text: "on [CLASS] delete class variable [NAME]",
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        NAME: commonArguments.classVariableName,
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineStaticMethod",
                    text: ["define static method [NAME] [SHADOW]"],
                    arguments: {
                        NAME: commonArguments.methodName,
                        SHADOW: {fillIn: "allFunctionArgs"},
                    },
                },
                {
                    ...jwArrayStub.Block,
                    opcode: "propertyNamesOfClass",
                    text: "[PROPERTY] names of class [CLASS]",
                    arguments: {
                        PROPERTY: {type: ArgumentType.STRING, menu: "classProperty"},
                        CLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                "---",
                "---",
                makeLabel("Working with Instances"),
                "---",
                makeLabel("Create & Inspect"),
                {
                    ...gceClassInstance.Block,
                    opcode: "createInstance",
                    text: "create instance of class [CLASS] with positional args [POSARGS]",
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                {
                    ...commonBlocks.returnsBoolean,
                    opcode: "isInstance",
                    text: "is [INSTANCE] an instance of [CLASS] ?",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                        CLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "getClassOfInstance",
                    text: "get class of [INSTANCE]",
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
                    arguments: {
                        NAME: commonArguments.attributeName,
                        INSTANCE: gceClassInstance.Argument,
                    },
                },
                {
                    ...dogeiscutObjectStub.Block,
                    opcode: "getAllAttributes",
                    text: "all attributes of [INSTANCE]",
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
                    arguments: {
                        NAME: commonArguments.methodName,
                        CLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                "---",
                "---",
                makeLabel("Functions"),
                "---",
                makeLabel("Configure Before Define"),
                {
                    ...commonBlocks.command,
                    opcode: "configureNextFunctionArgs",
                    text: "configure next function: argument names [ARGNAMES] defaults [ARGDEFAULTS]",
                    arguments: {
                        ARGNAMES: commonArguments.argNames,
                        ARGDEFAULTS: commonArguments.argDefaults,
                    },
                },
                "---",
                makeLabel("Define"),
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "createFunctionAt",
                    text: ["create function at [NAME] [SHADOW]"],
                    arguments: {
                        NAME: commonArguments.funcName,
                        SHADOW: {fillIn: "allFunctionArgs"},
                    },
                },
                {
                    ...gceFunction.Block,
                    opcode: "createFunctionNamed",
                    text: ["create function named [NAME] [SHADOW]"],
                    branchCount: 1,
                    arguments: {
                        NAME: commonArguments.funcName,
                        SHADOW: {fillIn: "allFunctionArgs"},
                    },
                },
                "---",
                makeLabel("Inside Functions & Methods"),
                {
                    ...dogeiscutObjectStub.Block,
                    opcode: "allFunctionArgs",
                    text: "function arguments",
                    canDragDuplicate: true,
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "functionArg",
                    text: "function arg [NAME]",
                    arguments: {
                        NAME: commonArguments.argumentName,
                    },
                    canDragDuplicate: true,
                },
                {
                    ...commonBlocks.command,
                    opcode: "return",
                    text: "return [VALUE]",
                    isTerminal: true,
                    arguments: {
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    ...commonBlocks.command,
                    opcode: "transferFunctionArgsToTempVars",
                    text: "transfer arguments to temporary variables",
                },
                { // BUTTON
                    opcode: "addTempVars",
                    text: "add temporary variables extension",
                    blockType: BlockType.BUTTON,
                },
                "---",
                makeLabel("Use Functions"),
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "callFunction",
                    text: "call function [FUNC] with positional args [POSARGS]",
                    arguments: {
                        FUNC: gceFunction.ArgumentFunctionOrVarName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                {
                    ...gceFunction.Block,
                    opcode: "getFunction",
                    text: "get function [NAME]",
                    arguments: {
                        NAME: commonArguments.funcName,
                    },
                },
                {
                    ...commonBlocks.returnsBoolean,
                    opcode: "functionExists",
                    text: "function [NAME] exists?",
                    arguments: {
                        NAME: commonArguments.funcName,
                    },
                },
                {
                    ...jwArrayStub.Block,
                    opcode: "allFunctions",
                    text: "all functions",
                },
                {
                    ...commonBlocks.command,
                    opcode: "deleteFunction",
                    text: "delete function [NAME]",
                    arguments: {
                        NAME: commonArguments.funcName,
                    },
                },
                {
                    ...commonBlocks.command,
                    opcode: "deleteAllFunctions",
                    text: "delete all functions",
                },
                "---",
                "---",
                makeLabel("Utilities"),
                {
                    ...commonBlocks.returnString,
                    opcode: "objectAsString",
                    text: "[VALUE] as string",
                    arguments: {
                        VALUE: commonArguments.allowAnything,
                    }
                },
                {
                    ...commonBlocks.returnString,
                    opcode: "typeof",
                    text: "typeof [VALUE]",
                    arguments: {
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    ...commonBlocks.returnsBoolean,
                    opcode: "checkIdentity",
                    text: "[VALUE1] is [VALUE2] ?",
                    arguments: {
                        VALUE1: commonArguments.allowAnything,
                        VALUE2: commonArguments.allowAnything,
                    },
                },
                {
                    ...gceNothing.Block,
                    opcode: "nothing",
                    text: "Nothing",
                },
                {
                    ...commonBlocks.command,
                    opcode: "executeExpression",
                    text: "execute expression [EXPR]",
                    arguments: {
                        EXPR: commonArguments.allowAnything,
                    },
                },
                //{
                //    
                //},
            ],
            menus: {
                variableAvailableKind: {
                    acceptReporters: false,
                    items: [
                        "all scopes",
                        "local scope",
                    ],
                },
                bindVarOriginKind: {
                    acceptReporters: false,
                    items: [
                        "non-local",
                        "global",
                    ],
                },
                classProperty: {
                    acceptReporters: false,
                    items: [
                        "instance method",
                        "static method",
                        "getter method",
                        "setter method",
                        "operator method",
                        "class variable",
                    ],
                },
                operatorMethod: {
                    acceptReporters: false,
                    items: Object.entries(CONFIG.INTERNAL_OP_NAMES).map(([publicName, internalName]) => {
                        return {text: publicName, value: internalName}
                    })
                },
                specialMethod: {
                    acceptReporters: false,
                    items: [
                        {text: "init", value: CONFIG.INIT_METHOD_NAME},
                        {text: "as string", value: CONFIG.AS_STRING_METHOD_NAME},
                    ],
                }
            },
        }
        if (CONFIG.HIDE_ARGUMENT_DEFAULTS) {
            info.blocks.forEach((blockInfo) => {
                if (blockInfo.arguments) {
                    Object.keys(blockInfo.arguments).forEach((argumentName) => {
                        delete blockInfo.arguments[argumentName]["defaultValue"]
                    })
                }
            })
        }
        return info
    }
    
    getCompileInfo() {
        const createIRGenerator = (kind, inputs, fields, yieldRequired = false) => (generator, block) => {
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
        }

        const EXTENSION_PREFIX = "runtime.ext_gceClassesOOP"
        const ENV_PREFIX = `${EXTENSION_PREFIX}.environment`
        const ENV_MANAGER = `${ENV_PREFIX}.ThreadEnvManager()`
        const CAST_PREFIX = `${EXTENSION_PREFIX}.Cast`

        const createClassCore = (node, compiler, setVariable, superClsCode = null) => {
            const nameCode = compiler.descendInput(node.NAME).asString()
            const clsLocal = compiler.localVariables.next()
            const superClass = superClsCode ? `${CAST_PREFIX}.toClass(${superClsCode})`: `${ENV_PREFIX}.commonSuperClass`
            
            return {
                setup: `thread.gceEnv ??= new ${ENV_MANAGER};` +
                    `const ${clsLocal} = new ${ENV_PREFIX}.ClassType(${nameCode}, ${superClass});` +
                    (setVariable ? `${EXTENSION_PREFIX}.classVars.set(${clsLocal}.name, ${clsLocal});` : "") +
                    `thread.gceEnv.enterClassContext(${clsLocal});`,
                cleanup: "thread.gceEnv.exitClassContext();",
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
            
            compiler.source += `thread.gceEnv ??= new ${ENV_MANAGER};` +
                `const ${nameLocal} = ${nameCode};` +
                `thread.gceEnv.getClsOrThrow("define method").setMember(${nameLocal}, ${quote(memberType)}, `+
                `new ${ENV_PREFIX}.${classId}(${nameLocal}, function* (thread) {`
            addSubstackCode(compiler, node.SUBSTACK, imports)
            compiler.source += "thread.gceEnv.prepareReturn();" + 
                // Nothing is indepedent of function context, so we can exit context before
                `return ${ENV_PREFIX}.Nothing;` +
                "}, thread.gceEnv." + (disableFuncConfig ? "getDefaultFuncConfig()" : "getAndResetNextFuncConfig()") + "));\n"
        }

        const createCallCode = (castMethod, target, m, ...args) => {
            return `(yield* ${CAST_PREFIX}.${castMethod}(${target}).${m}(thread, ${args.join(", ")}))`
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

        return {
            ir: {
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


                // Define
                createFunctionAt: createIRGenerator("stack", ["NAME", "SUBSTACK"], []),
                createFunctionNamed: createIRGenerator("input", ["NAME", "SUBSTACK"], []),

                // Inside Functions & Methods
                return: createIRGenerator("stack", ["VALUE"], []),
                transferFunctionArgsToTempVars: createIRGenerator("stack", [], []),

                // Use Functions
                callFunction: createIRGenerator("input", ["FUNC", "POSARGS"], [], true),


                // Utilities
                objectAsString: createIRGenerator("input", ["VALUE"], [], true),                
            },
            js: {
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
                    const nameCode = quote(node.SPECIAL_METHOD)
                    createMethodDefinition(node, compiler, imports, nameCode, "MethodType", "instance method", false)
                },
                callSuperMethod: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = `(thread.gceEnv ??= new ${ENV_MANAGER}, ` +
                        `(yield* thread.gceEnv.getSelfOrThrow().executeSuperMethod(thread, ${nameCode}, ${posArgsCode})))`
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
                callSuperInitMethod: (node, compiler, imports) => {
                    const nameCode = quote(CONFIG.INIT_METHOD_NAME)
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = `(thread.gceEnv ??= new ${ENV_MANAGER}, ` +
                        `(yield* thread.gceEnv.getSelfOrThrow().executeSuperInitMethod(thread, ${nameCode}, ${posArgsCode})))`
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Define Getters & Setters
                defineGetter: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.name).asString()
                    createMethodDefinition(node, compiler, imports, nameCode, "GetterMethodType", "getter method", true)
                },
                defineSetter: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    createMethodDefinition(node, compiler, imports, nameCode, "SetterMethodType", "setter method", true)
                },
                
                // Define Operator Methods
                defineOperatorMethod: (node, compiler, imports) => {
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
                    const generatedCode = createCallCode("toClass", classCode, "createInstance", posArgsCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Attributes
                setAttribute: (node, compiler, imports) => {
                    const instanceCode = compiler.descendInput(node.INSTANCE).asUnknown()
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const valueCode = compiler.descendInput(node.VALUE).asUnknown()
                    compiler.source += createCallCode("toClassInstance", instanceCode, "setAttribute", nameCode, valueCode) + ";\n"
                },
                getAttribute: (node, compiler, imports) => {
                    const instanceCode = compiler.descendInput(node.INSTANCE).asUnknown()
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const generatedCode = createCallCode("toClassInstance", instanceCode, "getAttribute", nameCode) 
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Call Methods
                callMethod: (node, compiler, imports) => {
                    const instanceCode = compiler.descendInput(node.INSTANCE).asUnknown()
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = createCallCode("toClassInstance", instanceCode, "executeInstanceMethod", nameCode, posArgsCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
                callStaticMethod: (node, compiler, imports) => {
                    const classCode = compiler.descendInput(node.CLASS).asUnknown()
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = createCallCode("toClass", classCode, "executeStaticMethod", nameCode, posArgsCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },


                // Define
                createFunctionAt: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const nameLocal = compiler.localVariables.next()
                    
                    compiler.source += `thread.gceEnv ??= new ${ENV_MANAGER};` +
                        `const ${nameLocal} = ${nameCode};` +
                        `${EXTENSION_PREFIX}.funcVars.set(${nameLocal}, new ${ENV_PREFIX}.FunctionType(${nameLocal}, function* (thread) {`
                    addSubstackCode(compiler, node.SUBSTACK, imports)
                    compiler.source += "thread.gceEnv.prepareReturn();" +
                        // Nothing is indepedent of function context, so we can exit context before
                        `return ${ENV_PREFIX}.Nothing;` +
                        "}, thread.gceEnv.getAndResetNextFuncConfig()));\n"
                },
                createFunctionNamed: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const generatedCode = `(thread.gceEnv ??= new ${ENV_MANAGER}, ` +
                        `new ${ENV_PREFIX}.FunctionType(${nameCode}, function* (thread) {`+
                        getSubstackCode(compiler, node.SUBSTACK, imports)+
                        "thread.gceEnv.prepareReturn();" +
                        // Nothing is indepedent of function context, so we can exit context before
                        `return ${ENV_PREFIX}.Nothing;` +
                        "}, thread.gceEnv.getAndResetNextFuncConfig()))"
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Inside Functions & Methods
                return: (node, compiler, imports) => {
                    const returnValueLocal = compiler.localVariables.next()
                    // We need to cache the return value before exiting context, as it might depend on it
                    compiler.source += `thread.gceEnv ??= new ${ENV_MANAGER};` +
                        `const ${returnValueLocal} = ${compiler.descendInput(node.VALUE).asUnknown()};` +
                        "thread.gceEnv.prepareReturn();" +
                        `return ${returnValueLocal};\n`
                },
                transferFunctionArgsToTempVars: (node, compiler, imports) => {
                    // tempVars seems to always be defined
                    compiler.source += 'try {tempVars} catch {throw new Error("Failed to transfer to temporary variables.")};' +
                        `thread.gceEnv ??= new ${ENV_MANAGER};` +
                        "Object.assign(tempVars, thread.gceEnv.getArgsOrThrow());\n"
                },

                // Use Functions
                callFunction: (node, compiler, imports) => {
                    const funcCode = compiler.descendInput(node.FUNC).asUnknown()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = createCallCode("toFunction", funcCode, "execute", posArgsCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },


                // Utilities
                objectAsString: (node, compiler, imports) => {
                    const objectCode = compiler.descendInput(node.VALUE).asUnknown()
                    const generatedCode = `(yield* ${EXTENSION_PREFIX}._objectAsString(${objectCode}, thread))`
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
            },
        }
    }
    
    constructor() {
        // to allow other extensions access from the extension class
        Object.assign(Scratch.vm, {gceFunction, gceMethod, gceClass, gceClassInstance, gceNothing})
        this.Cast = Cast
        this.environment = {
            VariableManager, SpecialBlockStorageManager, ThreadEnvManager, CONFIG, 
            TypeChecker, Cast, CustomType, BaseCallableType, FunctionType,
            MethodType, GetterMethodType, SetterMethodType, OperatorMethodType,
            ClassType, commonSuperClass, ClassInstanceType, NothingType, Nothing,
            gceFunction, gceMethod, gceClass, gceClassInstance, gceNothing,
        }

        runtime.registerCompiledExtensionBlocks("gceClassesOOP", this.getCompileInfo())
        runtime.registerSerializer(
            "gceNothing",
            v => (v instanceof NothingType ? v.toJSON() : null),
            v => Nothing,
        )
        Scratch.gui.getBlockly().then(ScratchBlocks => {
            ScratchBlocks.BlockSvg.registerCustomShape("gceClassesOOP-doublePlus", CUSTOM_SHAPE)
        })
        
        applyHacks(Scratch)

        this.classVars = new VariableManager()
        this.funcVars = new VariableManager()
        this.specialBlockStorage = new SpecialBlockStorageManager()
        
        runtime.on("THREAD_FINISHED", (thread) => {this.specialBlockStorage.deleteThreadStorage(thread)})
    }    
    
    /************************************************************************************
    *                                       Blocks                                      *
    ************************************************************************************/

    /******************** Scoped Variables ********************/

    setScopeVar(args, util) {
        const name = Cast.toString(args.NAME)
        util.thread.gceEnv ??= new ThreadEnvManager()
        util.thread.gceEnv.setScopeVar(name, args.VALUE)
    }
    getScopeVar(args, util) {
        const name = Cast.toString(args.NAME)
        util.thread.gceEnv ??= new ThreadEnvManager()
        return util.thread.gceEnv.getScopeVar(name)
    }
    hasScopeVar(args, util) {
        const name = Cast.toString(args.NAME)
        const onlyCurrentScope = Cast.toString(args.KIND) === "local scope"
        util.thread.gceEnv ??= new ThreadEnvManager()
        return Cast.toBoolean(util.thread.gceEnv.hasScopeVar(name, onlyCurrentScope))
    }
    deleteScopeVar(args, util) {
        const name = Cast.toString(args.NAME)
        util.thread.gceEnv ??= new ThreadEnvManager()
        util.thread.gceEnv.deleteScopeVar(name)
    }
    allVariables(args, util) {
        const onlyCurrentScope = Cast.toString(args.KIND) === "local scope"
        util.thread.gceEnv ??= new ThreadEnvManager()
        return Cast.toArray(util.thread.gceEnv.getScopeVarNames(onlyCurrentScope))
    }
    createVarScope(args, util) {
        util.thread.gceEnv ??= new ThreadEnvManager()
        util.thread.gceEnv.enterUserScope()
        util.startBranch(1, false, () => {
            util.thread.gceEnv.exitUserScope()
        })
    }
    bindVarToScope(args, util) {
        const name = Cast.toString(args.NAME)
        util.thread.gceEnv ??= new ThreadEnvManager()
        switch (Cast.toString(args.KIND)) {
            case "non-local":
                util.thread.gceEnv.bindScopeVarNonlocal(name)
                break
            case "global":
                util.thread.gceEnv.bindScopeVarGlobal(name)
                break
        }
        util.thread.gceEnv ??= new ThreadEnvManager()
        ({
            ...commonBlocks.command,
            opcode: "bindVarToScope",
            text: "bind [KIND] variable [NAME] to local scope",
            arguments: {
                KIND: {type: ArgumentType.STRING, menu: "bindVarOriginKind"},
                NAME: commonArguments.classVarName,
            },
        })
    }

    /******************** Classes ********************/

    // Define Classes
    createClassAt = this._isACompiledBlock
    createSubclassAt = this._isACompiledBlock
    createClassNamed = this._isACompiledBlock
    createSubclassNamed = this._isACompiledBlock
    onClass(args, util) {
        const cls = Cast.toClass(args.CLASS)
        util.thread.gceEnv ??= new ThreadEnvManager()
        util.thread.gceEnv.enterClassContext(cls)
        util.startBranch(1, false, () => {
            util.thread.gceEnv.exitClassContext()
        })
    }
    classBeingCreated(args, util) {
        util.thread.gceEnv ??= new ThreadEnvManager()
        return util.thread.gceEnv.getClsOrThrow("class being created")
    }
    setClass(args, util) {
        const name = Cast.toString(args.NAME)
        const cls = Cast.toClass(args.CLASS)
        this.classVars.set(name, cls)
    }

    // Use Classes
    getClass(args, util) {
        const name = Cast.toString(args.NAME)
        return this.classVars.get(name)
    }
    classExists(args, util) {
        const name = Cast.toString(args.NAME)
        return Cast.toBoolean(this.classVars.has(name))
    }
    allClasses(args, util) {
        return Cast.toArray(this.classVars.getNames())
    }
    deleteClass(args, util) {
        this.classVars.delete(Cast.toString(args.NAME))
    }
    deleteAllClasses(args, util) {
        this.classVars.reset()
    }
    isSubclass(args, util) {
        const subCls = Cast.toClass(args.SUBCLASS)
        const superCls = Cast.toClass(args.SUPERCLASS)
        return Cast.toBoolean(subCls.isSubclassOf(superCls))
    }
    getSuperclass(args, util) {
        const cls = Cast.toClass(args.CLASS)
        return cls.superCls ?? Nothing
    }
    
    /******************** Class Members ********************/

    // Define Instance Methods
    defineInstanceMethod = this._isACompiledBlock
    defineSpecialMethod = this._isACompiledBlock
    self(args, util) {
        util.thread.gceEnv ??= new ThreadEnvManager()
        return util.thread.gceEnv.getSelfOrThrow()
    }
    callSuperMethod = this._isACompiledBlock
    callSuperInitMethod = this._isACompiledBlock

    // Define Getters & Setters
    defineGetter = this._isACompiledBlock
    defineSetter = this._isACompiledBlock
    defineSetterValue(args, util) {
        util.thread.gceEnv ??= new ThreadEnvManager()
        return util.thread.gceEnv.getSetterValueOrThrow()
    }

    // Define Operator Methods
    defineOperatorMethod = this._isACompiledBlock
    operatorOtherValue(args, util) {
        util.thread.gceEnv ??= new ThreadEnvManager()
        return util.thread.gceEnv.getOtherValueOrThrow()
    }

    // Define Static Methods & Class Variables
    setClassVariable(args, util) {
        const cls = Cast.toClass(args.CLASS)
        const name = Cast.toString(args.NAME)
        const value = args.VALUE
        cls.variables[name] = value
    }
    getClassVariable(args, util) {
        const cls = Cast.toClass(args.CLASS)
        const name = Cast.toString(args.NAME)
        return cls.getClassVariable(name)
    }
    deleteClassVariable(args, util) {
        const cls = Cast.toClass(args.CLASS)
        const name = Cast.toString(args.NAME)
        delete cls.variables[name]
    }
    defineStaticMethod = this._isACompiledBlock
    propertyNamesOfClass(args, util) {
        const property = args.PROPERTY
        const cls = Cast.toClass(args.CLASS)
        const [instanceMethods, staticMethods, getterMethods, setterMethods, operatorMethods, classVariables] = cls.getAllMembers()
        let values = []
        if (property === "instance method") values = instanceMethods
        else if (property === "static method") values = staticMethods
        else if (property === "getter method") values = getterMethods
        else if (property === "setter method") values = setterMethods
        else if (property === "operator method") values = operatorMethods
        else if (property === "class variable") values = classVariables
        let names = Object.keys(values)
        if (property == "instance method") {
            let index
            index = names.indexOf(CONFIG.INIT_METHOD_NAME)
            if (index !== 1) names[index] = "[special] init"
            index = names.indexOf(CONFIG.AS_STRING_METHOD_NAME)
            if (index !== 1) names[index] = "[special] as string"
        }
        else if (property === "operator method") {
            names = names.map(name => CONFIG.PUBLIC_OP_NAMES[name])
        }
        return Cast.toArray(names)
    }

    /******************** Working with Instances ********************/

    // Create & Inspect
    createInstance = this._isACompiledBlock
    isInstance(args, util) {
        const instance = Cast.toClassInstance(args.INSTANCE)
        const cls = Cast.toClass(args.CLASS)
        return Cast.toBoolean(instance.cls.isSubclassOf(cls))
    }
    getClassOfInstance(args, util) {
        const instance = Cast.toClassInstance(args.INSTANCE)
        return instance.cls
    }

    // Attributes
    setAttribute = this._isACompiledBlock
    getAttribute = this._isACompiledBlock
    getAllAttributes(args, util) {
        const instance = Cast.toClassInstance(args.INSTANCE)
        return Cast.toObject(instance.attributes)
    }

    // Call Methods
    callMethod = this._isACompiledBlock
    callStaticMethod = this._isACompiledBlock
    getStaticMethodFunc(args, util) {
        const cls = Cast.toClass(args.CLASS)
        const name = Cast.toString(args.NAME)
        return cls.getStaticMethod(name)
    }

    /******************** Functions ********************/

    // Configure Before Define
    configureNextFunctionArgs(args, util) {
        const argNames = Cast.toArray(args.ARGNAMES).array.map(name => Cast.toString(name))
        const argDefaults = Cast.toArray(args.ARGDEFAULTS).array
        if (argDefaults.length > argNames.length) {
            throw new Error("There can only be as many default values as argument names.")
        }
        util.thread.gceEnv ??= new ThreadEnvManager()
        util.thread.gceEnv.setNextFuncConfig({argNames, argDefaults})
    }

    // Define
    createFunctionAt = this._isACompiledBlock
    createFunctionNamed = this._isACompiledBlock

    // Inside Functions & Methods
    allFunctionArgs(blockArgs, util) {
        util.thread.gceEnv ??= new ThreadEnvManager()
        return Cast.toObject(util.thread.gceEnv.getArgsOrThrow())
    }
    functionArg(blockArgs, util) {
        util.thread.gceEnv ??= new ThreadEnvManager()
        const args = util.thread.gceEnv.getArgsOrThrow()
        const name = Cast.toString(blockArgs.NAME)
        if (!(name in args)) throw new Error(`Undefined function argument ${quote(name)}.`)
        return args[name]
    }
    return = this._isACompiledBlock
    transferFunctionArgsToTempVars = this._isACompiledBlock
    addTempVars() { // BUTTON
        if (!Scratch.vm.extensionManager.isExtensionLoaded("tempVars")) {
            Scratch.vm.extensionManager.loadExtensionIdSync("tempVars")
        }
    }

    // Use Functions
    callFunction = this._isACompiledBlock
    getFunction(args, util) {
        const name = Cast.toString(args.NAME)
        return this.funcVars.get(name)
    }
    functionExists(args, util) {
        const name = Cast.toString(args.NAME)
        return Cast.toBoolean(this.funcVars.has(name))
    }
    allFunctions(args, util) {
        return Cast.toArray(this.funcVars.getNames())
    }
    deleteFunction(args, util) {
        this.funcVars.delete(Cast.toString(args.NAME))
    }
    deleteAllFunctions(args, util) {
        this.funcVars.reset()
    }

    /******************** Utilities ********************/
    objectAsString = this._isACompiledBlock
    typeof(args, util) {
        const value = args.VALUE
        // My Types
        if (value instanceof BaseCallableType) return value.className // respect subclass names
        if (value instanceof ClassType) return "Class"
        if (value instanceof ClassInstanceType) return "Class Instance"
        if (value instanceof NothingType) return "Nothing"
        
        // Common/Safe JS data types
        if (value === undefined) return "JavaScript Undefined"
        if (value === null) return "JavaScript Null"
        if (typeof value === "boolean") return "Boolean"
        if (typeof value === "number") return "Number"
        if (typeof value === "string") return "String"
        
        // Foreign Extensions
        if (TypeChecker.isArray(value)) return "Array"
        if (TypeChecker.isObject(value)) return "Object"
        if (TypeChecker.isDate(value)) return "Date"
        if (TypeChecker.isSet(value)) return "Set"
        if (TypeChecker.isLambda(value)) return "Lambda"
        if (TypeChecker.isColor(value)) return "Color"
        if (TypeChecker.isUnlimitedNum(value)) return "Unlimited Number"
        if (TypeChecker.isTarget(value)) return "Target"
        if (TypeChecker.isXML(value)) return "XML"
        
        // Rare/Overlapping JS data types
        if (typeof value === "bigint") return "JavaScript BigInt"
        if (typeof value === "symbol") return "JavaScript Symbol"
        if (typeof value === "function") return "JavaScript Function"
        if (typeof value === "object") return "JavaScript Object"

        return "Unknown"
    }
    checkIdentity(args, util) {
        return Cast.toBoolean(Object.is(args.VALUE1, args.VALUE2))
    }
    nothing(args, util) {
        return Nothing
    }
    executeExpression(args, util) {
        // do nothing
    }
    
    /************************************************************************************
    *                            Implementation of Operators                            *
    ************************************************************************************/
    /**
     * @param {any} object
     * @param {Thread} thread
     * @returns {string} the return value of the as string method
     */
    *_objectAsString(object, thread) {
        if (!(object instanceof ClassInstanceType)) return object.toString()
        let method
        try {
            method = object.cls.getMemberOfType(CONFIG.AS_STRING_METHOD_NAME, "instance method")
        } catch {}
        if (!method) return object.toString()
        const output = yield* method.execute(thread, object, [])
        if (typeof output !== "string") throw new Error(`As String methods must always return a string.`)
        return output
    }

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
                return mod(left, right)
            case "op.power": return Math.pow(left, right)
        }
        return null
    }
    
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
        raiseInternal("spry-hare")
    }
    
    /**
     * @param {FunctionType} func
     * @param {Array} posargs
     * @returns {Object}
     */
    _evaluateArgs(func, posArgs) {
        const args = Object.create(null)
        let name
        let prefix

        if (func instanceof MethodType && (func.name === CONFIG.INIT_METHOD_NAME)) prefix = "initializing object"
        else if (func instanceof MethodType) prefix = `calling method ${quote(func.name)}`
        else prefix = `calling function ${quote(func.name)}`

        // Ensure there are not too many arguments
        if (posArgs.length > func.argNames.length) {
            throw new Error(`${prefix}: expected at most ${func.argNames.length}, but got ${posArgs.length} arguments.`)
        }
    
        // Count how many arguments do NOT have defaults
        const posOnlyCount = func.argNames.length - func.argDefaults.length
    
        // Ensure enough positional arguments
        if (posArgs.length < posOnlyCount) {
            throw new Error(`${prefix}: expected at least ${posOnlyCount} positional arguments, but got only ${posArgs.length}.`)
        }
    
        // Assign positional arguments
        for (let i = 0; i < posArgs.length; i++) {
            name = func.argNames[i]
            args[name] = posArgs[i]
        }
    
        // Fill in defaults for missing arguments
        const defaultsStartIndex = func.argNames.length - func.argDefaults.length
        for (let i = posArgs.length; i < func.argNames.length; i++) {
            name = func.argNames[i]
            const defaultIndex = i - defaultsStartIndex
            args[name] = func.argDefaults[defaultIndex]
        }
    
        return args
    }
}
const extensionClassInstance = new GCEClassBlocks()
Scratch.extensions.register(extensionClassInstance)
})(Scratch)

/**
 * TODO:
 * - make as string work for arrays, objects too
 * - create docs(e.g. members or configure args)
 * - option to exclude super classes when asking for members
 * - implement hover tooltips
 * - implement right-click switch options for similar blocks
 * - name of class/function block
 * - inline todos
 * 
 * ON RELEASE:
 * - set CONFIG.HIDE_ARGUMENT_DEFAULTS to false
 */
