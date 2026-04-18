// Name: Functions & Scopes
// ID: gceFuncsScopes
// Description: Adds Functions and Scoped Variable Blocks. Depends on gceOOP for implementation and is inseperable from it. Contains the block UI's but not their implementation.
// By: GermanCodeEngineer <https://github.com/GermanCodeEngineer/>
// License: MIT
// Made for PenguinMod
// Requires gceOOP to be loaded as well
// Credit: Inspired by & Based on
//  - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jg_scripts/index.js
//  - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jwArray/index.js
//  - https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extensions/jwLambda/index.js
//  - https://github.com/PenguinMod/PenguinMod-ExtensionsGallery/blob/main/static/extensions/DogeisCut/dogeiscutObject.js
//  - https://github.com/PenguinMod/PenguinMod-ExtensionsGallery/blob/main/static/extensions/VeryGoodScratcher42/More-Types.js
//  - https://github.com/SharkPool-SP/SharkPools-Extensions/blob/main/extension-code/Temporary-Variables.js

(/** @param {ScratchObject} Scratch */ function(Scratch) {
"use strict"

/**
 * Allow importing this file in a non-Scratch testing environment.
 * When the extension is imported in PenguinMod this is always true
 */
const isRuntimeEnv = !Scratch.extensions.isTestingEnv
if (isRuntimeEnv && !Scratch.extensions.unsandboxed) {
    throw new Error("Functions and Scoped Variables Extension must run unsandboxed.")
}

/************************************************************************************
*                            Internal Types and Constants                           *
************************************************************************************/

const TYPEOF_MENU = [
    "Boolean",
    "Number",
    "String",

    "Function (GCE)",
    "Instance Method (GCE)",
    "Getter Method (GCE)",
    "Setter Method (GCE)",
    "Operator Method (GCE)",
    "Class (GCE)",
    "Class Instance (GCE)",
    "Nothing (GCE)",

    "Buffer (AndrewGaming587)",
    "Buffer Pointer (AndrewGaming587)",
    "Date (Old Version) (ddededodediamante)",
    "Date (ddededodediamante)",
    "Effect (Div)",
    "Iterator (Div)",
    "Object (DogeisCut)",
    "Regular Expression (DogeisCut)",
    "Set (DogeisCut)",
    "External Timer (steve0greatness)",
    "Array (jwklong)",
    "Color (jwklong)",
    "Date (jwklong)",
    "Lambda (jwklong)",
    "Number (jwklong)",
    "Target (jwklong)",
    "XML (jwklong)",
    "Canvas (RedMan13)",
    "Paint Utils Colour (Fruits555000)",
    
    "JavaScript Undefined",
    "JavaScript Null",
    "JavaScript BigInt",
    "JavaScript Symbol",
    "JavaScript Function",
    "JavaScript Object (generic)",
    "Unknown (rare)"
]

/**
 * @param {string} code
 * @param {string} additionalMsg
 * @returns {never}
 */
function throwInternal(code, additionalMsg = "") {
    throw new Error(
        `An internal error occured in the Functions and Scopes extension. `+
        `Please report it in the PenguinMod discord or on GitHub. ${additionalMsg} [ERROR CODE: ${code}]`
    )
}
const {BlockType, BlockShape, ArgumentType} = Scratch
const runtime = Scratch.vm.runtime

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
const gceFunctionStub = {
    Type: null,
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
        defaultValue: "myFunction",
        exemptFromNormalization: true,
    },
}
const gceNothingStub = {
    Type: null,
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
    funcName: {
        type: ArgumentType.STRING,
        defaultValue: "myFunction",
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

class GCEFuncsScopesBlocks {
    /**
     * @returns {object} metadata for this extension and its blocks.
     */
    getInfo() {
        const makeLabel = (text) => ({blockType: BlockType.LABEL, text: text})
        const info = {
            id: "gceFuncsScopes",
            name: "Functions & Scopes",
            color1: "#428af5",
            menuIconURI: "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICB2aWV3Qm94PSIwIDAgMjAgMjAiCiAgdmVyc2lvbj0iMS4xIgogIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPGNpcmNsZQogICAgY3g9IjEwIgogICAgY3k9IjEwIgogICAgcj0iOSIKICAgIHN0eWxlPSJmaWxsOiM0MjhhZjVmZjsgc3Ryb2tlOiMyZDVmYTg7IHN0cm9rZS13aWR0aDoycHg7IGZpbGwtb3BhY2l0eToxOyBzdHJva2Utb3BhY2l0eToxOyBwYWludC1vcmRlcjpzdHJva2UiIC8+CiAgPHBhdGgKICAgIGQ9Im0gMy41LDEwIDQuNSwtNS41IDEuMiwwLjYgLTMuNyw0LjkgMy43LDQuOSAtMS4yLDAuNiB6CiAgICAgICBtIDEzLDAgLTQuNSwtNS41IC0xLjIsMC42IDMuNyw0LjkgLTMuNyw0LjkgMS4yLDAuNiB6IgogICAgc3R5bGU9ImZpbGw6I2ZmZmZmZiIgLz4KPC9zdmc+",
            blocks: [
                makeLabel("Missing OOP Extension?"),
                { // BUTTON
                    blockType: BlockType.BUTTON,
                    opcode: "addOOPExtension",
                    text: "Add OOP Extension"
                },
                makeLabel("Scoped Variables"),
                {
                    ...commonBlocks.command,
                    opcode: "setScopeVar",
                    text: "set var [NAME] to [VALUE] in current scope",
                    tooltip: "Creates or updates a variable in the current scope.",
                    arguments: {
                        NAME: commonArguments.variableName,
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "getScopeVar",
                    text: "get var [NAME]",
                    tooltip: "Gets the value of a variable visible from the current or outer scopes.",
                    arguments: {
                        NAME: commonArguments.variableName,
                    },
                },
                {
                    ...commonBlocks.returnsBoolean,
                    opcode: "scopeVarExists",
                    text: "var [NAME] exists in [KIND]?",
                    tooltip: "Checks whether a variable exists in the selected scope range.",
                    arguments: {
                        NAME: commonArguments.variableName,
                        KIND: {type: ArgumentType.STRING, menu: "variableAvailableKind"},
                    },
                },
                {
                    ...commonBlocks.command,
                    opcode: "deleteScopeVar",
                    text: "delete var [NAME] in current scope",
                    tooltip: "Deletes a variable from the current scope.",
                    arguments: {
                        NAME: commonArguments.variableName,
                    },
                },
                {
                    ...jwArrayStub.Block,
                    opcode: "allVariables",
                    text: "all variables in [KIND]",
                    tooltip: "Returns all variable names visible in the selected scope range as an array.",
                    arguments: {
                        KIND: {type: ArgumentType.STRING, menu: "variableAvailableKind"},
                    },

                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "createVarScope",
                    text: ["create local variable scope"],
                    tooltip: "Runs the enclosed blocks inside a new local variable scope.",
                },
                {
                    ...commonBlocks.command,
                    opcode: "bindVarToScope",
                    text: "bind [KIND] variable [NAME] to current scope",
                    tooltip: "Links a global or non-local variable into the current scope.",
                    arguments: {
                        KIND: {type: ArgumentType.STRING, menu: "bindVarOriginKind"},
                        NAME: commonArguments.variableName,
                    },
                },
                "---",
                makeLabel("Functions"),
                "---",
                makeLabel("Configure Before Define"),
                {
                    ...commonBlocks.command,
                    opcode: "configureNextFunctionArgs",
                    text: "configure next function: argument names [ARGNAMES] defaults [ARGDEFAULTS]",
                    tooltip: "Configures the argument names and default values used by the next function or method definition.",
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
                    text: ["create function at var [NAME]"],
                    tooltip: "Creates a function and stores it in the chosen variable.",
                    arguments: {
                        NAME: commonArguments.funcName,
                    },
                },
                {
                    ...gceFunctionStub.Block,
                    opcode: "createFunctionNamed",
                    text: ["create function named [NAME]"],
                    tooltip: "Creates and returns a function with the given name.",
                    branchCount: 1,
                    arguments: {
                        NAME: commonArguments.funcName,
                    },
                },
                "---",
                makeLabel("Inside Functions & Methods"),
                {
                    ...commonBlocks.command,
                    opcode: "returnValue",
                    text: "return [VALUE]",
                    tooltip: "Returns a value from the current function or method and exits it.",
                    isTerminal: true,
                    arguments: {
                        VALUE: commonArguments.allowAnything,
                    },
                },
                "---",
                makeLabel("Use Functions"),
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "callFunction",
                    text: "call function [FUNC] with positional args [POSARGS]",
                    tooltip: "Calls a function value with positional arguments.",
                    arguments: {
                        FUNC: gceFunctionStub.ArgumentFunctionOrVarName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                "---",
                makeLabel("Utilities"),
                {
                    ...commonBlocks.returnString,
                    opcode: "objectAsString",
                    text: "[VALUE] as string",
                    tooltip: "Converts a value to its string form, using a class's special as string method when available.",
                    arguments: {
                        VALUE: commonArguments.allowAnything,
                    }
                },
                {
                    ...commonBlocks.returnString,
                    opcode: "typeofValue",
                    text: "typeof [VALUE]",
                    tooltip: "Returns a readable type name for a value.",
                    arguments: {
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    ...commonBlocks.returnsBoolean,
                    opcode: "typeofValueIsMenu",
                    text: "typeof [VALUE] is [TYPE] ?",
                    tooltip: "Check if a value is of a specific type.",
                    arguments: {
                        VALUE: commonArguments.allowAnything,
                        TYPE: {type: ArgumentType.STRING, menu: "typeofMenu"},
                    },
                },
                {
                    ...commonBlocks.returnsBoolean,
                    opcode: "checkIdentity",
                    text: "[VALUE1] is [VALUE2] ?",
                    tooltip: "Checks whether two values are exactly the same value (the same instance).",
                    arguments: {
                        VALUE1: commonArguments.allowAnything,
                        VALUE2: commonArguments.allowAnything,
                    },
                },
                {
                    ...gceNothingStub.Block,
                    opcode: "nothing",
                    text: "Nothing",
                    tooltip: "Returns the cool Nothing value like None in python.",
                },
                {
                    ...commonBlocks.command,
                    opcode: "executeExpression",
                    text: "execute expression [EXPR]",
                    tooltip: "Evaluates the input expression without performing any additional action. This allows you to e.g. use the function call block (a reporter) in a script.",
                    arguments: {
                        EXPR: commonArguments.allowAnything,
                    },
                },
            ],
            menus: {
                variableAvailableKind: {
                    acceptReporters: true,
                    items: [
                        "all scopes",
                        "local scope",
                        "global scope",
                    ],
                },
                bindVarOriginKind: {
                    acceptReporters: true,
                    items: [
                        "non-local",
                        "global",
                    ],
                },
                typeofMenu: {
                    acceptReporters: true,
                    items: TYPEOF_MENU,
                },
            },
        }
        return info
    }

    /************************************************************************************
    *                                       Blocks                                      *
    ************************************************************************************/

    addOOPExtension() { // BUTTON
        if (isRuntimeEnv &&!Scratch.vm.extensionManager.isExtensionLoaded("gceOOP")) {
            Scratch.vm.extensionManager.loadExtensionURL(
                "http://localhost:5173/extensions/gceOOP.js",
            )
        }
    }

    /******************** Scoped Variables ********************/


    setScopeVar = this._getImplementation("setScopeVar")

    getScopeVar = this._getImplementation("getScopeVar")

    scopeVarExists = this._getImplementation("scopeVarExists")

    deleteScopeVar = this._getImplementation("deleteScopeVar")

    allVariables = this._getImplementation("allVariables")

    createVarScope = this._getImplementation("createVarScope")

    bindVarToScope = this._getImplementation("bindVarToScope")

    /******************** Functions ********************/

    // Configure Before Define

    configureNextFunctionArgs = this._getImplementation("configureNextFunctionArgs")

    // Define
    createFunctionAt = this._getImplementation("createFunctionAt")
    createFunctionNamed = this._getImplementation("createFunctionNamed")

    // Inside Functions & Methods
    returnValue = this._getImplementation("returnValue")

    // Use Functions
    callFunction = this._getImplementation("callFunction")

    /******************** Utilities ********************/
    objectAsString = this._getImplementation("objectAsString")

    typeofValue = this._getImplementation("typeofValue")

    typeofValueIsMenu = this._getImplementation("typeofValueIsMenu")

    checkIdentity = this._getImplementation("checkIdentity")

    nothing = this._getImplementation("nothing")

    executeExpression = this._getImplementation("executeExpression")

    /************************************************************************************
    *                                      Helpers                                      *
    ************************************************************************************/

    /**
     * @param {string} blockId 
     * @returns {Function} the implementation of the block from gceOOP
     */
    _getImplementation(blockId) {
        if (!isRuntimeEnv) {
            return () => {}
        }

        // Acess actual implementation at runtime
        return (function bridgeToOOPExtension(...args) {
            if (!Scratch.vm.extensionManager.isExtensionLoaded("gceOOP")) {
                throw new Error(`The Functions & Scopes Extension requires the OOP Extension to work. Please click the "Add OOP Extension" button.`)
            }
            let func
            try {
                const gceOOPInstance = runtime.ext_gceOOP
                func = gceOOPInstance[blockId].bind(gceOOPInstance)
            } catch (e) {
                throwInternal("nimble-dolphin", e)
            }
            // Let errors raise, do not catch
            return func(...args)
        })
    }
}

const extensionClassInstance = new GCEFuncsScopesBlocks()
Scratch.extensions.register(extensionClassInstance)
// Compiled blocks info is registered in the OOP extension
if (!isRuntimeEnv) {
    console.log("Imported Functions & Scopes extension in non-runtime environment")
}
})(Scratch)

/************************************************************************************
*                                 Type Definitions                                  *
************************************************************************************/

/**
 * @typedef {Object} ExtensionManager
 * @property {function(string): boolean} isExtensionLoaded
 * @property {function(string): void} loadExtensionIdSync
 * @property {function(string): void} loadExtensionURL
 */

/**
 * @typedef {Object} VirtualMachine
 * @property {Runtime} runtime
 * @property {ExtensionManager} extensionManager
 */

/**
 * @typedef {Object} Runtime
 * @property {GCEOOPBlocks}  [ext_gceOOP]
 * @property {GCEFuncsScopesBlocks} ext_gceFuncsScopes
 */

/**
 * @typedef {Object} ScratchExtensions
 * @property {boolean} unsandboxed
 * @property {Function} register
 * @property {boolean} [isTestingEnv]
 */

/**
 * @typedef {Object} ScratchObject
 * @property {Object<string, string>} ArgumentType
 * @property {Object<string, string>} BlockType
 * @property {Object<string, number>} BlockShape
 * @property {ScratchExtensions} extensions
 * @property {VirtualMachine} vm
 */
