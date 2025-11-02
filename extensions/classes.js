// Name: Classes
// ID: gceClasses
// Description: Python-like classes and OOP
// By: GermanCodeEngineer <https://github.com/GermanCodeEngineer/>
// License: MIT
// Requires and automatically adds jwArray and dogeiscutObject
// Credit: Inspired by & Based on
//  - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jg_scripts/index.js
//  - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jwArray/index.js
//  - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jwLambda/index.js
//  - https://github.com/PenguinMod/PenguinMod-ExtensionsGallery/blob/main/static/extensions/DogeisCut/dogeiscutObject.js
//  - https://github.com/PenguinMod/PenguinMod-ExtensionsGallery/blob/main/static/extensions/VeryGoodScratcher42/More-Types.js


(function(Scratch) {
"use strict"

if (!Scratch.extensions.unsandboxed) {
    throw new Error("Classes Extension must run unsandboxed.")
}

/************************************************************************************
*                                Custom Block Shapes                                *
************************************************************************************/

const CUSTOM_SHAPE_DOUBLE_PLUS = {
    emptyInputPath: "m 6 3 a 3 3 0 0 1 3 -3 h 7 h 10 h 7 a 3 3 0 0 1 3 3 a 3 3 0 0 0 3 3 a 3 3 0 0 1 3 3 v 1 a 3 3 0 0 1 -3 3 a 3 3 0 0 0 -3 3 a 3 3 0 0 0 3 3 a 3 3 0 0 1 3 3 v 1 a 3 3 0 0 1 -3 3 a 3 3 0 0 0 -3 3 a 3 3 0 0 1 -3 3 h -7 h -10 h -7 a 3 3 0 0 1 -3 -3 a 3 3 0 0 0 -3 -3 a 3 3 0 0 1 -3 -3 v -1 a 3 3 0 0 1 3 -3 a 3 3 0 0 0 3 -3 a 3 3 0 0 0 -3 -3 a 3 3 0 0 1 -3 -3 v -1 a 3 3 0 0 1 3 -3 a 3 3 0 0 0 3 -3",
    emptyInputWidth: 10 * ScratchBlocks.BlockSvg.GRID_UNIT,
    leftPath: (block) => {
        const block_height = block.height
        const emptyHeight = 32
        const fifth = (block_height - emptyHeight) / 5
        const fifthLine = `v -${fifth}`
        const fifthLineExtended = `v -${fifth + 1}`
        return [ 
            "h -7 "+
            "a 3 3 0 0 1 -3 -3 "+
            fifthLine+
            "a 3 3 0 0 0 -3 -3 "+
            "a 3 3 0 0 1 -3 -3 "+
            fifthLineExtended+
            "a 3 3 0 0 1 3 -3 "+
            "a 3 3 0 0 0 3 -3 "+
            fifthLine+
            "a 3 3 0 0 0 -3 -3 "+
            "a 3 3 0 0 1 -3 -3 "+
            fifthLineExtended+
            "a 3 3 0 0 1 3 -3 "+
            "a 3 3 0 0 0 3 -3 "+
            fifthLine+
            "a 3 3 0 0 1 3 -3 "+
            "h 7 "
        ]
    },
    rightPath: (block) => {
        const block_height = block.edgeShapeWidth_ * 2 // block.height not available
        const emptyHeight = 32
        const fifth = (block_height - emptyHeight) / 5
        const fifthLine = `v ${fifth}`
        const fifthLineExtended = `v ${fifth + 1}`
        return [ 
            "h 7 "+
            "a 3 3 0 0 1 3 3 "+
            fifthLine+
            "a 3 3 0 0 0 3 3 "+
            "a 3 3 0 0 1 3 3 "+
            fifthLineExtended+
            "a 3 3 0 0 1 -3 3 "+
            "a 3 3 0 0 0 -3 3 "+
            fifthLine+
            "a 3 3 0 0 0 3 3 "+
            "a 3 3 0 0 1 3 3 "+
            fifthLineExtended+
            "a 3 3 0 0 1 -3 3 "+
            "a 3 3 0 0 0 -3 3 "+
            fifthLine+
            "a 3 3 0 0 1 -3 3 "+
            "h -7 "
        ]
    },
}

/************************************************************************************
*                            Internal Types and Constants                           *
************************************************************************************/

function quote(s) {
    if (!s.includes('"')) return `'${s}'`
    if (!s.includes("'")) return `"${s}"`
    return `'${s.replaceAll("'", "\\'")}'`
}
function safeSpan(text) {
    text = text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;")
    let element = document.createElement("span")
    element.innerHTML = text
    element.style.display = "hidden"
    //element.style.whiteSpace = "nowrap"
    element.style.width = "100%"
    element.style.textAlign = "center"
    return element
}

class VariableManager {
    constructor() {
        this.reset()
    }
    reset() {
        this.variables = {}
    }
    set(name, value) {
        this.variables[name] = value
    }
    delete(name) {
        if (this.has(name)) {
            this.variables[name]
        }
    }
    has(name) {
        return name in this.variables
    }
    get(name) {
        if (!this.has(name)) {
            throw new Error(`${quote(name)} is not defined.`)
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
    static FUNCTION = "FUNCTION"
    static METHOD = "METHOD"
    static CLASS_DEF = "CLASS_DEF"
    
    constructor() {
        this.environments = []
        this.setNextFuncConfig()
    }
    
    enterFunction(args) {
        this.environments.splice(0, 0, {type: ThreadEnvManager.FUNCTION, args})
        console.log("enterFunction", JSON.stringify(this.environments))
        return this
    }
    enterMethod(self, args) {
        this.environments.splice(0, 0, {type: ThreadEnvManager.METHOD, self, args})
        console.log("enterMethod", JSON.stringify(this.environments))
        return this
    }
    enterClassDef(cls) {
        this.environments.splice(0, 0, {type: ThreadEnvManager.CLASS_DEF, cls})
        console.log("enterClassDef", JSON.stringify(this.environments))
        return this
    }
    
    _getEnv(allowedTypes) {
        for (let i = 0; i < this.environments.length; i++) {
            if (this.environments[i].type in allowedTypes) return this.environments[i]
        }
        return null
    }
    
    getArgsOrThrow() {
        console.log("getArgs", JSON.stringify(this.environments))
        const env = this._getEnv([ThreadEnvManager.FUNCTION, ThreadEnvManager.METHOD])
        if (!env) {
            throw new Error("Function arguments can only be used within a function or method.")
        }
        return env.args
    }
    getSelfOrThrow() {
        console.log("getSelf", JSON.stringify(this.environments))
        const env = this._getEnv([ThreadEnvManager.METHOD])
        if (!env) {
            throw new Error("'self' can only be used within a method.")
        }
        return env.self
    }
    getClsOrThrow() {
        console.log("getCls", JSON.stringify(ThreadEnvManager.environments))
        const topEnv = this.environments[0]
        if (!topEnv || (topEnv.type !== ThreadEnvManager.CLASS_DEF)) {
            throw new Error("'define method' can only be used within a class definition or 'on class' block.")
        }
        return topEnv.cls
    }
    
    prepareReturn() {
        const topEnv = this.environments[0]
        if (!topEnv || !(topEnv.type in [ThreadEnvManager.FUNCTION, ThreadEnvManager.METHOD])) {
            throw new Error("'return' can only be used within a function or method.")
        }
        this.environments.shift()
        console.log("perpareReturn", JSON.stringify(this.environments))
    }
    exitClassDef() {
        const topEnv = this.environments[0]
        if (!topEnv || (topEnv.type !== ThreadEnvManager.CLASS_DEF)) {
            throw new Error("An internal error occured in the classes extension. Please report it.")
        }
        this.environments.shift()
        console.log("exitClassDef", JSON.stringify(this.environments))
    }
    
    getSize() {
        return this.environments.length
    }
    setSize(size) {
        this.environments = this.environments.slice(-size)
    }
    
    setNextFuncConfig(config = {argNames: [], argDefaults: []}) {
        this.nextFuncConfig = config
        console.log("setNextFuncConfig", JSON.stringify(this.environments))
    }
    getAndResetNextFuncConfig() {
        const config = this.nextFuncConfig
        this.setNextFuncConfig()
        console.log("getAndResetNextFuncConfig", JSON.stringify(this.environments), config)
        return config
    }
}

const {BlockType, BlockShape, ArgumentType} = Scratch
const runtime = Scratch.vm.runtime

const CONFIG = {
    INIT_METHOD_NAME: "__init__",
    HIDE_ARGUMENT_DEFAULTS: false, // TODO: change to false on release
}

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
    static toArray(value) {
        if (!Scratch.vm.jwArray) throw new Error("Array extension was not loaded properly.")
        return Scratch.vm.jwArray.Type.toArray(value)
    }
    
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
        return safeSpan(this.toString())
    }
}

class FunctionType extends CustomType {
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
        return `<Function ${quote(this.name)}>`
    }
    toJSON() {
        return "Functions can not be serialized."
    }

    /**
     * @param {Thread} thread 
     * @param {array} posArgs
     * @returns {any} the return value of the function
     */
    *execute(thread, posArgs) {
        const args = extensionClassInstance._evaluateArgs(this, posArgs)
        thread.gceEnv ??= new ThreadEnvManager()
        //const size = thread.gceEnv.getSize()
        thread.gceEnv.enterFunction(args)
        const output = (yield* this.jsFunc(thread))
        //thread.gceEnv.setSize(size)
        return output
    }
}

class MethodType extends FunctionType {
    toString() {
        return `<Method ${quote(this.name)}>`
    }
    toJSON() {
        return "Methods can not be serialized."
    }

    /**
     * @param {Thread} thread 
     * @param {ClassInstanceType} instance
     * @param {array} posArgs
     * @returns {any} the return value of the method
     */
    *execute(thread, instance, posArgs) {
        const args = extensionClassInstance._evaluateArgs(this, posArgs)
        thread.gceEnv ??= new ThreadEnvManager()
        //const size = thread.gceEnv.getSize()
        thread.gceEnv.enterMethod(instance, args)
        const output = (yield* this.jsFunc(thread))
        //thread.gceEnv.setSize(size)
        return output
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
        this.methods = {}
        this.superCls = superCls
        if (!superCls) {
            const func = function* () {return Nothing}
            this.methods[CONFIG.INIT_METHOD_NAME] = new MethodType(CONFIG.INIT_METHOD_NAME, func, [], [])
        }
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
     * @param {boolean} strict
     * @returns {?MethodType}
     */
    getMethod(name, strict) {
        let currentCls = this
        while (currentCls) {
            if (name in currentCls.methods) return currentCls.methods[name]
            currentCls = currentCls.superCls
        }
        if (strict) throw new Error(`Undefined method ${quote(name)}.`)
        else return null
    }
    /**
     * @param {Thread} thread 
     * @param {array} posArgs
     * @returns {ClassInstanceType} the instance
     */
    *createInstance(thread, posArgs) {
        const instance = new ClassInstanceType(this) 
        yield* instance.executeMethod(thread, CONFIG.INIT_METHOD_NAME, posArgs) // an init method always exists
        return instance
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
    // TODO: possibly define toReporterContent for better visualization

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {array} posArgs
     * @returns {any} the return value of the method
     */
     *executeMethod(thread, name, posArgs) {
        const method = this.cls.getMethod(name, true)
        return yield* method.execute(thread, this, posArgs)
    }
}

class NothingType extends CustomType {
    customId = "gceNothing"

    toString() {
        return "<Nothing>"
    }
    toJSON() {
        return {"gceNothing": true} // Just for debugging, not actually used anywhere
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
        blockShape: "gceClasses-doublePlus",
        forceOutputType: "gceClassInstance",
        disableMonitor: true,
    },
    Argument: {
        shape: "gceClasses-doublePlus",
        exemptFromNormalization: true,
        check: ["gceClassInstance", "dogeiscutObject"],
    },
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
    funcName: {
        type: ArgumentType.STRING,
        defaultValue: "Function1",
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
            id: "gceClasses",
            name: "Classes",
            color1: "#428af5ff",
            menuIconURI: "data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHdpZHRoPSIyMCIgaGVpZ2h0PSIyNC4xNjc5MiIgdmlld0JveD0iMCwwLDIwLDI0LjE2NzkyIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMjMwLC0xNjcuMzIwODgpIj48ZyBzdHJva2UtbWl0ZXJsaW1pdD0iMTAiPjxwYXRoIGQ9Ik0yMzEsMTgwYzAsLTQuOTcwNTYgNC4wMjk0NCwtOSA5LC05YzQuOTcwNTYsMCA5LDQuMDI5NDQgOSw5YzAsNC45NzA1NiAtNC4wMjk0NCw5IC05LDljLTQuOTcwNTYsMCAtOSwtNC4wMjk0NCAtOSwtOXoiIGZpbGw9IiM0MjhhZjUiIHN0cm9rZT0iIzJiNTg5ZCIgc3Ryb2tlLXdpZHRoPSIyIi8+PHRleHQgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjMyLjc1MTAyLDE4Ni4wOTQxNykgc2NhbGUoMC4yNTgxNiwwLjQzMTU3KSIgZm9udC1zaXplPSI0MCIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIgZmlsbD0iI2ZmZmZmZiIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjEiIGZvbnQtZmFtaWx5PSJTYW5zIFNlcmlmIiBmb250LXdlaWdodD0ibm9ybWFsIiB0ZXh0LWFuY2hvcj0ic3RhcnQiPjx0c3BhbiB4PSIwIiBkeT0iMCI+Jmx0OyAmZ3Q7PC90c3Bhbj48L3RleHQ+PC9nPjwvZz48L3N2Zz48IS0tcm90YXRpb25DZW50ZXI6MTA6MTIuNjc5MTI0MjQ5Mjk4MDQyLS0+",
            blocks: [
                makeLabel("Classes"),
                {
                    opcode: "createClassAt",
                    blockType: BlockType.CONDITIONAL,
                    text: ["create class at [NAME]"],
                    branchCount: 1,
                    arguments: {
                        NAME: commonArguments.classVarName,
                    },
                },
                {
                    opcode: "createSubclassAt",
                    blockType: BlockType.CONDITIONAL,
                    text: ["create subclass at [NAME] with superclass [SUPERCLASS]"],
                    branchCount: 1,
                    arguments: {
                        NAME: {...commonArguments.classVarName, defaultValue: "MySubclass"},
                        SUPERCLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "createClassNamed",
                    text: ["create class named [NAME]"],
                    branchCount: 1,
                    arguments: {
                        NAME: commonArguments.classVarName,
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "createSubclassNamed",
                    text: ["create subclass named [NAME] with superclass [SUPERCLASS]"],
                    branchCount: 1,
                    arguments: {
                        NAME: {...commonArguments.classVarName, defaultValue: "MySubclass"},
                        SUPERCLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                {
                    opcode: "setClass",
                    blockType: BlockType.COMMAND,
                    text: "set class [NAME] to [CLASS]",
                    arguments: {
                        NAME: commonArguments.classVarName,
                        CLASS: gceClass.Argument,
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "getClass",
                    text: "get class [NAME]",
                    arguments: {
                        NAME: commonArguments.classVarName,
                    },
                },
                {
                    opcode: "classExists",
                    blockType: BlockType.BOOLEAN,
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
                    opcode: "deleteClass",
                    blockType: BlockType.COMMAND,
                    text: "delete class [NAME]",
                    arguments: {
                        NAME: commonArguments.classVarName,
                    },
                },
                {
                    opcode: "deleteAllClasses",
                    blockType: BlockType.COMMAND,
                    text: "delete all classes"
                },
                {
                    opcode: "isSubclass",
                    blockType: BlockType.BOOLEAN,
                    text: "is [SUBCLASS] a subclass of [SUPERCLASS] ?",
                    arguments: {
                        SUBCLASS: gceClass.ArgumentClassOrVarName,
                        SUPERCLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                "---",
                makeLabel("Functions & Methods"),
                {
                    opcode: "configureNextFunctionArgs",
                    blockType: BlockType.COMMAND,
                    text: "configure next function: argument names [ARGNAMES] defaults [ARGDEFAULTS]",
                    arguments: {
                        ARGNAMES: jwArrayStub.Argument,
                        ARGDEFAULTS: jwArrayStub.Argument,
                    },
                },
                {
                    opcode: "createFunctionAt",
                    blockType: BlockType.CONDITIONAL,
                    text: ["create function at [NAME]"],
                    branchCount: 1,
                    arguments: {
                        NAME: commonArguments.funcName,
                    },
                },
                {
                    ...gceFunction.Block,
                    opcode: "createFunctionNamed",
                    text: ["create function named [NAME]"],
                    branchCount: 1,
                    arguments: {
                        NAME: commonArguments.funcName,
                    },
                },
                {
                    ...dogeiscutObjectStub.Block,
                    opcode: "allFunctionArgs",
                    text: "function arguments",
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "functionArg",
                    text: "function arg [NAME]",
                    arguments: {
                        NAME: commonArguments.argumentName,
                    },
                },
                {
                    opcode: "return",
                    text: "return [VALUE]",
                    blockType: BlockType.COMMAND,
                    isTerminal: true,
                    arguments: {
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    opcode: "callFunction",
                    text: "call function [FUNC] with positional args [POSARGS]",
                    blockType: BlockType.REPORTER,
                    arguments: {
                        FUNC: gceFunction.ArgumentFunctionOrVarName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                { // BUTTON
                    opcode: "addTempVars",
                    blockType: BlockType.BUTTON,
                    text: "add temporary variables extension",
                },
                {
                    opcode: "transferFunctionArgsToTempVars",
                    blockType: BlockType.COMMAND,
                    text: "transfer arguments to temporary variables",
                },
                "---",
                {
                    opcode: "defineMethod",
                    blockType: BlockType.CONDITIONAL,
                    text: ["define method [NAME]"],
                    branchCount: 1,
                    arguments: {
                        NAME: commonArguments.methodName,
                    },
                },
                {
                    opcode: "defineInitMethod",
                    blockType: BlockType.CONDITIONAL,
                    text: ["define init method"],
                    branchCount: 1,
                },
                {
                    ...gceClassInstance.Block,
                    opcode: "self",
                    text: "self",
                },
                "---",
                makeLabel("Instances"),
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
                    opcode: "setAttribute",
                    blockType: BlockType.COMMAND,
                    text: "on [INSTANCE] set attribute [NAME] to [VALUE]",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                        NAME: {type: ArgumentType.STRING, defaultValue: "myAttr"},
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "getAttribute",
                    text: "get attribute [NAME] of [INSTANCE]",
                    arguments: {
                        NAME: {type: ArgumentType.STRING, defaultValue: "myAttr"},
                        INSTANCE: gceClassInstance.Argument,
                    },
                },
                {
                    opcode: "callMethod",
                    blockType: BlockType.REPORTER,
                    text: "on [INSTANCE] call method [NAME] with positional args [POSARGS]",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                        NAME: commonArguments.methodName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                {
                    opcode: "isInstance",
                    blockType: BlockType.BOOLEAN,
                    text: "is [INSTANCE] an instance of [CLASS] ?",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                        CLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                "---",
                makeLabel("Miscellaneous"),
                {
                    opcode: "typeof",
                    text: "typeof [VALUE]",
                    blockType: BlockType.REPORTER,
                    arguments: {
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    opcode: "checkIdentity",
                    text: "[VALUE1] is [VALUE2] ?",
                    blockType: BlockType.BOOLEAN,
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
                "---",
                makeLabel("Debugging & Temporary"),
                {
                    ...dogeiscutObjectStub.Block,
                    opcode: "jsTypeof",
                    text: "debugging: JS typeof [VALUE]",
                    arguments: {
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    opcode: "throw",
                    blockType: BlockType.COMMAND,
                    text: "debugging: throw",
                },
                {
                    opcode: "logThread",
                    blockType: BlockType.COMMAND,
                    text: "debugging: log thread",
                },
            ],
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
        return {
            ir: {
                createFunctionAt: (generator, block) => ({
                    kind: "stack",
                    name: generator.descendInputOfBlock(block, "NAME"),
                    funcStack: generator.descendSubstack(block, "SUBSTACK"),
                }),
                createFunctionNamed: (generator, block) => ({
                    kind: "input",
                    name: generator.descendInputOfBlock(block, "NAME"),
                    funcStack: generator.descendSubstack(block, "SUBSTACK"),
                }),
                return: (generator, block) => ({
                    kind: "stack",
                    value: generator.descendInputOfBlock(block, "VALUE"),
                }),
                callFunction: (generator, block) => (generator.script.yields = true, {
                    kind: "input",
                    func: generator.descendInputOfBlock(block, "FUNC"),
                    posArgs: generator.descendInputOfBlock(block, "POSARGS"),
                }),
                transferFunctionArgsToTempVars: (generator, block) => ({kind: "stack"}),
                defineMethod: (generator, block) => ({
                    kind: "stack",
                    name: generator.descendInputOfBlock(block, "NAME"),
                    funcStack: generator.descendSubstack(block, "SUBSTACK"),
                }),
                defineInitMethod: (generator, block) => ({
                    kind: "stack",
                    funcStack: generator.descendSubstack(block, "SUBSTACK"),
                }),
                createInstance: (generator, block) => ({
                    kind: "input",
                    cls: generator.descendInputOfBlock(block, "CLASS"),
                    posArgs: generator.descendInputOfBlock(block, "POSARGS"),
                }),
                callMethod: (generator, block) => ({
                    kind: "input",
                    instance: generator.descendInputOfBlock(block, "INSTANCE"),
                    name: generator.descendInputOfBlock(block, "NAME"),
                    posArgs: generator.descendInputOfBlock(block, "POSARGS"),
                }),
            },
            js: {
                // Blocks: Functions & Methods
                createFunctionAt: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.name).asString()
                    const nameLocal = compiler.localVariables.next()
                    
                    compiler.source += "thread.gceEnv ??= new runtime.ext_gceClasses.environment.ThreadEnvManager();"+
                        `const ${nameLocal} = ${nameCode};`+
                        `runtime.ext_gceClasses.funcVars.set(${nameLocal}, new runtime.ext_gceClasses.environment.FunctionType(${nameLocal}, function* (thread) {`
                    compiler.descendStack(node.funcStack, new imports.Frame(false, undefined, true))
                    compiler.source += "thread.gceEnv.prepareReturn();"+
                        "return runtime.ext_gceClasses.environment.Nothing;"+
                        "}, thread.gceEnv.getAndResetNextFuncConfig()));\n"
                },
                createFunctionNamed: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.name).asString()
                    
                    const oldSource = compiler.source
                    compiler.source = "(thread.gceEnv ??= new runtime.ext_gceClasses.environment.ThreadEnvManager(), "+
                        `new runtime.ext_gceClasses.environment.FunctionType(${nameCode}, function* (thread) {`
                    compiler.descendStack(node.funcStack, new imports.Frame(false, undefined, true))
                    compiler.source += "thread.gceEnv.prepareReturn();"+
                        "return runtime.ext_gceClasses.environment.Nothing;"+
                        "}, thread.gceEnv.getAndResetNextFuncConfig()));\n"
                    
                    const generatedCode = compiler.source
                    compiler.source = oldSource
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
                return: (node, compiler, imports) => {
                    compiler.source += "thread.gceEnv ??= new runtime.ext_gceClasses.environment.ThreadEnvManager();"+
                        "thread.gceEnv.prepareReturn();"+
                        `return ${compiler.descendInput(node.value).asUnknown()};\n`
                },
                callFunction: (node, compiler, imports) => {
                    const funcCode = compiler.descendInput(node.func).asUnknown()
                    const posArgsCode = compiler.descendInput(node.posArgs).asUnknown()
                    const generatedCode = `(yield* runtime.ext_gceClasses.Cast.toFunction(${funcCode})`+
                        `.execute(thread, runtime.ext_gceClasses.Cast.toArray(${posArgsCode}).array))`
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
                transferFunctionArgsToTempVars: (node, compiler, imports) => {
                    // tempVars seems to always be defined
                    compiler.source += "try {tempVars} catch {throw new Error("+
                        '"Failed to transfer to temporary variables.")};'+
                        "thread.gceEnv ??= new runtime.ext_gceClasses.environment.ThreadEnvManager();"+
                        "Object.assign(tempVars, thread.gceEnv.getArgsOrThrow());\n"
                        
                },
                defineMethod: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.name).asString()
                    const nameLocal = compiler.localVariables.next()
                    
                    compiler.source += "thread.gceEnv ??= new runtime.ext_gceClasses.environment.ThreadEnvManager();"+
                        `const ${nameLocal} = ${nameCode};`+
                        `thread.gceEnv.getClsOrThrow().methods[${nameLocal}] = new runtime.ext_gceClasses.environment.MethodType(${nameLocal}, function* (thread) {\n`
                    compiler.descendStack(node.funcStack, new imports.Frame(false, undefined, true))
                    compiler.source += "thread.gceEnv.prepareReturn();"+
                         "return runtime.ext_gceClasses.environment.Nothing;"+
                        "}, thread.gceEnv.getAndResetNextFuncConfig()));\n"
                },
                defineInitMethod: (node, compiler, imports) => {
                    const nameCode = quote(CONFIG.INIT_METHOD_NAME)

                    compiler.source += "thread.gceEnv ??= new runtime.ext_gceClasses.environment.ThreadEnvManager();"+
                        `thread.gceEnv.getClsOrThrow().methods[${nameCodel}] = new runtime.ext_gceClasses.environment.MethodType(${nameLocal}, function* (thread) {\n`
                    compiler.descendStack(node.funcStack, new imports.Frame(false, undefined, true))
                    compiler.source += "thread.gceEnv.prepareReturn();"+
                         "return runtime.ext_gceClasses.environment.Nothing;"+
                        "}, thread.gceEnv.getAndResetNextFuncConfig()));\n"
                },
                // Blocks: Functions & Methods
                createInstance: (node, compiler, imports) => {
                    const classCode = compiler.descendInput(node.cls).asUnknown()
                    const posArgsCode = compiler.descendInput(node.posArgs).asUnknown()
                    const generatedCode = `(yield* runtime.ext_gceClasses.Cast.toClass(${classCode})`+
                        `.createInstance(thread, runtime.ext_gceClasses.Cast.toArray(${posArgsCode}).array))`
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
                callMethod: (node, compiler, imports) => {
                    const instanceCode = compiler.descendInput(node.instance).asUnknown()
                    const nameCode = compiler.descendInput(node.name).asUnknown()
                    const posArgsCode = compiler.descendInput(node.posArgs).asUnknown()
                    const generatedCode = `(yield* runtime.ext_gceClasses.Cast.toClassInstance(${instanceCode})`+
                        `.executeMethod(thread, ${nameCode}, runtime.ext_gceClasses.Cast.toArray(${posArgsCode}).array))`
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
            VariableManager, SpecialBlockStorageManager, ThreadEnvManager, TypeChecker, Cast,
            CustomType, FunctionType, MethodType, ClassType, ClassInstanceType, NothingType, Nothing,
            gceFunction, gceMethod, gceClass, gceClassInstance, gceNothing,
        }
        
        runtime.registerCompiledExtensionBlocks("gceClasses", this.getCompileInfo())
        runtime.registerSerializer(
            "gceNothing",
            v => (v instanceof NothingType ? v.toJSON() : null),
            v => Nothing,
        )
        Scratch.gui.getBlockly().then(ScratchBlocks => {
            ScratchBlocks.BlockSvg.registerCustomShape("gceClasses-doublePlus", CUSTOM_SHAPE_DOUBLE_PLUS)
        })

        // wrap Scratch.Cast.toBoolean to return false for Nothing
        const oldToBoolean = Scratch.Cast.toBoolean
        Scratch.Cast.toBoolean = function modifiedToBoolean(value) {
            if (value instanceof NothingType) return false
            return oldToBoolean(value)
        }

        this.classVars = new VariableManager()
        this.funcVars = new VariableManager()
        this.specialBlockStorage = new SpecialBlockStorageManager()
        
        runtime.on("THREAD_FINISHED", (thread) => {this.specialBlockStorage.deleteThreadStorage(thread)})
    }    
    
    /************************************************************************************
    *                                       Blocks                                      *
    ************************************************************************************/

    // Blocks: Classes

    createClassAt(args, util) { // WARNING: reran (contains function execution)
        const name = Cast.toString(args.NAME)
        const {isDone, cls} = this._createClass(util, name, null)
        if (isDone) this.classVars.set(name, cls)
    }

    createSubclassAt(args, util) { // WARNING: reran (contains function execution)
        const name = Cast.toString(args.NAME)
        const superCls = Cast.toClass(args.SUPERCLASS)
        const {isDone, cls} = this._createClass(util, name, superCls)
        if (isDone) this.classVars.set(name, cls)
    }
    
    createClassNamed(args, util) { // WARNING: reran (contains function execution)
        const name = Cast.toString(args.NAME)
        const {isDone, cls} = this._createClass(util, name, null)
        if (isDone) return cls
    }

    createSubclassNamed(args, util) { // WARNING: reran (contains function execution)
        const name = Cast.toString(args.NAME)
        const superCls = Cast.toClass(args.SUPERCLASS)
        const {isDone, cls} = this._createClass(util, name, superCls)
        if (isDone) return cls
    }
    
    setClass(args, util) {
        const name = Cast.toString(args.NAME)
        const cls = args.CLASS
        if (!(cls instanceof ClassType)) {
            throw new Error("Class argument of 'set class' must be a class.")
        }
        this.classVars.set(name, cls)
    }
    
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

    // Blocks: Functions & Methods

    configureNextFunctionArgs(args, util) {
        const argNames = Cast.toArray(args.ARGNAMES).array.map(name => Cast.toString(name))
        const argDefaults = Cast.toArray(args.ARGDEFAULTS).array.map(val => Cast.toString(val))
        if (argDefaults.length > argNames.length) {
            throw new Error("There can only be as many default values as argument names.")
        }
        util.thread.gceEnv ??= new ThreadEnvManager()
        util.thread.gceEnv.setNextFuncConfig({argNames, argDefaults})
    }

    createFunctionAt = this._isACompiledBlock
    createClassNamed = this._isACompiledBlock

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
    callFunction = this._isACompiledBlock

    addTempVars() { // BUTTON
        if (!Scratch.vm.extensionManager.isExtensionLoaded("tempVars")) {
            Scratch.vm.extensionManager.loadExtensionIdSync("tempVars")
        }
    }

    transferFunctionArgsToTempVars = this._isACompiledBlock
    defineMethod = this._isACompiledBlock
    defineInitMethod = this._isACompiledBlock
    
    self(args, util) {
        util.thread.gceEnv ??= new ThreadEnvManager()
        return util.thread.gceEnv.getSelfOrThrow()
    }

    // Block: Instances

    createInstance = this._isACompiledBlock
    
    setAttribute(args, util) {
        const instance = args.INSTANCE
        if (!(instance instanceof ClassInstanceType)) {
            throw new Error("Instance argument of 'set attribute' must be a class instance.")
        }
        const name = Cast.toString(args.NAME)
        const value = args.VALUE
        instance.attributes[name] = value
    }
    
    getAttribute(args, util) {
        const instance = args.INSTANCE
        if (!(instance instanceof ClassInstanceType)) {
            throw new Error("Instance argument of 'get attribute' must be a class instance.")
        }
        const name = Cast.toString(args.NAME)
        if (!(name in instance.attributes)) {
            throw new Error(`${instance} has no attribute ${quote(name)}.`)
        }
        return instance.attributes[name]
    }

    callMethod = this._isACompiledBlock

    isInstance(args, util) {
        const instance = args.INSTANCE
        if (!(instance instanceof ClassInstanceType)) {
            throw new Error("Instance argument of 'is instance' must be a class instance.")
        }
        const cls = Cast.toClass(args.CLASS)
        return Cast.toBoolean(instance.cls.isSubclassOf(cls))
    }
    
    // Blocks: Miscellaneous
    typeof(args, util) {
        const value = args.VALUE
        // My Types
        if (value instanceof FunctionType) return "Function"
        if (value instanceof MethodType) return "Method"
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
    
    nothing(args, util) {
        return Nothing
    }

    checkIdentity(args, util) {
        return Cast.toBoolean(Object.is(args.VALUE1, args.VALUE2))
    }

    // Blocks: Temporary

    jsTypeof(args, util) {
        console.log("value", args.VALUE)
        console.log("typeof value", typeof args.VALUE)
        return Cast.toObject({
            typeof: typeof args.VALUE, 
            proto: Object.getPrototypeOf(args.VALUE),
        })
    }

    throw () {
        throw new Error("BREAK")
    }

    logThread(args, util) {
        console.log("logging thread", util.thread)
    }

    /************************************************************************************
    *                                      Helpers                                      *
    ************************************************************************************/

    _isACompiledBlock() {
        throw new Error("Please activate the compiler.")
    }

    /**
     * @param {BlockUtility} util
     * @param {string} name
     * @param {ClassType} superCls
     * @returns {{isDone: boolean, cls: ClassType}}
     */
    _createClass(util, name, superCls) { // WARNING: reran (contains function execution)
        const ownThread = util.thread
        const ownBlockId = ownThread.peekStack()
        let blockStorage = this.specialBlockStorage.getBlockData(ownBlockId, ownThread) 
        
        if (!blockStorage) {
            blockStorage = {cls: new ClassType(name, superCls)}
            this.specialBlockStorage.storeBlockData(ownBlockId, ownThread, blockStorage)
        }
        
        const isDone = this._runBranchInClassContext(util, 1, blockStorage.cls)
        return {isDone, cls: blockStorage.cls}
    }

    /**
     * WARNING: makes the block caling this run MULITPLE times on one activation
     * @param {BlockUtility} util
     * @param {number} branchNumber
     * @param {?ClassType} cls
     * @returns {boolean} if the branch is done
     */
    _runBranchInClassContext(util, branchNumber, cls) {
        // Prepare stack frame and get thread
        const branch = util.thread.blockContainer.getBranch(util.thread.peekStack(), branchNumber)
        const frame = util.stackFrame
        if (frame.JGindex === undefined) frame.JGindex = 0
        let thread = frame.JGthread
        
        // Make a thread if there is none
        if (util.target.blocks.getBlock(branch) === undefined) return true
        if (!thread && (frame.JGindex < 1)) {
            thread = runtime._pushThread(branch, util.target, {stackClick: false})
            
            thread.gceEnv ??= new ThreadEnvManager()
            thread.gceEnv.enterClassDef(cls)
            thread.target = util.target
            thread.tryCompile() // update thread
            
            frame.JGthread = thread
            frame.JGindex = 1
        }

        // Yeah thanks to JG, this section is really confusing, but it works  ¯\_(ツ)_/¯
        // Run the thread if it is active, otherwise set return value and clean up
        let isDone = false
        if (frame.JGthread && runtime.isActiveThread(frame.JGthread)) util.yield()
        else {
            isDone = true
            frame.JGthread = ""
        }
        if ((frame.JGindex < 1)) util.yield()
        return isDone
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
            throw new Error(`${prefix}: expected at most ${func.argNames.length}, but got ${posArgs.length} arguments`)
        }
    
        // Count how many arguments do NOT have defaults
        const posOnlyCount = func.argNames.length - func.argDefaults.length
    
        // Ensure enough positional arguments
        if (posArgs.length < posOnlyCount) {
            throw new Error(`${prefix}: expected at least ${posOnlyCount} positional arguments, but got only ${posArgs.length}`)
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
 * TODOS:
 * - make function, method arguments, self use a stack like jw's extension
 * - make "on class X" block
 * - more features for instances, classes and methods
 * - inline todos
 * - remove static qoutes in errors
 */

