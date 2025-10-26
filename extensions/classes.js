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

const IS_DEVELOPMENT = true; // TODO: change on release

/************************************************************************************
*                            Internal Types and Constants                           *
************************************************************************************/

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
        return `<Script '${this.name}'`
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
        return `<Method '${this.name}'`
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
            throw new Error(`'${name}' is not defined.`)
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
        this.threads.delete(thread) // doesnt ever throw
    }
}

const {BlockType, BlockShape, ArgumentType} = Scratch
const runtime = Scratch.vm.runtime

const CONFIG = {
    INIT_METHOD_NAME: "__init__"
}

class Cast extends Scratch.Cast {
    static toArray(value) {
        if (!Scratch.vm.jwArray) throw new Error("Array extension was not loaded properly.")
        return Scratch.vm.jwArray.Type.toArray(value)
    }

    static toObject(value, copy = false) {
        if (!Scratch.vm.dogeiscutObject) throw new Error("Object extension was not loaded properly.")
        return Scratch.vm.dogeiscutObject.Type.toObject(value, copy)
    }

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
     */
     
    constructor(name) {
        this.name = name
        this.methods = {}
    }
    toString() {
        return `<Class '${this.name}'>`
    }
    toJSON() {
        return "Classes can not be serialized."
    }
}

const gceClass = {
    Type: ClassType,
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: BlockShape.PLUS,
        forceOutputType: "gceClass",
        disableMonitor: true,
    },
    Argument: {
        shape: BlockShape.PLUS,
        exemptFromNormalization: true,
        check: ["gceClass"],
    },
    ArgumentAllowVarName: {
        type: ArgumentType.STRING,
        exemptFromNormalization: true,
        defaultValue: IS_DEVELOPMENT ? undefined : "MyClass",
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
        return `<Instance of '${this.cls.name}'>`
    }
    toJSON() {
        return "Class Instances can not be serialized."
    }
    // TODO: define toReporterContent for better visualization
}
const gceClassInstance = {
    Type: ClassInstanceType,
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: BlockShape.PLUS,
        forceOutputType: "gceClassInstance",
        disableMonitor: true,
    },
    Argument: {
        shape: BlockShape.PLUS,
        exemptFromNormalization: true,
        check: ["gceClassInstance"],
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
        return {
            id: "gceClasses",
            name: "Classes",
            color1: "#d9661a",
            color2: "#b34801",
            blocks: [
                makeLabel("Variables n Stuff"),
                {
                    opcode: "getClass",
                    blockType: BlockType.REPORTER,
                    text: "get class [NAME]",
                    arguments: {
                        NAME: {type: ArgumentType.STRING, defaultValue: "MyClass"},
                    },
                },
                {
                    opcode: "deleteClass",
                    blockType: BlockType.COMMAND,
                    text: "delete class [NAME]",
                    arguments: {
                        NAME: {type: ArgumentType.STRING, defaultValue: "MyClass"},
                    },
                },
                {
                    opcode: "deleteAllClasses",
                    blockType: BlockType.COMMAND,
                    text: "delete all classes"
                },
                {
                    opcode: "classExists",
                    blockType: BlockType.BOOLEAN,
                    text: "class [NAME] exists?",
                    arguments: {
                        NAME: {type: ArgumentType.STRING, defaultValue: "Script1"},
                    },
                },
                "---",
                makeLabel("Classes"),
                // New
                {
                    opcode: "createClass",
                    blockType: BlockType.CONDITIONAL,
                    text: ["create class [NAME]"],
                    branchCount: 1,
                    arguments: {
                        NAME: {type: ArgumentType.STRING, defaultValue: "MyClass"},
                    },
                },
                {
                    opcode: "allClasses",
                    blockType: BlockType.REPORTER,
                    text: "all classes",
                    ...jwArrayStub.Block
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
                        NAME: {type: ArgumentType.STRING, defaultValue: "myMethod"},
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
                        VALUE: {
                            type: ArgumentType.STRING, defaultValue: "", 
                            exemptFromNormalization: true,
                        },
                    },
                },
                {
                    opcode: "self",
                    text: "self",
                    ...gceClassInstance.Block,
                },
                {
                    opcode: "allMethodArgs",
                    text: "method arguments",
                    ...dogeiscutObjectStub.Block,
                },
                {
                    opcode: "methodArg",
                    blockType: BlockType.REPORTER,
                    text: "method arg [NAME]",
                    arguments: {
                        NAME: {type: ArgumentType.STRING, defaultValue: "myArg"},
                    },
                    allowDropAnywhere: true,
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
                    opcode: "createInstance",
                    text: "create instance of class [NAME] with positional args [POSARGS]",
                    arguments: {
                        NAME: gceClass.ArgumentAllowVarName,
                        POSARGS: jwArrayStub.Argument,
                    },
                    ...gceClassInstance.Block,
                },
                {
                    opcode: "setAttribute",
                    blockType: BlockType.COMMAND,
                    text: "on [INSTANCE] set attribute [NAME] to [VALUE]",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                        NAME: {type: ArgumentType.STRING, defaultValue: "myAttr"},
                        VALUE: {
                            type: ArgumentType.STRING, defaultValue: "",
                            exemptFromNormalization: true,
                        },
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
                        NAME: {type: ArgumentType.STRING, defaultValue: "myMethod"},
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                "---",
                makeLabel("Scripts"),
                {
                    opcode: "createScript",
                    blockType: BlockType.CONDITIONAL,
                    text: ["create script [NAME]"],
                    branchCount: 1,
                    arguments: {
                        NAME: {type: ArgumentType.STRING, defaultValue: "Script1"},
                    },
                },
                {
                    opcode: "runScript",
                    text: "run script [NAME]",
                    blockType: BlockType.REPORTER,
                    arguments: {
                        NAME: {type: ArgumentType.STRING, defaultValue: "Script1"},
                    },
                },
                "---",
                makeLabel("Temporary"),
                {
                    opcode: "typeof",
                    text: "typeof [VALUE]",
                    blockType: BlockType.REPORTER,
                    arguments: {
                        VALUE: {type: ArgumentType.STRING, exemptFromNormalization: true},
                    },
                },
                {
                    opcode: 'getVariable',
                    text: 'get [name]',
                    arguments: {
                        name: {
                            type: ArgumentType.STRING,
                            defaultValue: 'Variable'
                        }
                    },
                    allowDropAnywhere: true,
                    blockType: BlockType.REPORTER
                },
            ],
        }
    }
    
    constructor() {
        this.classVars = new VariableManager()
        this.scriptVars = new VariableManager()
        this.specialBlockStorage = new SpecialBlockStorageManager()
        this.environment = { // to allow access from the extension class
            Script, Method, ClassType, VariableManager, SpecialBlockStorageManager,
            CONFIG, Cast, ClassInstanceType, gceClassInstance,
        }
        
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

    // Blocks: Variables n Stuff

    getClass(args) {
        const name = Cast.toString(args.NAME)
        return this.classVars.get(name)
    }

    deleteClass(args) {
        this.classVars.delete(Cast.toString(args.NAME))
    }

    deleteAllClasses() {
        this.classVars.reset()
    }

    classExists(args) {
        const name = Cast.toString(args.NAME)
        return Cast.toBoolean(this.classVars.has(name))
    }

    // Blocks: Classes

    createClass(args, util) { // WARNING: reran (contains script execution)
        const name = Cast.toString(args.NAME)
        
        const ownThread = util.thread
        const ownBlockId = ownThread.peekStack()
        let blockStorage = this.specialBlockStorage.getBlockData(ownBlockId, ownThread) 
        
        if (!blockStorage) {
            blockStorage = {cls: new ClassType(name)}
            this.specialBlockStorage.storeBlockData(ownBlockId, ownThread, blockStorage)
            this.classVars.set(name, blockStorage.cls)
        }
        
        const tempScript = this._createScriptFromBranch(util, "<class body>")
        this._runScript(util, tempScript, {cls: blockStorage.cls})
    }

    allClasses() {
        return Cast.toArray(this.classVars.getNames())
    }

    // Blocks: Methods

    configureNextMethodArguments(args, util) {
        const argNames = Cast.toArray(args.ARGNAMES)
        const argDefaults = Cast.toArray(args.ARGDEFAULTS)
        argNames.array.forEach(argName => {
            this.nextMethodArgConfig.names.push(Cast.toString(argName))
        });
        argDefaults.array.forEach(argDefault => {
            this.nextMethodArgConfig.defaults.push(Cast.toString(argDefault))
        });
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
        if (!value) throw new Error(`Undefined method argument '${name}'.`)
        return value
    }

    addTempVars() { // BUTTON
        if (!Scratch.vm.extensionManager.isExtensionLoaded("tempVars")) {
            Scratch.vm.extensionManager.loadExtensionIdSync("tempVars")
        }
    }

    transferMethodArgsToTempVars(blockArgs, util) {
        //if (!Scratch.vm.extensionManager.isExtensionLoaded("tempVars")) {
        //    throw new Error("This block requires the temporary variables extension. Click the button above this block to add it.")
        //}
        const args = util.thread.GCEargs
        if (!args) throw new Error("Method arguments can only be used within a method.")
        if (!util.thread.tempVars) util.thread.tempVars = Object.create(null);
        for (const [argName, argValue] of Object.entries(args)) {
            util.thread.tempVars[`threadVar_${argName}`] = argValue
        }
        console.log("transferred", util.thread)
    }


    // Block: Instances
        
    createInstance(args, util) { // WARNING: reran (contains script execution)
        const cls = Cast.toClass(args.NAME)
        const method = cls.methods[CONFIG.INIT_METHOD_NAME]

        const ownThread = util.thread
        const ownBlockId = ownThread.peekStack()
        let blockStorage = this.specialBlockStorage.getBlockData(ownBlockId, ownThread) 

        if (!blockStorage) {
            blockStorage = {instance: new ClassInstanceType(cls)}
            this.specialBlockStorage.storeBlockData(ownBlockId, ownThread, blockStorage)
        }

        if (method) {
            const posArgs = Cast.toArray(args.POSARGS).array
            const evaluatedArgs = this._evaluateArgs(method, posArgs)
            const context = {self: blockStorage.instance, args: evaluatedArgs}
            this._runScript(util, method.script, context)
        }
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
            throw new Error(`${instance} has no attribute '${name}'.`)
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
            throw new Error(`Undefined method '${name}'.`)
        }
        const evaluatedArgs = this._evaluateArgs(method, posArgs)
        const context = {self: instance, args: evaluatedArgs}
        const {hasReturnValue, returnValue} = this._runScript(util, method.script, context)
        if (hasReturnValue) return returnValue
        else return "" // TODO: find other solution possibly
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
        if (!script) throw new Error(`Script '${name}' is not defined.`)
        
        const {hasReturnValue, returnValue} = this._runScript(util, script)
        if (hasReturnValue) return returnValue
        else return "" // TODO: find other solution possibly
    }

    // Blocks: Temporary

    typeof(args, util) {
        console.log("value", args.VALUE)
        console.log("typeof value", typeof args.VALUE)
    }
    
    getThreadVars (thread) {
        if (!thread.tempVars) {
            thread.tempVars = Object.create(null)
        }
        return thread.tempVars
    }

    getVariable (args, util) {
        const tempVars = this.getThreadVars(util.thread);
        console.log("got all", tempVars)
        const name = `threadVar_${args.name}`
        const value = tempVars[name]
        if (!value) return ''
        console.log("got v", value)
        return value
    }

    /************************************************************************************
    *                                      Helpers                                      *
    ************************************************************************************/

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
        const args = {}
        let name
        const prefix = (method.name === CONFIG.INIT_METHOD_NAME) ? "initalizing object" : `calling method '${method.name}'`

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