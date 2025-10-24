/**
 * Author: GermanCodeEngineer
 * Credit: Inspired by & Based on
 *     - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jg_scripts/index.js
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
     * @param {Array} blocks 
     */
    constructor(name, blocks) {
        this.name = name
        this.blocks = blocks
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

class CustomClass {
    /**
     * @param {string} name 
     */
    constructor(name) {
        this.name = name
        this.methods = {}
    }
    toString() {
        return `<Custom Class '${this.name}'>`
    }
    toJSON() {
        return "Custom Classes do not save."
    }
}

class CustomClassInstance {
    /**
     * @param {CustomClass} cls 
     */
    constructor(cls) {
        this.cls = cls
        this.attributes = {}
    }
    toString() {
        return `<Instance of '${this.cls.name}'>`
    }
    toJSON() {
        return "Custom Class Instances do not save."
    }
}


class VariableManager {
    constructor() {
        this.reset()
    }
    reset() {
        this.variables = {}
        this.scripts = new Set()
        this.classes = new Set()
    }
    assertFree(name) {
        if (this.has(name)) {
            throw new Error(`Name '${name}' is already occupied. Please delete it or pick another name.`)
        }
    }
    has(name) {
        return (name in this.variables)
    }
    get(name) {
        if (!this.has(name)) {
            throw new Error(`Name '${name}' is not defined.`)
        }
        return this.variables[name]
    }
    delete(name) {
        if (this.has(name)) {
            delete this.variables[name]
            this.scripts.delete(name)
            this.classes.delete(name)
        }
    }
    addScript(name, value) {
        this.variables[name] = value
        this.scripts.add(name)
    }
    addClass(name, value) {
        this.variables[name] = value
        this.classes.add(name)
    }
    hasScript(name) {
        return this.scripts.has(name)
    }
    hasClass(name) {
        return this.classes.has(name)
    }
    getScript(name) {
        const value = this.get(name) // Also checks if exists
        if (!this.hasScript(name)) {
            throw new Error(`'${name}' is not a script.`)
        }
        return value
    }
    getClass(name) {
        const value = this.get(name) // Also checks if exists
        if (!this.hasClass(name)) {
            throw new Error(`'${name}' is not a class.`)
        }
        return value
    }
    getScriptNames() {
        return Array.from(this.scripts)
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
Scratch.vm.extensionManager.loadExtensionIdSync("jwArray")
if (!Scratch.vm.dogeiscutObject) (async () => {
    await Scratch.vm.extensionManager.loadExtensionURL("https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutObject.js");
})();


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
const gceClassInstance = {
    Type: null, // TODO: eventually create
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: BlockShape.BUMPED,
        //forceOutputType: "Object",
        disableMonitor: true
    },
    Argument: {
        shape: BlockShape.BUMPED,
        exemptFromNormalization: true,
        //check: ["Object"]
    }
}


class Extension {
    constructor() {
        this.reset()
        // TODO: possibly remove? // TODO: change on release
        runtime.on("PROJECT_START", this.reset)
        runtime.on("PROJECT_STOP_ALL", this.reset)
    }

    reset() {
        // block id => Custom Class
        this.blockClasses = {}
        this.resetNextMethodArgConfig()
        vars.reset()
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
                    opcode: "allScripts",
                    blockType: BlockType.REPORTER,
                    text: "all scripts",
                    disableMonitor: true,
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
                {
                    opcode: "scriptData",
                    text: "script data",
                    blockType: BlockType.REPORTER,
                    allowDropAnywhere: true,
                    disableMonitor: true
                },
                "---",
                makeLabel("Running Scripts"),
                {
                    opcode: "runBlocks",
                    text: "run script [NAME] in [SPRITE]",
                    blockType: BlockType.CONDITIONAL,
                    branchCount: -1,
                    arguments: {
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "Script1"
                        },
                        SPRITE: {
                            type: ArgumentType.STRING,
                            menu: "TARGETS"
                        }
                    },
                },
                {
                    opcode: "runBlocksData",
                    text: "run script [NAME] in [SPRITE] with data [DATA]",
                    blockType: BlockType.CONDITIONAL,
                    branchCount: -1,
                    arguments: {
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "Script1"
                        },
                        SPRITE: {
                            type: ArgumentType.STRING,
                            menu: "TARGETS"
                        },
                        DATA: {
                            type: ArgumentType.STRING,
                            defaultValue: "data"
                        }
                    },
                },
                {
                    opcode: "reportBlocks",
                    text: "run script [NAME] in [SPRITE]",
                    blockType: BlockType.REPORTER,
                    allowDropAnywhere: true,
                    arguments: {
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "Script1"
                        },
                        SPRITE: {
                            type: ArgumentType.STRING,
                            menu: "TARGETS"
                        }
                    },
                },
                {
                    opcode: "reportBlocksData",
                    text: "run script [NAME] in [SPRITE] with data [DATA]",
                    blockType: BlockType.REPORTER,
                    allowDropAnywhere: true,
                    arguments: {
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "Script1"
                        },
                        SPRITE: {
                            type: ArgumentType.STRING,
                            menu: "TARGETS"
                        },
                        DATA: {
                            type: ArgumentType.STRING,
                            defaultValue: "data"
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
                "---",
                makeLabel("Script Creation"),
                {
                    opcode: "createScriptFromBranch",
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
                "---",
                makeLabel("Temporary"),
                {
                    opcode: "typeof",
                    text: "typeof [VALUE] [X]",
                    blockType: BlockType.REPORTER,
                    arguments: {VALUE: {type: ArgumentType.STRING, exemptFromNormalization: true}, X: gceClassInstance.Argument},
                },

            ],
            menus: {
                TARGETS: {
                    acceptReporters: true,
                    items: "_getTargets"
                }
            },
        }
    }

    // Helpers

    _getTargets() {
        const spriteNames = [{
                text: "myself",
                value: "_myself_"
            },
            {
                text: "Stage",
                value: "_stage_"
            }
        ]
        const targets = runtime.targets
        for (let index = 1; index < targets.length; index++) {
            const target = targets[index]
            if (target.isOriginal) spriteNames.push({
                text: target.getName(),
                value: target.getName()
            })
        }
        return spriteNames.length > 0 ? spriteNames : [""]
    }

    _createScriptFromBranch(util, name) {
        const script = new Script(name, [])
        const branch = util.thread.target.blocks.getBranch(util.thread.peekStack(), 1)
        if (branch) {
            script.blocks.push({
                stack: branch,
                target: util.target
            })
        }
        return script
    }

    _getMenuTarget(sprite, util) {
        if (sprite === "_myself_") return util.target
        else if (sprite === "_stage_") return runtime.getTargetForStage()
        else return runtime.getSpriteTargetByName(sprite)
    }

    _prepareRun(args, util) {
        // Get target, script name and script data
        const target = this._getMenuTarget(args.SPRITE, util)
        const name = Cast.toString(args.NAME)
        const data = args.DATA ? Cast.toString(args.DATA) : ""
        if (!vars.hasScript(name) || !target) return [null, null]

        // Prepare stack frame and get thread
        const frame = util.stackFrame
        if (frame.JGindex === undefined) frame.JGindex = 0
        if (frame.JGthread === undefined) frame.JGthread = ""
        const blocks = vars.getScript(name).blocks
        let thread = frame.JGthread

        // Make a thread if there is none
        if (!thread && frame.JGindex < blocks.length) {
            const thisStack = blocks[frame.JGindex]
            if (thisStack.target.blocks.getBlock(thisStack.stack) !== undefined) {
                thread = runtime._pushThread(thisStack.stack, thisStack.target, {
                    stackClick: false
                })
                thread.scriptData = data
                thread.target = target
                thread.tryCompile() // update thread
                frame.JGthread = thread
            }
            frame.JGindex = frame.JGindex + 1
        }

        return [frame, blocks] // For later use
    }

    /**
     * @return {CustomClass}
     */
    _getContainerClass(ownId, blockContainer) {
        let currentId = ownId
        let parentId = null
        let currentBlock = null
        let parentBlock = null
        let finalId = null

        while (true) {
            currentBlock = blockContainer.getBlock(currentId)
            parentId = currentBlock.parent
            if (parentId === null) break
            parentBlock = blockContainer.getBlock(parentId)
            if ((parentBlock.next !== currentId) && (parentBlock.opcode === "gceClasses_createClass")) {
                // this ensures the parent block is to the left and not above the current block
                finalId = parentId
                break
            }
            currentId = parentId
        }
        if (finalId === null) return null
        else return this.blockClasses[finalId]
    }


    // Old or modified Blocks

    getVar(args) {
        const name = Cast.toString(args.NAME)
        return Cast.toString(vars.get(name))
    }

    deleteVar(args) {
        vars.delete(Cast.toString(args.NAME))
    }

    deleteAll() {
        vars.reset()
    }

    allScripts() {
        return JSON.stringify(vars.getScriptNames())
    }

    allClasses() {
        return JSON.stringify(vars.getClassNames())
    }

    varExists(args) {
        const name = Cast.toString(args.NAME)
        return Cast.toBoolean(vars.has(name))
    }

    return (args, util) {
        util.thread.report = Cast.toString(args.THING)
    }

    scriptData(args, util) {
        const data = util.thread.scriptData
        return data ? data : ""
    }

    runBlocksData(args, util) {
        this.runBlocks(args, util)
    }
    runBlocks(args, util) {
        const [frame, blocks] = this._prepareRun(args, util)
        if (frame === null) return

        // Run the thread if it is active, otherwise clean up
        if (frame.JGthread && runtime.isActiveThread(frame.JGthread)) util.startBranch(1, true)
        else frame.JGthread = ""
        if (frame.JGindex < blocks.length) util.startBranch(1, true)
    }

    reportBlocksData(args, util) {
        return this.reportBlocks(args, util) || ""
    }
    reportBlocks(args, util) {
        const [frame, blocks] = this._prepareRun(args, util)
        if (frame === null) return

        // Run the thread if it is active, otherwise set return value and clean up
        if (frame.JGthread && runtime.isActiveThread(frame.JGthread)) util.yield()
        else {
            if (frame.JGthread.report !== undefined) {
                frame.JGreport = frame.JGthread.report
                frame.JGindex = blocks.length + 1
            }
            frame.JGthread = ""
        }
        if (frame.JGindex < blocks.length) util.yield()
        return frame.JGreport || ""
    }

    // New Blocks

    createClass(args, util, blockInfo) {
        const name = Cast.toString(args.NAME)
        vars.assertFree(name)
        const cls = new CustomClass(name)
        const ownId = util.thread.peekStack()

        this.blockClasses[ownId] = cls
        vars.addClass(name, cls)
        util.startBranch(1, false)
    }

    configureNextMethodArguments(args, util) {
        this.resetNextMethodArgConfig()
        if (args.ARGNAMES?.customId === "jwArray") {
            args.ARGNAMES.array.forEach(argName => {
                this.nextMethodArgConfig.names.push(Cast.toString(argName))
            });
        }
        if (args.ARGDEFAULTS?.customId === "jwArray") {
            args.ARGDEFAULTS.array.forEach(argDefault => {
                this.nextMethodArgConfig.defaults.push(Cast.toString(argDefault))
            });
        }
        if (this.nextMethodArgConfig.defaults.length > this.nextMethodArgConfig.names.length) {
            this.resetNextMethodArgConfig()
            throw new Error("there can only be as many defaults as argument names")
        }
    }

    defineMethod(args, util) {
        const name = Cast.toString(args.NAME)
        const ownId = util.thread.peekStack()
        const blockContainer = util.thread.blockContainer
        const containerClass = this._getContainerClass(ownId, blockContainer)
        if (containerClass === null) throw new Error("'add method' must be used within a class")
        
        const methodArgConfig = this.nextMethodArgConfig
        this.resetNextMethodArgConfig()
        const script = this._createScriptFromBranch(util, "<anonymous>")
        containerClass.methods[name] = new Method(name, script, methodArgConfig.names, methodArgConfig.defaults)
        console.log(containerClass)
    }

    createInstance(args, util) {
        const name = Cast.toString(args.NAME)
        return new CustomClassInstance(vars.getClass(name))
    }

    methodArgs(args, util) {
        // Step 2
    }

    createScriptFromBranch(args, util) {
        const name = Cast.toString(args.NAME)
        vars.assertFree(name)
        const script = this._createScriptFromBranch(util, name)
        vars.addScript(name, script)
    }

    typeof(args, util) {
        console.log("value", args.VALUE)
        console.log("typeof value", typeof args.VALUE)
    }
}

Scratch.extensions.register(new Extension())
})(Scratch)