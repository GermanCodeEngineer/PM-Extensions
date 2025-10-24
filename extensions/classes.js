/**
 * Author: GermanCodeEngineer
 * Credit: Inspired by & Based on
 *     - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jg_scripts/index.js
 *     - https://github.com/PenguinMod/PenguinMod-ExtensionsGallery/blob/main/static/extensions/VeryGoodScratcher42/More-Types.js
 */

(function (Scratch) {
"use strict"

if (!Scratch.extensions.unsandboxed) {
  throw new Error("Classes Extension must run unsandboxed")
}

// Temporary Utility
 
function safeStringify(obj) {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (typeof value === "object" && value !== null) {
      if (seen.has(value)) return "[Circular]";
      seen.add(value);
    }
    return value;
  });
}
function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Helper Classes
class Script {
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

class CustomClass {
  constructor(name) {
    this.name = name
  }
  toString() {
    return `<Custom Class '${this.name}'>`
  }
  toJSON() {
    return "Custom Classes do not save."
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
const ArgumentType = Scratch.ArgumentType
const Cast = Scratch.Cast
const runtime = Scratch.vm.runtime
const vars = new VariableManager()

// Add Array Extension
//if (!Scratch.vm.jwArray) Scratch.vm.extensionManager.loadExtensionIdSync("jwArray")
//const jwArray = Scratch.vm.jwArray

class Extension {
  constructor() {
    /**
     * The runtime instantiating this block package.
     * @type {Runtime}
     */
    // TODO: possibly remove? // TODO: change on release
    runtime.on("PROJECT_START", () => { vars.reset(); console.clear() })
    runtime.on("PROJECT_STOP_ALL", vars.reset)
  }
  
  /**
   * @returns {object} metadata for this extension and its blocks.
  */
  getInfo() {
    return {
      id: "gceClasses",
      name: "Classes",
      color1: "#d9661a",
      color2: "#b34801",
      blocks: [
        {
          opcode: "getVar",
          blockType: BlockType.REPORTER,
          text: "get variable [NAME]",
          arguments: {
            NAME: { type: ArgumentType.STRING, defaultValue: "Script1" }
          },
        },
        {
          opcode: "deleteVar",
          blockType: BlockType.COMMAND,
          text: "delete variable [NAME]",
          arguments: {
            NAME: { type: ArgumentType.STRING, defaultValue: "Script1" }
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
          text: "all scripts"
        },
        {
          opcode: "allClasses",
          blockType: BlockType.REPORTER,
          text: "all classes"
        },
        {
          opcode: "varExists",
          blockType: BlockType.BOOLEAN,
          text: "variable [NAME] exists?",
          arguments: {
            NAME: { type: ArgumentType.STRING, defaultValue: "Script1" }
          },
        },
        "---",
        {
          opcode: "return",
          text: "return [THING]",
          blockType: BlockType.COMMAND,
          isTerminal: true,
          arguments: {
            THING: { type: ArgumentType.STRING, defaultValue: "1" }
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
        {
          opcode: "runBlocks",
          text: "run script [NAME] in [SPRITE]",
          blockType: BlockType.CONDITIONAL,
          branchCount: -1,
          arguments: {
            NAME: { type: ArgumentType.STRING, defaultValue: "Script1" },
            SPRITE: { type: ArgumentType.STRING, menu: "TARGETS" }
          },
        },
        {
          opcode: "runBlocksData",
          text: "run script [NAME] in [SPRITE] with data [DATA]",
          blockType: BlockType.CONDITIONAL,
          branchCount: -1,
          arguments: {
            NAME: { type: ArgumentType.STRING, defaultValue: "Script1" },
            SPRITE: { type: ArgumentType.STRING, menu: "TARGETS" },
            DATA: { type: ArgumentType.STRING, defaultValue: "data" }
          },
        },
        "---",
        {
          opcode: "reportBlocks",
          text: "run script [NAME] in [SPRITE]",
          blockType: BlockType.REPORTER,
          allowDropAnywhere: true,
          arguments: {
            NAME: { type: ArgumentType.STRING, defaultValue: "Script1" },
            SPRITE: { type: ArgumentType.STRING, menu: "TARGETS" }
          },
        },
        {
          opcode: "reportBlocksData",
          text: "run script [NAME] in [SPRITE] with data [DATA]",
          blockType: BlockType.REPORTER,
          allowDropAnywhere: true,
          arguments: {
            NAME: { type: ArgumentType.STRING, defaultValue: "Script1" },
            SPRITE: { type: ArgumentType.STRING, menu: "TARGETS" },
            DATA: { type: ArgumentType.STRING, defaultValue: "data" }
          },
        },
        "---",
        "---",
        // New
        {
          opcode: "createClass",
          blockType: BlockType.COMMAND,
          text: ["create class [NAME]"],
          branchCount: 1,
          arguments: {
            NAME: { type: ArgumentType.STRING, defaultValue: "MyClass" }
          },
        },
        
        {
          opcode: "createScriptFromBranch",
          blockType: BlockType.COMMAND,
          text: ["create script named [NAME]"],
          branchCount: 1,
          arguments: {
            NAME: { type: ArgumentType.STRING, defaultValue: "Script1" }
          },
        },
      ],
      menus: {
        TARGETS: { acceptReporters: true, items: "_getTargets" }
      },
    }
  }
  
  // Helpers
  _getTargets() {
    const spriteNames = [
      { text: "myself", value: "_myself_" },
      { text: "Stage", value: "_stage_" }
    ]
    const targets = runtime.targets
    for (let index = 1; index < targets.length; index++) {
      const target = targets[index]
      if (target.isOriginal) spriteNames.push({
        text: target.getName(), value: target.getName()
      })
    }
    return spriteNames.length > 0 ? spriteNames : [""]
  }
  
  _createScriptFromBranch(name, util) {
    vars.assertFree(name)
    const script = new Script(name, [])
    const branch = util.thread.target.blocks.getBranch(util.thread.peekStack(), 1)
    if (branch) {
      script.blocks.push({ stack : branch, target : util.target })
    }
    vars.addScript(name, script)
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
    console.log("util", util)
    if (frame.JGindex === undefined) frame.JGindex = 0
    if (frame.JGthread === undefined) frame.JGthread = ""
    const blocks = vars.getScript(name).blocks
    let thread = frame.JGthread
    
    // Make a thread if there is none
    if (!thread && frame.JGindex < blocks.length) {
      const thisStack = blocks[frame.JGindex]
      if (thisStack.target.blocks.getBlock(thisStack.stack) !== undefined) {
        thread = runtime._pushThread(thisStack.stack, thisStack.target, { stackClick: false })
        thread.scriptData = data
        thread.target = target
        thread.tryCompile() // update thread
        frame.JGthread = thread
      }
      frame.JGindex = frame.JGindex + 1
    }
    
    return [frame, blocks] // For later use
  }

  
  // Old or modified Blocks
  
  getVar(args) {
    const name = Cast.toString(args.NAME)
    return Cast.toString(vars.get(name))
  }
  
  deleteVar(args) { vars.delete(Cast.toString(args.NAME)) }

  deleteAll() { vars.reset() }

  allScripts() { return JSON.stringify(vars.getScriptNames()) }
  
  allClasses() { return JSON.stringify(vars.getClassNames()) }

  varExists(args) {
    const name = Cast.toString(args.NAME)
    return Cast.toBoolean(vars.has(name))
  }

  return(args, util) { util.thread.report = Cast.toString(args.THING) }

  scriptData(args, util) {
    const data = util.thread.scriptData
    return data ? data : ""
  }
  
  runBlocksData(args, util) { this.runBlocks(args, util) }
  runBlocks(args, util) {
    const [frame, blocks] = this._prepareRun(args, util);
    if (frame === null) return
    
    // Run the thread if it is active, otherwise clean up
    if (frame.JGthread && runtime.isActiveThread(frame.JGthread)) util.startBranch(1, true)
    else frame.JGthread = ""
    if (frame.JGindex < blocks.length) util.startBranch(1, true)
  }

  reportBlocksData(args, util) { return this.reportBlocks(args, util) || "" }
  reportBlocks(args, util) {
    const [frame, blocks] = this._prepareRun(args, util);
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
  
  createClass(args, util) {
    const name = Cast.toString(args.NAME)
    vars.assertFree(name)
    const cls = new CustomClass(name)
    vars.addClass(name, cls)
  }
  
  createScriptFromBranch(args, util) {
    this._createScriptFromBranch(Cast.toString(args.NAME), util)
  }
}

Scratch.extensions.register(new Extension())
})(Scratch)
