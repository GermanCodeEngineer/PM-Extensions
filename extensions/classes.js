// Name: Classes
// ID: gceClasses
// Description: Python-like classes and OOP
// By: GermanCodeEngineer <https://github.com/GermanCodeEngineer/>
// License: MIT
// Credit: Inspired by & Based on
//  - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jg_scripts/index.js
//  - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jwArray/index.js
//  - https://github.com/PenguinMod/PenguinMod-ExtensionsGallery/blob/main/static/extensions/DogeisCut/dogeiscutObject.js
//  - https://github.com/PenguinMod/PenguinMod-ExtensionsGallery/blob/main/static/extensions/VeryGoodScratcher42/More-Types.js


(function(Scratch) {
"use strict"

if (!Scratch.extensions.unsandboxed) {
    throw new Error("Classes Extension must run unsandboxed")
}

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
        return "Scripts do not save."
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
        return "Methods do not save."
    }
}

class ClassType {
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
        return "Classes do not save."
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
            throw new Error(`'${name}' is not a class.`)
        }
        return this.variables[name]
    }
    getNames() {
        return Object.keys(this.variables)
    }
}

const BlockType = Scratch.BlockType
const BlockShape = Scratch.BlockShape
const ArgumentType = Scratch.ArgumentType
const ScratchCast = Scratch.Cast
const runtime = Scratch.vm.runtime

const config = {
    INIT_METHOD_NAME: "__init__"
}

class Cast extends ScratchCast {
    static toArray(value) {
        if (!Scratch.vm.jwArray) throw new Error("Array extension was not loaded properly")
        return Scratch.vm.jwArray.Type.toArray(value)
    }

    static toObject(value, copy = false) {
        if (!Scratch.vm.dogeiscutObject) throw new Error("Object extension was not loaded properly")
        return Scratch.vm.dogeiscutObject.Type.toObject(value, copy)
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
        }
    },
}
const dogeiscutObjectStub = {
    Type: null,
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: BlockShape.PLUS,
        forceOutputType: "Object",
        disableMonitor: true
    },
    Argument: {
        shape: BlockShape.PLUS,
        exemptFromNormalization: true,
        check: ["Object"]
    }
}

class ClassInstanceType {
    customId = "gceClassInstance"

    /**
     * @param {ClassType} cls 
     */
    constructor(cls) {
        console.error(new Error("new instance"))
        if (!(cls instanceof ClassType)) throw new Error("Cannot create class instance with no class given")
        this.cls = cls
        this.attributes = {}
    }
    
    toString() {
        return `<Instance of '${this.cls.name}'>`
    }
    toJSON() {
        return "Class Instances do not save."
    }
    // TODO: define toReporterContent for better visualization
}
const gceClassInstance = {
    Type: ClassInstanceType,
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: BlockShape.PLUS,
        forceOutputType: "gceClassInstance",
        disableMonitor: true
    },
    Argument: {
        shape: BlockShape.PLUS,
        exemptFromNormalization: true,
        check: ["gceClassInstance"]
    }
}

/************************************************************************************
*                                  Extension Class                                  *
************************************************************************************/

class Extension {
    constructor() {
        this.classVars = new VariableManager()
        this.scriptVars = new VariableManager()
        this.reset()
        // TODO: possibly remove? // TODO: change on release
        runtime.on("PROJECT_START", this.reset)
        runtime.on("PROJECT_STOP_ALL", this.reset)
    }

    reset() {
        this.resetNextMethodArgConfig()
    }

