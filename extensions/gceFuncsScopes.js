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
    throwError("Functions and Scoped Variables Extension must run unsandboxed.")
}

/************************************************************************************
*                                   Translations                                    *
************************************************************************************/
const TRANSLATIONS = {
    de: {
        // Errors in chronological order of appearance
        "Functions and Scoped Variables Extension must run unsandboxed.": "Die Funktionen- und Variablen-Erweiterung muss ohne Sandbox laufen.",
        "An internal error occured in the Functions and Scopes extension. Please report it in the PenguinMod discord or on GitHub. ${additionalMsg} [ERROR CODE: ${code}]": "Ein interner Fehler ist in der Funktionen- und Variablen-Erweiterung aufgetreten. Bitte melde ihn im PenguinMod Discord oder auf GitHub. ${additionalMsg} [FEHLERCODE: ${code}]",
        'The Functions & Scopes Extension requires the OOP Extension to work. Please click the "Add OOP Extension" button.': 'Die Funktionen- und Variablen-Erweiterung benötigt die OOP-Erweiterung, um zu funktionieren. Bitte klicke auf die Schaltfläche "OOP-Erweiterung hinzufügen".',

        // getInfo defaults
        "myFunction": "meineFunktion",
        "myVar": "meineVariable",
        '["name"]': '["name"]',
        '[]': '[]',

        // getInfo block texts
        "Functions & Scopes": "Funktionen & Variablen",
        "Missing OOP Extension?": "Fehlende OOP-Erweiterung?",
        "Add OOP Extension": "OOP-Erweiterung hinzufügen",
        "Scoped Variables": "Bereichsvariablen",
        "set var [NAME] to [VALUE] in current scope": "Setze Variable [NAME] auf [VALUE] im aktuellen Bereich",
        "Creates or updates a variable in the current scope.": "Erstellt oder aktualisiert eine Variable im aktuellen Bereich.",
        "get var [NAME]": "Lese Variable [NAME]",
        "Gets the value of a variable visible from the current or outer scopes.": "Liest den Wert einer Variable, die im aktuellen oder äußeren Bereich sichtbar ist.",
        "var [NAME] exists in [KIND]?": "Existiert Variable [NAME] in [KIND]?",
        "Checks whether a variable exists in the selected scope range.": "Prüft, ob eine Variable im ausgewählten Bereich existiert.",
        "delete var [NAME] in current scope": "Lösche Variable [NAME] im aktuellen Bereich",
        "Deletes a variable from the current scope.": "Löscht eine Variable aus dem aktuellen Bereich.",
        "all variables in [KIND]": "Alle Variablen in [KIND]",
        "Returns all variable names visible in the selected scope range as an array.": "Gibt alle Variablennamen zurück, die im ausgewählten Bereich sichtbar sind, als Array.",
        "create local variable scope": "Erstelle lokalen Variablenbereich",
        "Runs the enclosed blocks inside a new local variable scope.": "Führt die eingeschlossenen Blöcke in einem neuen lokalen Variablenbereich aus.",
        "bind [KIND] variable [NAME] to current scope": "Binde [KIND]-Variable [NAME] an den aktuellen Bereich",
        "Links a global or non-local variable into the current scope.": "Verknüpft eine globale oder nicht-lokale Variable mit dem aktuellen Bereich.",
        "Functions": "Funktionen",
        "Configure Before Define": "Vorher konfigurieren",
        "configure next function: argument names [ARGNAMES] defaults [ARGDEFAULTS]": "Konfiguriere nächste Funktion: Argumentnamen [ARGNAMES] Standardwerte [ARGDEFAULTS]",
        "Configures the argument names and default values used by the next function or method definition.": "Konfiguriert die Argumentnamen und Standardwerte, die von der nächsten Funktions- oder Methodendefinition verwendet werden.",
        "Define": "Definieren",
        "create function at var [NAME]": "Erstelle Funktion bei Variable [NAME]",
        "Creates a function and stores it in the chosen variable.": "Erstellt eine Funktion und speichert sie in der gewählten Variable.",
        "create function named [NAME]": "Erstelle Funktion mit Namen [NAME]",
        "Creates and returns a function with the given name.": "Erstellt und gibt eine Funktion mit dem angegebenen Namen zurück.",
        "Inside Functions & Methods": "Innerhalb von Funktionen & Methoden",
        "return [VALUE]": "Gib [VALUE] zurück",
        "Returns a value from the current function or method and exits it.": "Gibt einen Wert aus der aktuellen Funktion oder Methode zurück und beendet sie.",
        "Use Functions": "Funktionen verwenden",
        "call function [FUNC] with positional args [POSARGS]": "Rufe Funktion [FUNC] mit Positionsargumenten [POSARGS] auf",
        "Calls a function value with positional arguments.": "Ruft einen Funktionswert mit Positionsargumenten auf.",
        "Utilities": "Dienstprogramme",
        "[VALUE] as string": "[VALUE] als Zeichenfolge",
        "Converts a value to its string form, using a class's special as string method when available.": "Wandelt einen Wert in seine Zeichenfolgendarstellung um und verwendet bei Bedarf die spezielle As-String-Methode einer Klasse.",
        "typeof [VALUE]": "typeof [VALUE]",
        "Returns a readable type name for a value.": "Gibt einen lesbaren Typnamen für einen Wert zurück.",
        "typeof [VALUE] is [TYPE] ?": "typeof [VALUE] ist [TYPE]?",
        "[TYPE]": "[TYPE]",
        "Provides a list of value types, you can choose from.": "Stellt eine Liste von Wertetypen zur Auswahl bereit.",
        "Check if a value is of a specific type.": "Prüft, ob ein Wert von einem bestimmten Typ ist.",
        "[VALUE1] is [VALUE2] ?": "[VALUE1] ist [VALUE2]?",
        "Checks whether two values are exactly the same value (the same instance).": "Prüft, ob zwei Werte genau derselbe Wert (dasselbe Objekt) sind.",
        "Nothing": "Nichts",
        "Returns the cool Nothing value like None in python.": "Gibt den coolen Nothing-Wert zurück, wie None in Python.",
        "execute expression [EXPR]": "Führe Ausdruck [EXPR] aus",
        "Evaluates the input expression without performing any additional action. This allows you to e.g. use the function call block (a reporter) in a script.": "Wertet den Eingabeausdruck aus, ohne zusätzliche Aktion auszuführen. So kannst du z.B. den Funktionsaufruf-Block (einen Reporter) in einem Skript verwenden.",
    },
}

