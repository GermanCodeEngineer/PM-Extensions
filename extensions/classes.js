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


/**
 * Safely stringify an object with:
 *  - circular reference protection
 *  - max depth control
 *  - automatic handling of Immutable-like objects
 *
 * Works in environments without `require` or `import`.
 *
 * @param {any} value - The value to stringify.
 * @param {number} [maxDepth=3] - Maximum recursion depth.
 * @param {number} [space=2] - Indentation for JSON.
 * @returns {string}
 */
function safeStringify(value, maxDepth = 4, space = 2) {
  const seen = new WeakSet();

  function _normalize(val, depth = 0) {
    // Handle Immutable-like structures
    if (val && typeof val === 'object') {
      if (typeof val.toJS === 'function') {
        try {
          return _normalize(val.toJS(), depth + 1);
        } catch {
          return '[ImmutableError]';
        }
      }
      if (typeof val.toJSON === 'function' && !Array.isArray(val)) {
        try {
          return _normalize(val.toJSON(), depth + 1);
        } catch {
          return '[JSONError]';
        }
      }
    }

    // Handle circulars and depth limit
    if (typeof val === 'object' && val !== null) {
      if (seen.has(val)) return '[Circular]';
      if (depth >= maxDepth) return '[MaxDepth]';
      seen.add(val);

      const out = Array.isArray(val) ? [] : {};
      for (const k in val) {
        try {
          out[k] = _normalize(val[k], depth + 1);
        } catch {
          out[k] = '[Error]';
        }
      }
      seen.delete(val);
      return out;
    }

    return val;
  }

  return JSON.stringify(_normalize(value), null, space);
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
        
    createInstance(args, util) { // WARNING: reran (contains script execution)
        const clsName = Cast.toString(args.NAME)
        const cls = this.classVars.get(clsName)
        const method = cls.methods[config.INIT_METHOD_NAME]

        if (method) {
            const ownThread = util.thread
            const ownBlockId = ownThread.peekStack()
            let blockStorage = this.specialBlockStorage.getBlockData(ownBlockId, ownThread) 
            
            if (!blockStorage) {
                blockStorage = {instance: new ClassInstanceType(cls)}
                this.specialBlockStorage.storeBlockData(ownBlockId, ownThread, blockStorage)
            }
        
            const posArgs = Cast.toArray(args.POSARGS).array
            const evaluatedArgs = this._evaluateArgs(method, posArgs)
            const context = {
                self: blockStorage.instance,
                args: evaluatedArgs,
            }
            this._runScript(util, method.script, context)
        }
        return blockStorage.instance
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
        if (!self) throw new Error("'self' can only be used within a method")
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

    callMethod(args, util) { // WARNING: reran (contains script execution)
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
        return this._runScript(util, method.script, context)
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
        if (!script) throw new Error("%no-script%") // TODO: msg
        
        const {hasReturnValue, returnValue} = this._runScript(util, script)
        if (hasReturnValue) return returnValue
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
     * WARNING: makes the block caling this run MULITPLE times on one activation
     * @param {Script} script
     * @param {boolean} doYield
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
        if (frame.JGthread && runtime.isActiveThread(frame.JGthread)) {
            console.log("still-active-yield")
            util.yield()
        }
        else {
            if (frame.JGthread.report !== undefined) {
                result = {hasReturnValue: true, returnValue: frame.JGthread.report}
                frame.JGindex = 2
            }
            frame.JGthread = ""
        }
        if ((frame.JGindex < 1)) {
            console.log("index-too-low-yield")
            util.yield()
        }
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