/**
 * Author: GermanCodeEngineer
 * Credit: Inspired by & Based on
 *     - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jg_scripts/index.js
 *     - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jwArray/index.js
 *     - https://github.com/PenguinMod/PenguinMod-ExtensionsGallery/blob/main/static/extensions/DogeisCut/dogeiscutObject.js
 *     - https://github.com/PenguinMod/PenguinMod-ExtensionsGallery/blob/main/static/extensions/VeryGoodScratcher42/More-Types.js
 */

(function(Scratch) {
"use strict"

if (!Scratch.extensions.unsandboxed) {
    throw new Error("Classes Extension must run unsandboxed")
}

// Helper Classes
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
        this.classes = {}
    }
    setClass(name, value) {
        this.classes[name] = value
    }
    deleteClass(name) {
        if (this.hasClass(name)) {
            this.classes[name]
        }
    }
    hasClass(name) {
        return name in this.classes
    }
    getClass(name) {
        if (!this.hasClass(name)) {
            throw new Error(`'${name}' is not a class.`)
        }
        return this.classes[name]
    }
    getClassNames() {
        return Array.from(this.classes)
    }
}

const BlockType = Scratch.BlockType
const BlockShape = Scratch.BlockShape
const ArgumentType = Scratch.ArgumentType
const Cast = Scratch.Cast
const runtime = Scratch.vm.runtime
const vars = new VariableManager()

// Add required extensions
if (!Scratch.vm.jwArray) Scratch.vm.extensionManager.loadExtensionIdSync("jwArray")
if (!Scratch.vm.dogeiscutObject) Scratch.vm.extensionManager.loadExtensionURL(
    "https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutObject.js"
)


