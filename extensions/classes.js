// Name: Classes
// ID: gceClasses
// Description: Python-like classes and OOP
// By: GermanCodeEngineer <https://github.com/GermanCodeEngineer/>
// License: MIT
// Requires and automatically adds jwArray and dogeiscutObject
// Credit: Inspired by & Based on
//  - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jg_scripts/index.js
//  - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jwArray/index.js
//  - https://github.com/PenguinMod/PenguinMod-ExtensionsGallery/blob/main/static/extensions/DogeisCut/dogeiscutObject.js
//  - https://github.com/PenguinMod/PenguinMod-ExtensionsGallery/blob/main/static/extensions/VeryGoodScratcher42/More-Types.js


(function(Scratch) {
"use strict"

if (!Scratch.extensions.unsandboxed) {
    throw new Error("Classes Extension must run unsandboxed.")
}

Scratch.gui.getBlockly().then(ScratchBlocks => {
    ScratchBlocks.BlockSvg.registerCustomShape("gceClasses-doublePlus", {
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
    })
})

/************************************************************************************
*                            Internal Types and Constants                           *
************************************************************************************/

function quote(s) {
    if (!s.includes('"')) return `'${s}'`
    if (!s.includes("'")) return `"${s}"`
    return `'${s.replace("'", "\\'")}'`
}

class Script {
    /**
     * @param {string} name 
     * @param {string} branch
     * @param {Target} target 
     */
    constructor(name, branch, target) {
        this.name = name
        this.branch = branch
        this.target = target
    }
    toString() {
        return `<Script ${quote(this.name)}`
    }
    toJSON() {
        return "Scripts can not be serialized."
    }
}

class Method {
    /**
     * @param {string} name
     * @param {Script} script 
     * @param {Array<string>} argNames
     * @param {Array<string>} argDefaults
     */
    constructor(name, script, argNames, argDefaults) {
        this.name = name
        this.script = script
        this.argNames = argNames
        this.argDefaults = argDefaults
    }
    toString() {
        return `<Method ${quote(this.name)}`
    }
    toJSON() {
        return "Methods can not be serialized."
    }
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
    onThreadFinished(thread) {
        this.threads.delete(thread) // does not ever throw
    }
}

const {BlockType, BlockShape, ArgumentType} = Scratch
const runtime = Scratch.vm.runtime

const CONFIG = {
    INIT_METHOD_NAME: "__init__",
    HIDE_ARGUMENT_DEFAULTS: false, // TODO: change on release
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
        return false;
    }
    
    static isSet(value) {
        if (!Scratch.vm.dogeiscutSet) return false;
        return value instanceof Scratch.vm.dogeiscutSet.Type
    }
    
    static isLambda(value) {
        if (!Scratch.vm.jwLambda) return false;
        return value instanceof Scratch.vm.jwLambda.Type
    }
    
    static isColor(value) {
        if (!Scratch.vm.jwColor) return false;
        return value instanceof Scratch.vm.jwColor.Type
    }
    
    static isUnlimitedNum(value) {
        if (!Scratch.vm.jwNum) return false;
        return value instanceof Scratch.vm.jwNum.Type
    }

    static isTarget(value) {
        if (!Scratch.vm.jwTargets) return false;
        return value instanceof Scratch.vm.jwTargets.Type
    }
    
    static isXML(value) {
        if (!Scratch.vm.jwXML) return false;
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
    static toClass(value) {
        if (value instanceof ClassType) return value
        else if ((typeof value) === "string") return extensionClassInstance.classVars.get(value)
        else throw new Error("Expected a class or class variable name.")
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

class ClassType {
    customId = "gceClass"

    /**
     * @param {string} name
     * @param {ClassType} superCls
     */
     
    constructor(name, superCls) {
        this.name = name
        this.methods = {}
        this.superCls = superCls
    }
    toString() {
        const suffix = this.superCls ? `(super ${quote(this.superCls.name)})` : ""
        return `<Class ${quote(this.name)}${suffix}>`
    }
    toJSON() {
        return "Classes can not be serialized."
    }
    toMonitorContent() {
        return this.toString()
    }
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

class ClassInstanceType {
    customId = "gceClassInstance"

    /**
     * @param {ClassType} cls 
     */
    constructor(cls) {
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
    toMonitorContent() {
        return this.toString()
    }
    // TODO: define toReporterContent for better visualization???
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
        check: ["gceClassInstance"],
    },
}

class NothingType {
    customId = "gceNothing"

    constructor() {}
    toString() {
        return "<Nothing>"
    }
    toJSON() {
        return {"gceNothing": true}
    }
    toMonitorContent() {
        return this.toString()
    }
    // TODO: add monitor content method to all
}
const Nothing = new NothingType()

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
    scriptName: {
        type: ArgumentType.STRING,
        defaultValue: "Script1",
    },
    anything: {
        type: ArgumentType.STRING,
        defaultValue: "", 
        exemptFromNormalization: true,
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
        let info = {
            id: "gceClasses",
            name: "Classes",
            color1: "#428af5ff", // leftof; consider jwtarget color
            //blockText: "#ffffff",
            menuIconURI: "data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHdpZHRoPSIyMCIgaGVpZ2h0PSIyNC4xNjc5MiIgdmlld0JveD0iMCwwLDIwLDI0LjE2NzkyIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMjMwLC0xNjcuMzIwODgpIj48ZyBzdHJva2UtbWl0ZXJsaW1pdD0iMTAiPjxwYXRoIGQ9Ik0yMzEsMTgwYzAsLTQuOTcwNTYgNC4wMjk0NCwtOSA5LC05YzQuOTcwNTYsMCA5LDQuMDI5NDQgOSw5YzAsNC45NzA1NiAtNC4wMjk0NCw5IC05LDljLTQuOTcwNTYsMCAtOSwtNC4wMjk0NCAtOSwtOXoiIGZpbGw9IiM0MjhhZjUiIHN0cm9rZT0iIzJiNTg5ZCIgc3Ryb2tlLXdpZHRoPSIyIi8+PHRleHQgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjMyLjc1MTAyLDE4Ni4wOTQxNykgc2NhbGUoMC4yNTgxNiwwLjQzMTU3KSIgZm9udC1zaXplPSI0MCIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIgZmlsbD0iI2ZmZmZmZiIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjEiIGZvbnQtZmFtaWx5PSJTYW5zIFNlcmlmIiBmb250LXdlaWdodD0ibm9ybWFsIiB0ZXh0LWFuY2hvcj0ic3RhcnQiPjx0c3BhbiB4PSIwIiBkeT0iMCI+Jmx0OyAmZ3Q7PC90c3Bhbj48L3RleHQ+PC9nPjwvZz48L3N2Zz48IS0tcm90YXRpb25DZW50ZXI6MTA6MTIuNjc5MTI0MjQ5Mjk4MDQyLS0+",
            blocks: [
                makeLabel("Classes"),
                {
                    opcode: "createClass",
                    blockType: BlockType.CONDITIONAL,
                    text: ["create class [NAME]"],
                    branchCount: 1,
                    arguments: {
                        NAME: commonArguments.classVarName,
                    },
                },
                {
                    opcode: "createSubclass",
                    blockType: BlockType.CONDITIONAL,
                    text: ["create subclass [NAME] with superclass [SUPERCLASS]"],
                    branchCount: 1,
                    arguments: {
                        NAME: commonArguments.classVarName,
                        SUPERCLASS: {...gceClass.ArgumentClassOrVarName, defaultValue: "MySuperClass"},
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "setClass",
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
                makeLabel("Methods"),
                {
                    opcode: "configureNextMethodArguments",
                    blockType: BlockType.COMMAND,
                    text: "configure next method with argument names [ARGNAMES] defaults [ARGDEFAULTS]",
                    arguments: {
                        ARGNAMES: jwArrayStub.Argument,
                        ARGDEFAULTS: jwArrayStub.Argument,
                    },
                },
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
                    opcode: "return",
                    text: "return [VALUE]",
                    blockType: BlockType.COMMAND,
                    isTerminal: true,
                    arguments: {
                        VALUE: commonArguments.anything,
                    },
                },
                {
                    ...gceClassInstance.Block,
                    opcode: "self",
                    text: "self",
                },
                {
                    ...dogeiscutObjectStub.Block,
                    opcode: "allMethodArgs",
                    text: "method arguments",
                },
                {
                    opcode: "methodArg",
                    blockType: BlockType.REPORTER,
                    text: "method arg [NAME]",
                    arguments: {
                        NAME: commonArguments.argumentName,
                    },
                    allowDropAnywhere: true, // TODO: is necessary? refractor?
                },
                { // BUTTON
                    opcode: "addTempVars",
                    blockType: BlockType.BUTTON,
                    text: "add temporary variables extension",
                },
                {
                    opcode: "transferMethodArgsToTempVars",
                    blockType: BlockType.COMMAND,
                    text: "transfer method arguments to temporary variables",
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
                        VALUE: commonArguments.anything,
                    },
                },
                {
                    opcode: "getAttribute",
                    blockType: BlockType.REPORTER,
                    text: "get attribute [NAME] of [INSTANCE]",
                    arguments: {
                        NAME: {type: ArgumentType.STRING, defaultValue: "myAttr"},
                        INSTANCE: gceClassInstance.Argument,
                    },
                    allowDropAnywhere: true,
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
                        VALUE: commonArguments.anything,
                    },
                },
                {
                    opcode: "checkIdentity",
                    text: "[INSTANCE1] is [INSTANCE2] ?",
                    blockType: BlockType.BOOLEAN,
                    arguments: {
                        INSTANCE1: gceClassInstance.Argument,
                        INSTANCE2: gceClassInstance.Argument,
                    },
                },
                {
                    ...gceNothing.Block,
                    opcode: "nothing",
                    text: "Nothing",
                },
                "---",
                makeLabel("Scripts"),
                {
                    opcode: "createScript",
                    blockType: BlockType.CONDITIONAL,
                    text: ["create script [NAME]"],
                    branchCount: 1,
                    arguments: {
                        NAME: commonArguments.scriptName,
                    },
                },
                {
                    opcode: "runScript",
                    text: "run script [NAME]",
                    blockType: BlockType.REPORTER,
                    arguments: {
                        NAME: commonArguments.scriptName,
                    },
                },
                "---",
                makeLabel("Debugging & Temporary"),
                {
                    ...dogeiscutObjectStub.Block,
                    opcode: "jsTypeof",
                    text: "debugging: JS typeof [VALUE]",
                    arguments: {
                        VALUE: commonArguments.anything,
                    },
                },
                {
                    opcode: "throw",
                    text: "debugging: throw",
                    blockType: BlockType.COMMAND,
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
                transferMethodArgsToTempVars: (generator, block) => ({kind: "stack"}),
            },
            js: {
                transferMethodArgsToTempVars: (node, compiler, imports) => {
                    // tempVars seems to always be defined
                    compiler.source += 'if (!globalState.thread.GCEargs) throw new Error("Method arguments can only be used within a method.");\n'
                    compiler.source += 'try {Object.assign(tempVars, globalState.thread.GCEargs)} catch {throw new Error("Failed to transfer to temporary variables")};\n'
                },
            },
        }
    }
    
    constructor() {
        Scratch.vm.gceClass = gceClass
        Scratch.vm.gceClassInstance = gceClassInstance
        this.environment = { // to allow access from the extension class
            Script, Method, ClassType, gceClass, VariableManager, SpecialBlockStorageManager,
            CONFIG, Cast, ClassInstanceType, gceClassInstance,
        }
        vm.runtime.registerSerializer( // this basically copies variable serialization
            "gceNothing",
            v => {
                if (v instanceof NothingType) return v.toJSON()
                return null
            },
            v => {
                if (v.customId === "gceNothing") return Nothing
                return null
            },
        )
        runtime.registerCompiledExtensionBlocks("gceClasses", this.getCompileInfo())

        this.classVars = new VariableManager()
        this.scriptVars = new VariableManager()
        this.specialBlockStorage = new SpecialBlockStorageManager()
        
        this.reset()
        // TODO: possibly remove? // TODO: change on release
        runtime.on("PROJECT_START", this.reset)
        runtime.on("PROJECT_STOP_ALL", this.reset)
        runtime.on("THREAD_FINISHED", (thread) => {this.specialBlockStorage.onThreadFinished(thread)})
    }

    reset() {
        this.resetNextMethodArgConfig()
    }

    resetNextMethodArgConfig() {
        this.nextMethodArgConfig = {names: [], defaults: []}
    }
    
    
    /************************************************************************************
    *                                       Blocks                                      *
    ************************************************************************************/

    // Blocks: Classes

    createClass(args, util) { // WARNING: reran (contains script execution)
        const name = Cast.toString(args.NAME)
        
        const ownThread = util.thread
        const ownBlockId = ownThread.peekStack()
        let blockStorage = this.specialBlockStorage.getBlockData(ownBlockId, ownThread) 
        
        if (!blockStorage) {
            blockStorage = {cls: new ClassType(name, null)}
            this.specialBlockStorage.storeBlockData(ownBlockId, ownThread, blockStorage)
            this.classVars.set(name, blockStorage.cls)
        }
        
        const tempScript = this._createScriptFromBranch(util, "<class body>")
        this._runScript(util, tempScript, {cls: blockStorage.cls})
    }

    createSubclass(args, util) { // WARNING: reran (contains script execution)
        const name = Cast.toString(args.NAME)
        const superCls = Cast.toClass(args.SUPERCLASS)
        
        const ownThread = util.thread
        const ownBlockId = ownThread.peekStack()
        let blockStorage = this.specialBlockStorage.getBlockData(ownBlockId, ownThread) 
        
        if (!blockStorage) {
            blockStorage = {cls: new ClassType(name, superCls)}
            this.specialBlockStorage.storeBlockData(ownBlockId, ownThread, blockStorage)
            this.classVars.set(name, blockStorage.cls)
        }
        
        const tempScript = this._createScriptFromBranch(util, "<class body>")
        this._runScript(util, tempScript, {cls: blockStorage.cls})
    }

    getClass(args) {
        const name = Cast.toString(args.NAME)
        return this.classVars.get(name)
    }

    classExists(args) {
        const name = Cast.toString(args.NAME)
        return Cast.toBoolean(this.classVars.has(name))
    }

    allClasses() {
        return Cast.toArray(this.classVars.getNames())
    }
    
    deleteClass(args) {
        this.classVars.delete(Cast.toString(args.NAME))
    }
    
    deleteAllClasses() {
        this.classVars.reset()
    }

    isSubclass(args, util) {
        const subCls = Cast.toClass(args.SUBCLASS)
        const superCls = Cast.toClass(args.SUPERCLASS)
        return Cast.toBoolean(this._isSubclass(subCls, superCls))
    }

    // Blocks: Methods

    configureNextMethodArguments(args, util) {
        const argNames = Cast.toArray(args.ARGNAMES)
        const argDefaults = Cast.toArray(args.ARGDEFAULTS)
        argNames.array.forEach(argName => {
            this.nextMethodArgConfig.names.push(Cast.toString(argName))
        })
        argDefaults.array.forEach(argDefault => {
            this.nextMethodArgConfig.defaults.push(Cast.toString(argDefault))
        })
        if (this.nextMethodArgConfig.defaults.length > this.nextMethodArgConfig.names.length) {
            this.resetNextMethodArgConfig()
            throw new Error("There can only be as many default values as argument names.")
        }
    }

    defineMethod(args, util) {
        const name = Cast.toString(args.NAME)
        const cls = util.thread.GCEclass
        if (!cls) throw new Error("'define method' can only be used within a class.")
        
        const methodArgConfig = this.nextMethodArgConfig
        this.resetNextMethodArgConfig()
        const script = this._createScriptFromBranch(util, "<anonymous>")
        cls.methods[name] = new Method(name, script, methodArgConfig.names, methodArgConfig.defaults)
    }

    defineInitMethod(args, util) {
        this.defineMethod({NAME: CONFIG.INIT_METHOD_NAME}, util)
    }

    return (args, util) {
        util.thread.report = Cast.toString(args.VALUE)
    }
    
    self(args, util) {
        const self = util.thread.GCEself
        if (!self) throw new Error("'self' can only be used within a method.")
        return self
    }

    allMethodArgs(blockArgs, util) {
        const args = util.thread.GCEargs
        if (!args) throw new Error("Method arguments can only be used within a method.")
        return Cast.toObject(args)
    }

    methodArg(blockArgs, util) {
        const name = Cast.toString(blockArgs.NAME)
        const args = util.thread.GCEargs
        if (!args) throw new Error("Method arguments can only be used within a method.")
        const value = args[name]
        if (!value) throw new Error(`Undefined method argument ${quote(name)}.`)
        return value
    }

    addTempVars() { // BUTTON
        if (!Scratch.vm.extensionManager.isExtensionLoaded("tempVars")) {
            Scratch.vm.extensionManager.loadExtensionIdSync("tempVars")
        }
    }

    transferMethodArgsToTempVars (args, util) { // is a compiled block
        throw new Error("Please turn on the compiler. ")
    }

    // Block: Instances
        
    createInstance(args, util) { // WARNING: reran (contains script execution)
        const cls = Cast.toClass(args.CLASS)
        let method = cls.methods[CONFIG.INIT_METHOD_NAME]

        const ownThread = util.thread
        const ownBlockId = ownThread.peekStack()
        let blockStorage = this.specialBlockStorage.getBlockData(ownBlockId, ownThread) 

        if (!blockStorage) {
            blockStorage = {instance: new ClassInstanceType(cls)}
            this.specialBlockStorage.storeBlockData(ownBlockId, ownThread, blockStorage)
        }

        if (!method) method = new Method(CONFIG.INIT_METHOD_NAME, null, [], [])
        const posArgs = Cast.toArray(args.POSARGS).array
        const evaluatedArgs = this._evaluateArgs(method, posArgs)
        const context = {self: blockStorage.instance, args: evaluatedArgs}
        if (method.script) this._runScript(util, method.script, context)
        return blockStorage.instance
    }
    
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

    callMethod(args, util) { // WARNING: reran (contains script execution)
        const instance = args.INSTANCE
        if (!(instance instanceof ClassInstanceType)) {
            throw new Error("Instance argument of 'call method' must be a class instance.")
        }
        const name = Cast.toString(args.NAME)
        const posArgs = Cast.toArray(args.POSARGS).array
        
        const method = instance.cls.methods[name]
        if (!method) {
            throw new Error(`Undefined method ${quote(name)}.`)
        }
        const evaluatedArgs = this._evaluateArgs(method, posArgs)
        const context = {self: instance, args: evaluatedArgs}
        const {hasReturnValue, returnValue} = this._runScript(util, method.script, context)
        if (hasReturnValue) return returnValue
        else return "" // TODO: find other solution possibly
    }

    isInstance(args, util) {
        const instance = args.INSTANCE
        if (!(instance instanceof ClassInstanceType)) {
            throw new Error("Instance argument of 'is instance' must be a class instance.")
        }
        const cls = Cast.toClass(args.CLASS)
        return Cast.toBoolean(this._isSubclass(instance.cls, cls))
    }
    
    // Blocks: Miscellaneous
    typeof(args, util) {
        const value = args.VALUE
        // My Types
        if (value instanceof ClassType) return "Class"
        if (value instanceof ClassInstanceType) return "Class Instance"
        if (value instanceof Method) return "Method"
        if (value instanceof Script) return "Script"
        
        // Safe JS data types
        if (value === undefined) return "Nothing" // TODO: reconsider/refractor
        if (value === null) return "Nothing" // TODO: reconsider/refractor
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
        const instance1 = args.INSTANCE1
        const instance2 = args.INSTANCE2
        if (!(instance1 instanceof ClassInstanceType)) {
            throw new Error("Instance argument of 'is' must be a class instance.")
        }
        if (!(instance2 instanceof ClassInstanceType)) {
            throw new Error("Instance argument of 'is' must be a class instance.")
        }
        return Cast.toBoolean(instance1 === instance2)
    }

    // Blocks: Scripts

    createScript(args, util) {
        const name = Cast.toString(args.NAME)
        const script = this._createScriptFromBranch(util, name)
        this.scriptVars.set(name, script)
    }
    
    runScript(args, util) { // WARNING: reran (contains script execution)
        const name = Cast.toString(args.NAME)
        const script = this.scriptVars.get(name)
        if (!script) throw new Error(`Script ${quote(name)} is not defined.`)
        
        const {hasReturnValue, returnValue} = this._runScript(util, script, {})
        if (hasReturnValue) return returnValue
        else return "" // TODO: find other solution possibly
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

    /************************************************************************************
    *                                      Helpers                                      *
    ************************************************************************************/

    /**
     * @param {ClassType} subCls
     * @param {ClassType} superCls
     * @returns {boolean}
     */
    _isSubclass(subCls, superCls) {
        if (subCls === superCls) return true
        let currentCls = subCls
        while (currentCls.superCls) {
            if (currentCls.superCls === superCls) return true
            currentCls = currentCls.superCls
        }
        return false
    }

    /**
     * @param {BlockUtility} util
     * @param {string} name
     * @returns {Script}
     */
    _createScriptFromBranch(util, name) {
        const branch = util.thread.blockContainer.getBranch(util.thread.peekStack(), 1)
        return new Script(name, branch, util.target)
    }

    /**
     * WARNING: makes the block caling this run MULITPLE times on one activation
     * @param {BlockUtility} util
     * @param {Script} script
     * @param {?ClassType} cls
     * @param {?ClassInstanceType} self
     * @param {?Object} args
     * @returns {{ hasReturnValue: boolean, returnValue: ?any }}
     */
    _runScript(util, script, {cls = null, self = null, args = null}) {
        // Prepare stack frame and get thread
        const frame = util.stackFrame
        if (frame.JGindex === undefined) frame.JGindex = 0
        let thread = frame.JGthread
        let result = {hasReturnValue: false, returnValue: null}
        
        // Make a thread if there is none
        if (script.target.blocks.getBlock(script.branch) === undefined) return result
        if (!thread && (frame.JGindex < 1)) {
            thread = runtime._pushThread(script.branch, script.target, {stackClick: false})

            thread.GCEclass = cls
            thread.GCEself = self
            thread.GCEargs = args

            thread.target = script.target
            thread.tryCompile() // update thread
            
            frame.JGthread = thread
            frame.JGindex = 1
        }

        // Yeah thanks to JG, this section is really confusing, but it works  ¯\_(ツ)_/¯
        // Run the thread if it is active, otherwise set return value and clean up
        if (frame.JGthread && runtime.isActiveThread(frame.JGthread)) util.yield()
        else {
            if (frame.JGthread.report !== undefined) {
                result = {hasReturnValue: true, returnValue: frame.JGthread.report}
                frame.JGindex = 2
            }
            frame.JGthread = ""
        }
        if ((frame.JGindex < 1)) util.yield()
        return result
    }
    
    /**
     * @param {Method} method
     * @param {Array} posargs
     * @returns {Object}
     */
    _evaluateArgs(method, posArgs) {
        const args = Object.create(null)
        let name
        const prefix = (method.name === CONFIG.INIT_METHOD_NAME) ? "initalizing object" : `calling method ${quote(method.name)}`

        // Ensure there are not too many arguments
        if (posArgs.length > method.argNames.length) {
            throw new Error(`${prefix}: expected at most ${method.argNames.length}, but got ${posArgs.length} arguments`)
        }
    
        // Count how many arguments do NOT have defaults
        const posOnlyCount = method.argNames.length - method.argDefaults.length
    
        // Ensure enough positional arguments
        if (posArgs.length < posOnlyCount) {
            throw new Error(`${prefix}: expected at least ${posOnlyCount} positional arguments, but got only ${posArgs.length}`)
        }
    
        // Assign positional arguments
        for (let i = 0; i < posArgs.length; i++) {
            name = method.argNames[i]
            args[name] = posArgs[i]
        }
    
        // Fill in defaults for missing arguments
        const defaultsStartIndex = method.argNames.length - method.argDefaults.length
        for (let i = posArgs.length; i < method.argNames.length; i++) {
            name = method.argNames[i]
            const defaultIndex = i - defaultsStartIndex
            args[name] = method.argDefaults[defaultIndex]
        }
    
        return args
    }
}
const extensionClassInstance = new GCEClassBlocks()
Scratch.extensions.register(extensionClassInstance)
})(Scratch)
