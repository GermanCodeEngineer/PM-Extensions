// Name: Temporary Variables
// ID: SPtempVars
// Description: Create temporary variables for sprites, threads, and the project.
// By: SharkPool
// Licence: MIT

// Version V.1.0.1

(function (Scratch) {
  "use strict";
  if (!Scratch.extensions.unsandboxed) throw new Error("Temporary Variables must run unsandboxed!");

  const Cast = Scratch.Cast;
  const vm = Scratch.vm;
  const runtime = vm.runtime;

  const VAR_KEY = "SPtempVars";

  function initTempVarObjects() {
    runtime[VAR_KEY] = Object.create(null);
    for (const target of runtime.targets) target[VAR_KEY] = Object.create(null);
  }

  runtime.on("PROJECT_START", initTempVarObjects);
  runtime.on("PROJECT_STOP_ALL", initTempVarObjects);
  initTempVarObjects();

  function getCompiler() {
    if (vm.exports.i_will_not_ask_for_help_when_these_break) return vm.exports.i_will_not_ask_for_help_when_these_break();
    else if (vm.exports.JSGenerator && vm.exports.IRGenerator?.exports) return {
      ...vm.exports, ScriptTreeGenerator: vm.exports.IRGenerator.exports.ScriptTreeGenerator
    };
  }
  const compiler = getCompiler();
  if (compiler) {
    const { JSGenerator, ScriptTreeGenerator } = compiler;
    const exp = JSGenerator.exports === undefined ? JSGenerator.unstable_exports : JSGenerator.exports;

    const LOCATION_TO_OBJ = `(thread["${VAR_KEY}"] ??= Object.create(null))`;

    const _ogIRdescendStack = ScriptTreeGenerator.prototype.descendStackedBlock;
    ScriptTreeGenerator.prototype.descendStackedBlock = function (block) {
      switch (block.opcode) {
        case "SPtempVars_setVar":
          return {
            kind: "SPtempVars.setVar",
            name: this.descendInputOfBlock(block, "NAME"),
            value: this.descendInputOfBlock(block, "VALUE")
          };
        case "SPtempVars_scopeVar":
          this.analyzeLoop();
          return {
            kind: "SPtempVars.scopeVar",
            branch: this.descendSubstack(block, "SUBSTACK")
          };
        case "SPtempVars_deleteAllVar":
          return {
            kind: "SPtempVars.deleteVars",
          };
        case "SPtempVars_deleteVar":
          return {
            kind: "SPtempVars.deleteVar",
            name: this.descendInputOfBlock(block, "NAME")
          };
        default: return _ogIRdescendStack.call(this, block);
      }
    }
    const _ogJSdescendStack = JSGenerator.prototype.descendStackedBlock;
    JSGenerator.prototype.descendStackedBlock = function (node) {
      switch (node.kind) {
        case "SPtempVars.setVar": {
          const name = this.descendInput(node.name).asString();
          const value = this.descendInput(node.value).asUnknown();
          this.source += `${LOCATION_TO_OBJ}[${name}] = ${value};\n`;
          break;
        }
        case "SPtempVars.scopeVar": {
          const preScopeVar = this.localVariables.next();
          const postScopeVar = this.localVariables.next();

          this.source += `const ${preScopeVar} = structuredClone(${LOCATION_TO_OBJ});\n`;
          this.descendStack(node.branch, new exp.Frame(false));
          this.source += `const ${postScopeVar} = ${LOCATION_TO_OBJ};\n`;
          this.source += `Object.keys(${postScopeVar}).forEach((k) => {\n`;
          this.source += `if (${preScopeVar}[k] === undefined) delete ${postScopeVar}[k];\n`;
          this.source += `else ${postScopeVar}[k] = ${preScopeVar}[k];\n`;
          this.source += `});\n`;
          break;
        }
        case "SPtempVars.deleteVars": {
          const objVar = this.localVariables.next();
          this.source += `const ${objVar} = ${LOCATION_TO_OBJ};\n`;
          this.source += `Object.keys(${objVar}).forEach(n => delete ${objVar}[n]);\n`;
          break;
        }
        case "SPtempVars.deleteVar": {
          const name = this.descendInput(node.name).asString();
          this.source += `delete ${LOCATION_TO_OBJ}[${name}];\n`;
          break;
        }
        default: return _ogJSdescendStack.call(this, node);
      }
    }

    const _ogIRdescendInp = ScriptTreeGenerator.prototype.descendInput;
    ScriptTreeGenerator.prototype.descendInput = function (block) {
      switch (block.opcode) {
        case "SPtempVars_varExists":
          return {
            kind: "SPtempVars.varExist",
            obj: LOCATION_TO_OBJ,
            name: this.descendInputOfBlock(block, "NAME")
          };
        case "SPtempVars_getVar":
          return {
            kind: "SPtempVars.getVar",
            obj: LOCATION_TO_OBJ,
            name: this.descendInputOfBlock(block, "NAME")
          };
        case "SPtempVars_allVars":
          return {
            kind: "SPtempVars.allVars",
            obj: LOCATION_TO_OBJ
          };
        default: return _ogIRdescendInp.call(this, block);
      }
    };
    const _ogJSdescendInp = JSGenerator.prototype.descendInput;
    JSGenerator.prototype.descendInput = function (node) {
      switch (node.kind) {
        case "SPtempVars.varExist": {
          const name = this.descendInput(node.name).asString();
          return new exp.TypedInput(`(${LOCATION_TO_OBJ}[${name}] !== undefined)`, exp.TYPE_BOOLEAN);
        }
        case "SPtempVars.getVar": {
          const name = this.descendInput(node.name).asString();
          return new exp.TypedInput(`(${LOCATION_TO_OBJ}[${name}] ?? "")`, exp.TYPE_UNKNOWN);
        }
        case "SPtempVars.allVars": {
          return new exp.TypedInput(
            `JSON.stringify(Object.keys(${LOCATION_TO_OBJ}))`,
            exp.TYPE_STRING
          );
        }
        default: return _ogJSdescendInp.call(this, node);
      }
    };
  }

  class SPtempVars {
    getInfo() {
      return {
        id: "SPtempVars",
        name: "Temporary Variables",
        color1: "#FF8C1A",
        color2: "#f07800",
        color3: "#DB6E00",
        menuIconURI: undefined,
        blocks: [
          {
            opcode: "setVar",
            blockType: Scratch.BlockType.COMMAND,
            text: "set var [NAME] to [VALUE]",
            arguments: {
              NAME: { type: Scratch.ArgumentType.STRING, defaultValue: "my variable" },
              VALUE: { type: Scratch.ArgumentType.STRING, defaultValue: "0", exemptFromNormalization: true },
            },
          },
          "---",
          {
            opcode: "scopeVar",
            blockType: Scratch.BlockType.CONDITIONAL,
            text: "run thread vars in scope"
          },
          "---",
          {
            opcode: "varExists",
            blockType: Scratch.BlockType.BOOLEAN,
            text: "var [NAME] exists?",
            arguments: {
              NAME: { type: Scratch.ArgumentType.STRING, defaultValue: "my variable" },
            },
          },
          {
            opcode: "getVar",
            blockType: Scratch.BlockType.REPORTER,
            allowDropAnywhere: true,
            text: "get var [NAME]",
            arguments: {
              NAME: { type: Scratch.ArgumentType.STRING, defaultValue: "my variable" },
            },
          },
          "---",
          {
            opcode: "allVars",
            blockType: Scratch.BlockType.REPORTER,
            text: "all variables",
            disableMonitor: true,
          },
          {
            opcode: "deleteAllVar",
            blockType: Scratch.BlockType.COMMAND,
            text: "delete all variables",
          },
          {
            opcode: "deleteVar",
            blockType: Scratch.BlockType.COMMAND,
            text: "delete var [NAME]",
            arguments: {
              NAME: { type: Scratch.ArgumentType.STRING, defaultValue: "my variable" }
            },
          }
        ],
      };
    }

    // Helper Funcs
    _getOrInitObject(obj) {
      if (obj[VAR_KEY] === undefined) obj[VAR_KEY] = Object.create(null);
      return obj[VAR_KEY];
    }

    _objFromLocation(util) {
      // no need to init global variables as its already done and centeralized
      return this._getOrInitObject(util.thread);
    }

    // Block Funcs
    setVar(args, util) {
      const name = Cast.toString(args.NAME);
      this._objFromLocation(util)[name] = args.VALUE;
    }

    scopeVar(_, util) {
      const curThreadVars = this._getOrInitObject(util.thread);
      if (util.stackFrame.initialized === undefined) {
        util.stackFrame.initialized = true;
        util.stackFrame.preScopeVars = structuredClone(curThreadVars);
        util.startBranch(1, true);
      } else {
        // remove variables from scope
        const preScopeVars = util.stackFrame.preScopeVars;
        Object.keys(curThreadVars).forEach((key) => {
          if (preScopeVars[key] === undefined) delete curThreadVars[key];
          else curThreadVars[key] = preScopeVars[key];
        });
      }
    }

    varExists(args, util) {
      const name = Cast.toString(args.NAME);
      return this._objFromLocation(util)[name] !== undefined;
    }

    getVar(args, util) {
      const name = Cast.toString(args.NAME);
      return this._objFromLocation(util)[name] ?? "";
    }

    allVars(args, util) {
      return JSON.stringify(Object.keys(
        this._objFromLocation(util)
      ));
    }

    deleteAllVar(args, util) {
      const obj = this._objFromLocation(util);
      Object.keys(obj).forEach(name => delete obj[name]);
    }

    deleteVar(args, util) {
      const name = Cast.toString(args.NAME);
      delete this._objFromLocation(util)[name];
    }
  }

  Scratch.extensions.register(new SPtempVars());
})(Scratch);