// Types
const jwArray = {
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
const dogeiscutObject = {
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
        if (!(cls instanceof ClassType)) throw new Error("Cannot create class instance with no class given")
        this.cls = cls
        this.attributes = {}
    }
    
    toString() {
        return `<Instance of '${this.cls.name}'>`
    }
    toJSON() {
        console.log("running .toJSON")
        return "Class Instances do not save."
    }
    // TODO: defined toReporterContent for better visualization
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


class Extension {
    constructor() {
        this.reset()
        vars.reset()
        this.vars = vars
        // TODO: possibly remove? // TODO: change on release
        runtime.on("PROJECT_START", this.reset)
        runtime.on("PROJECT_STOP_ALL", this.reset)
    }

    reset() {
        // block id => ClassType
        this.blockClasses = {}
        this.resetNextMethodArgConfig()
        console.clear() // TODO: remove on release
    }

    resetNextMethodArgConfig() {
        this.nextMethodArgConfig = {names: [], defaults: []}
    }

    /**
     * @returns {object} metadata for this extension and its blocks.
     */
    getInfo() {
        const makeLabel = (text) => {
            return {
            blockType: Scratch.BlockType.LABEL,
            text: text
            }
        }
        return {
            id: "gceClasses",
            name: "Classes",
            color1: "#d9661a",
            color2: "#b34801",
            blocks: [
                makeLabel("Variables n Stuff"),
                {
                    opcode: "getVar",
                    blockType: BlockType.REPORTER,
                    text: "get variable [NAME]",
                    arguments: {
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "Script1"
                        }
                    },
                },
                {
                    opcode: "deleteVar",
                    blockType: BlockType.COMMAND,
                    text: "delete variable [NAME]",
                    arguments: {
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "Script1"
                        }
                    },
                },
                {
                    opcode: "deleteAll",
                    blockType: BlockType.COMMAND,
                    text: "delete all variables"
                },
                {
                    opcode: "allClasses",
                    blockType: BlockType.REPORTER,
                    text: "all classes",
                    disableMonitor: true,
                },
                {
                    opcode: "varExists",
                    blockType: BlockType.BOOLEAN,
                    text: "variable [NAME] exists?",
                    arguments: {
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "Script1"
                        }
                    },
                },
                "---",
                {
                    opcode: "return",
                    text: "return [THING]",
                    blockType: BlockType.COMMAND,
                    isTerminal: true,
                    arguments: {
                        THING: {
                            type: ArgumentType.STRING,
                            defaultValue: "1"
                        }
                    },
                },
                "---",
                makeLabel("Class Creation"),
                // New
                {
                    opcode: "createClass",
                    blockType: BlockType.CONDITIONAL,
                    text: ["create class [NAME]"],
                    branchCount: 1,
                    arguments: {
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "MyClass"
                        }
                    },
                },
                {
                    opcode: "configureNextMethodArguments",
                    blockType: BlockType.COMMAND,
                    text: "configure next method with argument names [ARGNAMES] defaults [ARGDEFAULTS]",
                    arguments: {
                        ARGNAMES: jwArray.Argument,
                        ARGDEFAULTS: jwArray.Argument,
                    }
                },
                {
                    opcode: "defineMethod",
                    blockType: BlockType.CONDITIONAL,
                    text: ["define method [NAME]"],
                    branchCount: 1,
                    arguments: {
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "myMethod"
                        },
                    },
                },
                {
                    opcode: "methodArgs",
                    text: "method arguments",
                    ...dogeiscutObject.Block,
                },
                {
                    opcode: "self",
                    text: "self",
                    ...gceClassInstance.Block,
                },
                "---",
                makeLabel("Class Usage"),
                {
                    opcode: "createInstance",
                    text: "create instance of class [NAME]",
                    arguments: {
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "MyClass"
                        },
                    },
                    ...gceClassInstance.Block
                },
                {
                    opcode: "callMethod",
                    blockType: BlockType.REPORTER,
                    text: "on [INSTANCE] call method [NAME] with positional args [POSARGS]",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "myMethod"
                        },
                        POSARGS: jwArray.Argument,
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
                    opcode: "inside",
                    blockType: BlockType.COMMAND,
                },
            ],
        }
    }

    // Helpers

    _createScriptFromBranch(util, name) {
        const branch = util.thread.blockContainer.getBranch(util.thread.peekStack(), 1)
        return new Script(name, branch, util.target)
    }

    /**
     * @param {Script} script
     * @param {?ClassType} cls
     * @param {?ClassInstanceType} self
     */
    _runScript(util, script, {cls = null, self = null, args = null}) {
        // Prepare stack frame and get thread
        const frame = util.stackFrame
        let thread = frame.JGthread = ""

        // Make a thread
        if (script.target.blocks.getBlock(script.branch) !== undefined) {
            thread = runtime._pushThread(script.branch, script.target, {stackClick: false})
            
            thread.GCEclass = cls
            thread.GCEself = self
            thread.GCEargs = args
            
            thread.target = util.target
            thread.tryCompile() // update thread
            frame.JGthread = thread
        }
        
        delete frame.JGthread
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
    
        // Ensure there are not too many arguments
        if (posArgs.length > method.argNames.length) {
            throw new Error(`calling method '${method.name}': expected at most ${method.argNames.length}, but got ${posArgs.length} arguments`)
        }
    
        // Count how many arguments do NOT have defaults
        const posOnlyCount = method.argNames.length - method.argDefaults.length
    
        // Ensure enough positional arguments
        if (posArgs.length < posOnlyCount) {
            throw new Error(`calling method '${method.name}': expected at least ${posOnlyCount} positional arguments, but got only ${posArgs.length}`)
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
    
    // Old or modified Blocks

    getVar(args) {
        const name = Cast.toString(args.NAME)
        return Cast.toString(vars.getClass(name))
    }

    deleteVar(args) {
        vars.deleteClass(Cast.toString(args.NAME))
    }

    deleteAll() {
        vars.reset()
    }

    allClasses() {
        return JSON.stringify(vars.getClassNames())
    }

    varExists(args) {
        const name = Cast.toString(args.NAME)
        return Cast.toBoolean(vars.hasClass(name))
    }

    return (args, util) {
        util.thread.report = Cast.toString(args.THING)
    }

    // New Blocks

    createClass(args, util) {
        const name = Cast.toString(args.NAME)
        const cls = new ClassType(name)
        const ownId = util.thread.peekStack()
        vars.setClass(name, cls)
        
        const tempScript = this._createScriptFromBranch(util, "<class body>")
        this._runScript(util, tempScript, {cls: cls})
    }

    configureNextMethodArguments(args, util) {
        if ((args.ARGNAMES?.customId !== "jwArray") || (args.ARGDEFAULTS?.customId !== "jwArray")) {
            this.resetNextMethodArgConfig()
            throw new Error("argument names and defaults must both be an array from the array extension")
        }
        if (this.nextMethodArgConfig.defaults.length > this.nextMethodArgConfig.names.length) {
            this.resetNextMethodArgConfig()
            throw new Error("there can only be as many default values as argument names")
        }
        args.ARGNAMES.array.forEach(argName => {
            this.nextMethodArgConfig.names.push(Cast.toString(argName))
        });
        args.ARGDEFAULTS.array.forEach(argDefault => {
            this.nextMethodArgConfig.defaults.push(Cast.toString(argDefault))
        });
    }

    defineMethod(args, util) {
        const name = Cast.toString(args.NAME)
        const cls = util.thread.GCEclass
        util.thread.blockContainer.runtime = null
        util.thread.blockContainer.runtime = Scratch.vm.runtime
        if (!cls) throw new Error("'define method' can only be used within a class")
        
        const methodArgConfig = this.nextMethodArgConfig
        this.resetNextMethodArgConfig()
        const script = this._createScriptFromBranch(util, "<anonymous>")
        cls.methods[name] = new Method(name, script, methodArgConfig.names, methodArgConfig.defaults)
    }

    createInstance(args, util) {
        const name = Cast.toString(args.NAME)
        const cls = vars.getClass(name)
        return new ClassInstanceType(cls)
    }
    
    callMethod(args, util) {
        const instance = args.INSTANCE
        if (instance?.customId !== "gceClassInstance") {
            throw new Error("instance argument of 'call method' must be a class instance")
        }
        const name = Cast.toString(args.NAME)
        if (args.POSARGS?.customId !== "jwArray") {
            throw new Error("positional arguments of 'call method' must be an array from the array extension")
        }
        const posArgs = args.POSARGS.array
        
        const method = instance.cls.methods[name]
        if (!method) {
            throw new Error(`undefined method '${name}'`)
        }
        const evaluatedArgs = this._evaluateArgs(method, posArgs)
        const context = {
            cls: instance.cls,
            self: instance,
            args: evaluatedArgs,
        }
        this._runScript(util, method.script, context)
    }

    methodArgs(blockArgs, util) {
        const args = util.thread.GCEargs
        if (!args) throw new Error("'method arguments' can only be used within a method")
        return args
    }
    
    self(args, util) {
        const self = util.thread.GCEself
        if (!self) throw new Error("'self' can only be used within a class")
        return self
     }

    typeof(args, util) {
        console.log("value", args.VALUE)
        console.log("typeof value", typeof args.VALUE)
    }
    
    inside(args, util) {
        console.error("inside", new Error())
    }
}

Scratch.extensions.register(new Extension())
})(Scratch)