    resetNextMethodArgConfig() {
        this.nextMethodArgConfig = {names: [], defaults: []}
    }

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
                        NAME: {type: ArgumentType.STRING, defaultValue: "Script1"},
                    },
                },
                {
                    opcode: "deleteClass",
                    blockType: BlockType.COMMAND,
                    text: "delete class [NAME]",
                    arguments: {
                        NAME: {type: ArgumentType.STRING, defaultValue: "Script1"},
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
                {
                    opcode: "createInstance",
                    text: "create instance of class [NAME] with positional args [POSARGS]",
                    arguments: {
                        NAME: {type: ArgumentType.STRING, defaultValue: "MyClass"},
                        POSARGS: jwArrayStub.Argument,
                    },
                    ...gceClassInstance.Block,
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
                        VALUE: {type: ArgumentType.STRING, defaultValue: "1"},
                    },
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
                },
                "---",
                makeLabel("Instances"),
                {
                    opcode: "self",
                    text: "self",
                    ...gceClassInstance.Block,
                },
                {
                    opcode: "setAttribute",
                    blockType: BlockType.COMMAND,
                    text: "on [INSTANCE] set attribute [NAME] to [VALUE]",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                        NAME: {type: ArgumentType.STRING, defaultValue: "myAttr"},
                        VALUE: {type: ArgumentType.STRING, defaultValue: ""},
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
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "Script1"
                        }
                    },
                },
                {
                    opcode: "runScript",
                    text: "run script [NAME]",
                    blockType: BlockType.REPORTER,
                    arguments: {
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "Script1"
                        }
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
            ],
        }
    }
    
    /************************************************************************************
    *                                       Blocks                                      *
    ************************************************************************************/

    // Blocks: Variables n Stuff

    getClass(args) {
        const name = Cast.toString(args.NAME)
        return Cast.toString(this.classVars.get(name))
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

    createClass(args, util) {
        const name = Cast.toString(args.NAME)
        const cls = new ClassType(name)
        this.classVars.set(name, cls)
        
        const tempScript = this._createScriptFromBranch(util, "<class body>")
        this._runScript(util, tempScript, false, {cls: cls})
    }

    allClasses() {
        return Cast.toArray(this.classVars.getNames())
    }

    createInstance(args, util) {
        const clsName = Cast.toString(args.NAME)
        const cls = this.classVars.get(clsName)
        
        const instance = new ClassInstanceType(cls)
        const method = cls.methods[config.INIT_METHOD_NAME]

        if (method) {
            const posArgs = Cast.toArray(args.POSARGS).array
            const evaluatedArgs = this._evaluateArgs(method, posArgs)
            const context = {
                self: instance,
                args: evaluatedArgs,
            }
            this._runScript(util, method.script, true, context)
        }
        return instance
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
            throw new Error("there can only be as many default values as argument names")
        }
    }

    defineMethod(args, util) {
        const name = Cast.toString(args.NAME)
        const cls = util.thread.GCEclass
        if (!cls) throw new Error("'define method' can only be used within a class")
        
        const methodArgConfig = this.nextMethodArgConfig
        this.resetNextMethodArgConfig()
        const script = this._createScriptFromBranch(util, "<anonymous>")
        cls.methods[name] = new Method(name, script, methodArgConfig.names, methodArgConfig.defaults)
    }

    defineInitMethod(args, util) {
        this.defineMethod({NAME: config.INIT_METHOD_NAME}, util)
    }

    return (args, util) {
        util.thread.report = Cast.toString(args.VALUE)
    }

    allMethodArgs(blockArgs, util) {
        const args = util.thread.GCEargs
        if (!args) throw new Error("method arguments can only be used within a method")
        return Cast.toObject(args)
    }

    methodArg(blockArgs, util) {
        const name = Cast.toString(blockArgs.NAME)
        const args = util.thread.GCEargs
        if (!args) throw new Error("method arguments can only be used within a method")
        const value = args[name]
        if (!value) throw new Error(`undefined method argument '${name}'`)
        return value
    }

    // Block: Instances
    
    self(args, util) {
        const self = util.thread.GCEself
        if (!self) throw new Error("'self' can only be used within a class")
        return self
    }
    
    setAttribute(args, util) {
        const instance = args.INSTANCE
        if (!(instance instanceof ClassInstanceType)) {
            throw new Error("instance argument of 'set attribute' must be a class instance")
        }
        const name = Cast.toString(args.NAME)
        const value = args.VALUE
        instance.attributes[name] = value
    }
    
    getAttribute(args, util) {
        const instance = args.INSTANCE
        if (!(instance instanceof ClassInstanceType)) {
            throw new Error("instance argument of 'get attribute' must be a class instance")
        }
        const name = Cast.toString(args.NAME)
        if (!(name in instance.attributes)) {
            throw new Error(`${instance} has no attribute '${name}'`)
        }
        return instance.attributes[name]
    }

    callMethod(args, util) {
        const instance = args.INSTANCE
        if (!(instance instanceof ClassInstanceType)) {
            throw new Error("instance argument of 'call method' must be a class instance")
        }
        const name = Cast.toString(args.NAME)
        const posArgs = Cast.toArray(args.POSARGS).array
        
        const method = instance.cls.methods[name]
        if (!method) {
            throw new Error(`undefined method '${name}'`)
        }
        const evaluatedArgs = this._evaluateArgs(method, posArgs)
        const context = {
            self: instance,
            args: evaluatedArgs,
        }
        return this._runScript(util, method.script, true, context)
    }

    // Blocks: Scripts

    createScript(args, util) {
        const name = Cast.toString(args.NAME)
        const script = this._createScriptFromBranch(util, name)
        this.scriptVars.set(name, script)
    }

    runScript(args, util) {
        const name = Cast.toString(args.NAME)
        const script = this.scriptVars.get(name)
        if (!script) throw new Error("%no-script&")
        return this._runScript(util, script, true, {})
    }

    // Blocks: Temporary

    typeof(args, util) {
        console.log("value", args.VALUE)
        console.log("typeof value", typeof args.VALUE)
    }

    /************************************************************************************
    *                                      Helpers                                      *
    ************************************************************************************/

    _createScriptFromBranch(util, name) {
        const branch = util.thread.blockContainer.getBranch(util.thread.peekStack(), 1)
        return new Script(name, branch, util.target)
    }

    /**
     * @param {Script} script
     * @param {boolean} doYield
     * @param {?ClassType} cls
     * @param {?ClassInstanceType} self
     * @param {?Object} args
     */
    
    _runScript(util, script, doYield, {cls = null, self = null, args = null}) {
        console.log("running", script, new Error())
        console.log(util.thread.blockContainer)
        // Prepare stack frame and get thread
        const frame = util.stackFrame
        if (frame.JGindex === undefined) frame.JGindex = 0
        let thread = frame.JGthread

        // Make a thread if there is none
        if (script.target.blocks.getBlock(script.branch) === undefined) return
        if (!thread && (frame.JGindex < 1)) {
            thread = runtime._pushThread(script.branch, script.target, {stackClick: false})

            thread.GCEclass = cls
            thread.GCEself = self
            thread.GCEargs = args

            thread.target = script.target
            thread.tryCompile() // update thread
            
            frame.JGthread = thread
            frame.JGindex = frame.JGindex + 1
        }

        // Yeah thanks to JG, this section is really confusing, but it works  ¯\_(ツ)_/¯
        // Run the thread if it is active, otherwise set return value and clean up
        if (frame.JGthread && runtime.isActiveThread(frame.JGthread) && doYield) util.yield()
        else {
            if (frame.JGthread.report !== undefined) {
                frame.JGreport = frame.JGthread.report
                frame.JGindex = 1 + 1
            }
            frame.JGthread = ""
        }
        if ((frame.JGindex < 1) && doYield) util.yield()
        return frame.JGreport
    }
    
    /**
     * @param {Method} method
     * @param {Array} posargs
     * @returns {Object}
     */
    _evaluateArgs(method, posArgs) {
        const args = {}
        let name
        const prefix = (method.name === config.INIT_METHOD_NAME) ? "initalizing object" : `calling method '${method.name}'`

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

Scratch.extensions.register(new Extension())
})(Scratch)