// Add underscore to every key in every value of TRANSLATIONS, because Scratch.translate expects it
Object.entries(TRANSLATIONS).forEach(([lang, langTranslations]) => {
    Object.keys(langTranslations).forEach(key => {
        langTranslations["_" + key] = langTranslations[key];
        delete langTranslations[key];
    });
});
Scratch.translate.setup(TRANSLATIONS);

/************************************************************************************
*                            Internal Types and Constants                           *
************************************************************************************/

/**
 * Translates and replaces placeholders in the format {key} with corresponding values from an object.
 * * @param {string} englishMessageTemplate - The english string containing {key} placeholders.
 * @param {Object<string, *>} values - Key-value pairs to inject.
 * @returns {string}
 */
function translatedMsg(englishMessageTemplate, values) {
    // Let format-message handle interpolation
    // Check if translation exists in TRANSLATIONS.de
    const key = englishMessageTemplate;
    const deTranslations = TRANSLATIONS && TRANSLATIONS.de;
    // If the key or key with leading underscore is not found, throw
    if (!deTranslations || (deTranslations["_" + key] === undefined)) {
        throw new Error(`Missing German translation for: ${key}`);
    } else {
        // Translation exists, return the translated message
        return Scratch.translate(englishMessageTemplate, values);
    }
}

/**
 * Translates an error message and throws it as an Error. Placeholders in the format {key} can be replaced with corresponding values from an object.
 * @param {string} message
 * @param {Object<string, *>} values - Key-value pairs to inject.
 * @returns {never}
 */
function throwError(message, values = {}) {
    throw new Error(translatedMsg(message, values))
}

/**
 * @param {string} code
 * @param {string} additionalMsg
 * @returns {never}
 */
function throwInternal(code, additionalMsg = "") {
    throwError(
        "An internal error occured in the Functions and Scopes extension. Please report it in the PenguinMod discord or on GitHub. ${additionalMsg} [ERROR CODE: ${code}]", {additionalMsg, code}
    )
}

/**
 * Properly manages menus, the translation between internal and public names and input validation
 */
class MenuManager {
    /**
     * @param {string} invalidPublicValueError
     * @param {Array<{value: string, text: string}>} menuItems
     */
    constructor(invalidPublicValueError, menuItems) {
        this._invalidPublicValueError = invalidPublicValueError
        this._menuItems = menuItems
        this._interalToPublic = Object.fromEntries(menuItems.map(item => [item.value, item.text]))
        this._publicToInternal = Object.fromEntries(menuItems.map(item => [item.text, item.value]))
    }

    /**
     * @return {Array<{value: string, text: string}>}
     */
    getMenuItems() {
        return this._menuItems
    }

    /**
     * @param {string} publicValue
     * @returns {string}
     * @throws if value is not in the menu
     */
    publicToInternal(publicValue) {
        if (!(publicValue in this._publicToInternal)) {
            throwError(this._invalidPublicValueError, {value: quote(publicValue)})
        }
        return this._publicToInternal[publicValue]
    }

    /**
     * @param {string} 
     * @returns {string}
     */
    internalToPublic(internalValue) {
        return this._interalToPublic[internalValue]
    }

    /**
     * Converts a user input to internal format (can be in either format because of acceptReporters=true)
     * @param {string} inputValue
     * @returns {boolean}
     */
    standardizeBlockInput(inputValue) {
        if (inputValue in this._interalToPublic) {
            return inputValue
        } else {
            // Handles invalid values
            return this.publicToInternal(inputValue)
        }
    }
}

const {BlockType, BlockShape, ArgumentType} = Scratch
const runtime = Scratch.vm.runtime

const MENUS = {
    // Not translated on purpose, because that could result in different behaviour of scripts
    VARIABLE_AVAILABLE_KIND: new MenuManager("Invalid variable scope kind: {value}", [
        {value: "VAK_ALL", text: "all scopes"},
        {value: "VAK_LOCAL", text: "local scope"},
        {value: "VAK_GLOBAL", text: "global scope"},
    ]),

    BIND_VAR_ORIGIN_KIND: new MenuManager("Invalid variable kind: {value}", [
        {value: "BVOK_GLOBAL", text: "global"},
        {value: "BVOK_NONLOCAL", text: "non-local"},
    ]),

    TYPEOF_MENU: new MenuManager("Invalid typeof type: {value}", [
        {value: "TO_BOOLEAN", text: "Boolean"},
        {value: "TO_NUMBER", text: "Number"},
        {value: "TO_STRING", text: "String"},

        {value: "TO_FUNCTION_GCE", text: "Function (GCE)"},
        {value: "TO_INSTANCE_METHOD_GCE", text: "Instance Method (GCE)"},
        {value: "TO_GETTER_METHOD_GCE", text: "Getter Method (GCE)"},
        {value: "TO_SETTER_METHOD_GCE", text: "Setter Method (GCE)"},
        {value: "TO_OPERATOR_METHOD_GCE", text: "Operator Method (GCE)"},
        {value: "TO_CLASS_GCE", text: "Class (GCE)"},
        {value: "TO_INSTANCE_GCE", text: "Class Instance (GCE)"},
        {value: "TO_NOTHING_GCE", text: "Nothing (GCE)"},
        
        {value: "TO_BUFFER_AG587", text: "Buffer (AndrewGaming587)"},
        {value: "TO_BUFFER_POINTER_AG587", text: "Buffer Pointer (AndrewGaming587)"},
        {value: "TO_DATE_OLD_DDE", text: "Date (Old Version) (ddededodediamante)"},
        {value: "TO_DATE_DDE", text: "Date (ddededodediamante)"},
        {value: "TO_EFFECT_DIV", text: "Effect (Div)"},
        {value: "TO_ITERATOR_DIV", text: "Iterator (Div)"},
        {value: "TO_OBJECT_DOGEISCUT", text: "Object (DogeisCut)"},
        {value: "TO_REGEXP_DOGEISCUT", text: "Regular Expression (DogeisCut)"},
        {value: "TO_SET_DOGEISCUT", text: "Set (DogeisCut)"},
        {value: "TO_EXTERNAL_TIMER_S0G", text: "External Timer (steve0greatness)"},
        {value: "TO_ARRAY_JWKLONG", text: "Array (jwklong)"},
        {value: "TO_COLOR_JWKLONG", text: "Color (jwklong)"},
        {value: "TO_DATE_JWKLONG", text: "Date (jwklong)"},
        {value: "TO_LAMBDA_JWKLONG", text: "Lambda (jwklong)"},
        {value: "TO_NUMBER_JWKLONG", text: "Number (jwklong)"},
        {value: "TO_TARGET_JWKLONG", text: "Target (jwklong)"},
        {value: "TO_VECTOR_JWKLONG", text: "Vector (jwklong)"},
        {value: "TO_XML_JWKLONG", text: "XML (jwklong)"},
        {value: "TO_CANVAS_REDMAN13", text: "Canvas (RedMan13)"},
        {value: "TO_PAINT_UTILS_COLOUR_FRUITS", text: "Paint Utils Colour (Fruits555000)"},
        
        {value: "TO_UNDEFINED_JS", text: "JavaScript Undefined"},
        {value: "TO_NULL_JS", text: "JavaScript Null"},
        {value: "TO_BIGINT_JS", text: "JavaScript BigInt"},
        {value: "TO_SYMBOL_JS", text: "JavaScript Symbol"},
        {value: "TO_FUNCTION_JS", text: "JavaScript Function"},
        {value: "TO_OBJECT_JS", text: "JavaScript Object (generic)"},
        {value: "TO_UNKNOWN", text: "Unknown (rare)"},
    ]),
}

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
        defaultValue: translatedMsg("myFunction"),
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
        defaultValue: translatedMsg("myVar"),
    },
    funcName: {
        type: ArgumentType.STRING,
        defaultValue: translatedMsg("myFunction"),
    },
    argNames: {
        type: ArgumentType.STRING,
        exemptFromNormalization: true,
        defaultValue: translatedMsg('["name"]'),
    },
    argDefaults: {
        type: ArgumentType.STRING,
        exemptFromNormalization: true,
        defaultValue: translatedMsg("[]"),
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
            name: translatedMsg("Functions & Scopes"),
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
                    ...commonBlocks.returnsAnything,
                    opcode: "typeofValueSelection",
                    text: "[TYPE]",
                    tooltip: "Provides a list of value types, you can choose from.",
                    arguments: {
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
                    items: MENUS.VARIABLE_AVAILABLE_KIND.getMenuItems(),
                },
                bindVarOriginKind: {
                    acceptReporters: true,
                    items: MENUS.BIND_VAR_ORIGIN_KIND.getMenuItems(),
                },
                typeofMenu: {
                    acceptReporters: true,
                    items: MENUS.TYPEOF_MENU.getMenuItems(),
                },
            },
        }
        info.blocks.forEach((block) => {
            if (typeof block !== "object") return
            if (typeof block.text === "string") block.text = translatedMsg(block.text)
            else if (typeof block.text === "object") {
                block.text = block.text.map(translatedMsg)
            }
            if (typeof block.tooltip === "string") block.tooltip = translatedMsg(block.tooltip)
            else if (typeof block.tooltip === "object") {
                block.tooltip = block.tooltip.map(translatedMsg)
            }
        })
        return info
    }

    /************************************************************************************
    *                                       Blocks                                      *
    ************************************************************************************/

    async _isLocalhostAvailable(url) {
        try {
            const controller = new AbortController()
            const timeout = setTimeout(() => controller.abort(), 500)
            const response = await fetch(url, { method: "HEAD", signal: controller.signal })
            clearTimeout(timeout)
            return response.ok
        } catch {
            return false
        }
    }

    async _addLocalhostOrProdExtension(localUrl, prodUrl) {
        const url = (await this._isLocalhostAvailable(localUrl)) ? localUrl : prodUrl
        Scratch.vm.extensionManager.loadExtensionURL(url)
    }

    addOOPExtension() { // BUTTON
        if (isRuntimeEnv &&!Scratch.vm.extensionManager.isExtensionLoaded("gceOOP")) {
            this._addLocalhostOrProdExtension(
                "http://localhost:5173/extensions/gceOOP.js",
                "https://germancodeengineer.github.io/PM-Extensions/extensions/gceOOP.js"
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

    typeofValueSelection = this._getImplementation("typeofValueSelection")

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
                throwError('The Functions & Scopes Extension requires the OOP Extension to work. Please click the "Add OOP Extension" button.')
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
