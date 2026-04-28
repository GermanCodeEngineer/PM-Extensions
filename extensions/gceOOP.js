// Name: OOP
// ID: gceOOP
// Description: Python-like classes and many features of Object Orientated Programming
// By: GermanCodeEngineer <https://github.com/GermanCodeEngineer/>
// License: MIT
// Made for PenguinMod
// Requires and automatically adds jwArray and dogeiscutObject
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
    throwError("OOP Extension must run unsandboxed.")
}

/************************************************************************************
*                                   Translations                                    *
************************************************************************************/
const TRANSLATIONS = {
    de: {
        // Errors in chronological order of appearance
        "OOP Extension must run unsandboxed.": "Die OOP Erweiterung muss ohne Sandbox laufen.",
        "[OOP Extension] Failed to create custom shape": "[OOP Erweiterung] Fehler beim Erstellen einer benutzerdefinierten Form",
        "An internal error occured in the OOP extension. Please report it in the PenguinMod discord or on GitHub. {additionalMsg} [ERROR CODE: {code}]": "Ein interner Fehler ist in der OOP Erweiterung aufgetreten. Bitte melde ihn im PenguinMod Discord oder auf GitHub. {additionalMsg} [FEHLERCODE: {code}]",
        "Variable {name} already exists in the current scope, can not bind variable with the same name.": "Variable {name} existiert bereits im aktuellen Bereich, kann keine Variable mit demselben Namen binden.",
        "Variable {name} is not defined.": "Variable {name} ist nicht definiert.",
        "self can only be used within an instance, getter or setter method.": "self kann nur innerhalb einer Instanz-, Getter- oder Setter-Methode verwendet werden.",
        "setter value can only be used within a setter method.": "setter-Wert kann nur innerhalb einer Setter-Methode verwendet werden.",
        "operator value can only be used within an operator method.": "operator-Wert kann nur innerhalb einer Operator-Methode verwendet werden.",
        '{blockText} can only be used within a class definition or "on class" block.': '{blockText} kann nur innerhalb einer Klassendefinition oder eines "Mit Klasse"-Blocks verwendet werden.',
        "return can only be used within a function or method.": "return kann nur innerhalb einer Funktion oder Methode verwendet werden.",
        "There can only be as many default values as argument names.": "Es darf nur so viele Standardwerte wie Argumentnamen geben.",
        "Can not set a variable in a scope, which does not support variables (e.g. a class definition).": "Kann keine Variable in einem Bereich setzen, der keine Variablen unterstützt (z.B. eine Klassendefinition).",
        "Can not delete a variable in a scope, which does not support variables(e.g. a class definition).": "Kann keine Variable in einem Bereich löschen, der keine Variablen unterstützt (z.B. eine Klassendefinition).",
        "No global variable named {name} found.": "Keine globale Variable mit dem Namen {name} gefunden.",
        "Can not bind a variable to a scope, which does not support variables(e.g. a class definition).": "Kann keine Variable an einen Bereich binden, der keine Variablen unterstützt (z.B. eine Klassendefinition).",
        "No non-local variable named {name} found.": "Keine nicht-lokale Variable mit dem Namen {name} gefunden.",
        "Type checking for extension types is not available in a non-runtime environment.": "Typüberprüfung für Erweiterungstypen ist in einer Nicht-Laufzeitumgebung nicht verfügbar.",
        "Casting to extension types is not available in a non-runtime environment.": "Umwandlung in Erweiterungstypen ist in einer Nicht-Laufzeitumgebung nicht verfügbar.",
        "Object extension was not loaded properly.": "Die Objekt-Erweiterung wurde nicht richtig geladen.",
        "Array extension was not loaded properly.": "Die Array-Erweiterung wurde nicht richtig geladen.",
        "Expected a {expectedDescription}, but got no input value.": "Erwartet wurde ein(e) {expectedDescription}, aber es wurde kein Eingabewert übergeben.",
        "Expected a {expectedDescription} not a {actualDescription}.": "Erwartet wurde ein(e) {expectedDescription}, nicht ein(e) {actualDescription}.",
        "Expected a {expectedDescription}, but variable {value} is not defined.": "Erwartet wurde ein(e) {expectedDescription}, aber die Variable {value} ist nicht definiert.",
        "Expected a {expectedDescription}, but variable {value} is a(n) {varValueName}.": "Erwartet wurde ein(e) {expectedDescription}, aber die Variable {value} ist ein(e) {varValueName}.",
        "Invalid class property: {value}": "Ungültige Klassen-Eigenschaft: {value}",
        "Invalid operator method: {value}": "Ungültige Operator-Methode: {value}",
        "Invalid special method: {value}": "Ungültige Spezialmethode: {value}",
        "Invalid typeof type: {value}": "Ungültiger typeof-Typ: {value}",
        "{prefix}: expected at most {maxArgCount} positional arguments, but got {argCount}.": "{prefix}: erwartet wurden höchstens {maxArgCount} Positionsargumente, aber {argCount} wurden erhalten.",
        "{prefix}: expected at least {posOnlyCount} positional arguments, but got only {argCount}.": "{prefix}: erwartet wurden mindestens {posOnlyCount} Positionsargumente, aber nur {argCount} wurden erhalten.",
        "Setter methods must return {nothingValue}.": "Setter-Methoden müssen {nothingValue} zurückgeben.",
        "Undefined {expectedMemberType} {name}.": "Nicht definierte(r/s) {expectedMemberType} {name}.",
        "Class Method or Variable {name} is not a {expectedMemberType} but a {type}.": "Klassenmethode oder -variable {name} ist kein(e) {expectedMemberType}, sondern ein(e) {type}.",
        "Can not assign {newMemberType}: {currentMemberType} already exists with the same name {name}.": "Kann {newMemberType} nicht zuweisen: {currentMemberType} mit demselben Namen {name} existiert bereits.",
        "Initialization methods must return {nothingValue}.": "Initialisierungsmethoden müssen {nothingValue} zurückgeben.",
        "Can not call super instance method: class has no superclass.": "Kann Super-Instanzmethode nicht aufrufen: Die Klasse hat keine Superklasse.",
        "{instanceValue} has no attribute or getter method for {name}.": "{instanceValue} hat kein Attribut oder keine Getter-Methode für {name}.",
        "Can not set attribute {name} of {instanceValue}: attribute only has a getter method.": "Kann Attribut {name} von {instanceValue} nicht setzen: Das Attribut hat nur eine Getter-Methode.",
        "As String methods must always return a string.": "As-String-Methoden müssen immer einen String zurückgeben.",
        "Comparison Operator methods must always return a boolean.": "Vergleichsoperator-Methoden müssen immer einen Wahrheitswert (Boolean) zurückgeben.",

        // MENUS
        "instance method": "Instanzmethode",
        "static method": "statische Methode",
        "getter method": "Getter-Methode",
        "setter method": "Setter-Methode",
        "operator method": "Operator-Methode",
        "class variable": "Klassenvariable",

        "init": "initialisierung",
        "as string": "als Zeichenfolge",

        "left add": "linke Addition",
        "right add": "rechte Addition",
        "left subtract": "linke Subtraktion",
        "right subtract": "rechte Subtraktion",
        "left multiply": "linke Multiplikation",
        "right multiply": "rechte Multiplikation",
        "left divide": "linke Division",
        "right divide": "rechte Division",
        "left power": "linke Potenzierung",
        "right power": "rechte Potenzierung",
        "left mod": "linkes Modulo",
        "right mod": "rechtes Modulo",
        "equals": "gleich",
        "not equals": "ungleich",
        "greater than": "größer als",
        "greater or equal": "größer oder gleich",
        "less than": "kleiner als",
        "less or equal": "kleiner oder gleich",

        // CAST
        "Unknown (non-runtime environment)": "Unbekannt (Nicht-Laufzeitumgebung)",
        "class or class variable name": "Klasse oder Klassenvariablenname",
        "class instance or class instance variable name": "Klasseninstanz oder Klasseninstanzvariablenname",
        "function or function variable name": "Funktion oder Funktionsvariablenname",

        // getInfo defaults
        "myFunction": "meineFunktion",
        "MyClass": "MeineKlasse",
        "MySubclass": "MeineUnterklasse",
        "myInstance": "meineInstanz",
        "myMethod": "meineMethode",
        "myClassVariable": "meineKlassenvariable",
        "myAttr": "meinAttribut",

        // getInfo block texts
        "OOP": "OOP",
        "Missing Extensions?": "Fehlen Erweiterungen?",
        "Add Functions & Scopes Extension": "Funktionen & Variablen Erweiterung hinzufügen",
        "Add Array Extension": "Array-Erweiterung hinzufügen",
        "Add Object Extension": "Objekt-Erweiterung hinzufügen",
        "Define Classes": "Klassen definieren",
        "create class at var [NAME] [SHADOW]": "Erstelle Klasse bei Variable [NAME] [SHADOW]",
        "Creates a new class, stores it in the chosen variable.": "Erstellt eine neue Klasse und speichert sie in der gewählten Variable.",
        "create subclass at var [NAME] with superclass [SUPERCLASS] [SHADOW]": "Erstelle Unterklasse bei Variable [NAME] mit Oberklasse [SUPERCLASS] [SHADOW]",
        "Creates a subclass with the given superclass, stores it in a variable.": "Erstellt eine Unterklasse mit der angegebenen Oberklasse und speichert sie in einer Variable.",
        "create class named [NAME] [SHADOW]": "Erstelle Klasse mit Namen [NAME] [SHADOW]",
        "Creates and returns a new class with the given name.": "Erstellt und gibt eine neue Klasse mit dem angegebenen Namen zurück.",
        "create subclass named [NAME] with superclass [SUPERCLASS] [SHADOW]": "Erstelle Unterklasse mit Namen [NAME] und Oberklasse [SUPERCLASS] [SHADOW]",
        "Creates and returns a new subclass with the given superclass.": "Erstellt und gibt eine neue Unterklasse mit der angegebenen Oberklasse zurück.",
        "on class [CLASS] [SHADOW]": "Mit Klasse [CLASS] [SHADOW]",
        "Runs the enclosed blocks as if they were inside the selected class definition. This allows you to e.g. add methods to already defined classes.": "Führt die eingeschlossenen Blöcke aus, als wären sie innerhalb der ausgewählten Klassendefinition. Dies ermöglicht z.B. das Hinzufügen von Methoden zu bereits definierten Klassen.",
        "current class": "aktuelle Klasse",
        "Returns the class currently being defined.": "Gibt die Klasse zurück, die gerade definiert wird.",
        "Use Classes": "Klassen verwenden",
        "is [SUBCLASS] a subclass of [SUPERCLASS] ?": "Ist [SUBCLASS] eine Unterklasse von [SUPERCLASS]?",
        "Checks whether one class inherits from another.": "Prüft, ob eine Klasse von einer anderen erbt.",
        "get superclass of [CLASS]": "Oberklasse von [CLASS] abrufen",
        "Returns the superclass of a class, or Nothing if it has none.": "Gibt die Oberklasse einer Klasse zurück oder Nichts, falls keine vorhanden ist.",
        "Class Members": "Klassenmitglieder",
        "Define Instance Methods": "Instanzmethoden definieren",
        "define instance method [NAME] [SHADOW]": "Instanzmethode [NAME] [SHADOW] definieren",
        "Defines an instance method on the current class.": "Definiert eine Instanzmethode in der aktuellen Klasse.",
        "define [SPECIAL_METHOD] instance method [SHADOW]": "[SPECIAL_METHOD] Instanzmethode [SHADOW] definieren",
        "Defines a special instance method.": "Definiert eine spezielle Instanzmethode.",
        "self": "self",
        "Reports the current instance inside a method.": "Gibt die aktuelle Instanz innerhalb einer Methode zurück.",
        "call super method [NAME] with positional args [POSARGS]": "Super-Methode [NAME] mit Positionsargumenten [POSARGS] aufrufen",
        "Calls an instance method from the superclass of the current object.": "Ruft eine Instanzmethode der Oberklasse des aktuellen Objekts auf.",
        "call super init method with positional args [POSARGS]": "Super-Init-Methode mit Positionsargumenten [POSARGS] aufrufen",
        "Calls the superclass init method for the current object.": "Ruft die Init-Methode der Oberklasse für das aktuelle Objekt auf.",
        "Define Getters & Setters": "Getter & Setter definieren",
        "define getter [NAME] [SHADOW]": "Getter [NAME] [SHADOW] definieren",
        "Defines a getter method for an attribute on the current class.": "Definiert eine Getter-Methode für ein Attribut in der aktuellen Klasse.",
        "define setter [NAME] [SHADOW1] [SHADOW2]": "Setter [NAME] [SHADOW1] [SHADOW2] definieren",
        "Defines a setter method for an attribute on the current class.": "Definiert eine Setter-Methode für ein Attribut in der aktuellen Klasse.",
        "operator value": "Operatorwert",
        "Reports the incoming value inside a setter method.": "Gibt den eingehenden Wert innerhalb einer Setter-Methode zurück.",
        "Define Operator Methods": "Operatormethoden definieren",
        "define operator method [OPERATOR_KIND] [SHADOW]": "Operatormethode [OPERATOR_KIND] [SHADOW] definieren",
        "Defines custom behavior for an operator on instances of the current class.": "Definiert benutzerdefiniertes Verhalten für einen Operator bei Instanzen der aktuellen Klasse.",
        "operator value": "Operatorwert",
        "Reports the other operand inside an operator method.": "Gibt den anderen Operanden innerhalb einer Operatormethode zurück.",
        "Define Static Methods & Class Variables": "Statische Methoden & Klassenvariablen definieren",
        "on [CLASS] set class var [NAME] to [VALUE]": "Setze Klassenvariable [NAME] von [CLASS] auf [VALUE]",
        "Sets a class variable on the selected class.": "Setzt eine Klassenvariable in der ausgewählten Klasse.",
        "get class var [NAME] of [CLASS]": "Klassenvariable [NAME] von [CLASS] abrufen",
        "Gets a class variable from the selected class.": "Liest eine Klassenvariable aus der ausgewählten Klasse aus.",
        "on [CLASS] delete class var [NAME]": "Lösche Klassenvariable [NAME] von [CLASS]",
        "Deletes a class variable from the selected class.": "Löscht eine Klassenvariable aus der ausgewählten Klasse.",
        "define static method [NAME]": "Statische Methode [NAME] definieren",
        "Defines a static method on the current class.": "Definiert eine statische Methode in der aktuellen Klasse.",
        "[PROPERTY] names of class [CLASS]": "[PROPERTY]-Namen der Klasse [CLASS]",
        "Returns the names of members of the selected type for a class.": "Gibt die Namen der Mitglieder des ausgewählten Typs für eine Klasse zurück.",
        "Working with Instances": "Mit Instanzen arbeiten",
        "Create & Inspect": "Erstellen & Untersuchen",
        "create instance of class [CLASS] with positional args [POSARGS]": "Instanz der Klasse [CLASS] mit Positionsargumenten [POSARGS] erstellen",
        "Creates an instance of a class and passes the given positional arguments to its init method.": "Erstellt eine Instanz einer Klasse und übergibt die angegebenen Positionsargumente an deren Init-Methode.",
        "is [INSTANCE] an instance of [CLASS] ?": "Ist [INSTANCE] eine Instanz von [CLASS]?",
        "Checks whether an instance belongs to a class or one of its subclasses.": "Prüft, ob eine Instanz zu einer Klasse oder einer ihrer Unterklassen gehört.",
        "get class of [INSTANCE]": "Klasse von [INSTANCE] abrufen",
        "Returns the class that created an instance.": "Gibt die Klasse zurück, die eine Instanz erstellt hat.",
        "Attributes": "Attribute",
        "on [INSTANCE] set attribute [NAME] to [VALUE]": "Setze Attribut [NAME] von [INSTANCE] auf [VALUE]",
        "Sets an attribute on an instance or calls its setter if one exists.": "Setzt ein Attribut einer Instanz oder ruft deren Setter auf, falls vorhanden.",
        "on [INSTANCE] get attribute [NAME]": "Attribut [NAME] von [INSTANCE]",
        "Gets an attribute from an instance or calls its getter if one exists.": "Liest ein Attribut einer Instanz aus oder ruft deren Getter auf, falls vorhanden.",
        "all attributes of [INSTANCE]": "Alle Attribute von [INSTANCE]",
        "Returns all direct instance attributes as an object.": "Gibt alle direkten Instanzattribute als Objekt zurück.",
        "Call Methods": "Methoden aufrufen",
        "on [INSTANCE] call method [NAME] with positional args [POSARGS]": "Methode [NAME] von [INSTANCE] mit Positionsargumenten [POSARGS] aufrufen",
        "Calls an instance method on an object with positional arguments.": "Ruft eine Instanzmethode eines Objekts mit Positionsargumenten auf.",
        "on [CLASS] call static method [NAME] with positional args [POSARGS]": "Statische Methode [NAME] von [CLASS] mit Positionsargumenten [POSARGS] aufrufen",
        "Calls a static method on a class with positional arguments.": "Ruft eine statische Methode einer Klasse mit Positionsargumenten auf.",
        "get static method [NAME] of [CLASS] as function": "Statische Methode [NAME] von [CLASS] als Funktion abrufen",
        "Returns a static method from a class as a callable function value.": "Gibt eine statische Methode einer Klasse als aufrufbare Funktion zurück.",

        // parts of getInfo block texts
        "define method": "Methode definieren",
    },
};

// Add underscore to every key in every value of TRANSLATIONS, because Scratch.translate expects it
Object.entries(TRANSLATIONS).forEach(([lang, langTranslations]) => {
    Object.keys(langTranslations).forEach(key => {
        langTranslations["_" + key] = langTranslations[key];
        delete langTranslations[key];
    });
});
Scratch.translate.setup(TRANSLATIONS);

/************************************************************************************
*                                Custom Block Shapes                                *
************************************************************************************/

let CUSTOM_SHAPE
if (isRuntimeEnv) {
    try { // If ScratchBlocks is not avaliable, skip
    CUSTOM_SHAPE = {
        emptyInputPath: "m 16 0 h 16 h 12 a 4 4 0 0 1 4 4 l -4 4 l 4 4 l 0 8 l -4 4 l 4 4 a 4 4 0 0 1 -4 4 h -12 h -16 h -12 a 4 4 0 0 1 -4 -4 l 4 -4 l -4 -4 l 0 -8 l 4 -4 l -4 -4 a 4 4 0 0 1 4 -4 z",
        emptyInputWidth: 10 * ScratchBlocks.BlockSvg.GRID_UNIT,
        leftPath: (block) => {
            const edgeWidth = block.height / 2
            const s = edgeWidth / 16
            return [
                `h ${-12*s} `+
                `a ${4*s} ${4*s} 0 0 1 ${-4*s} ${-4*s} `+
                `l ${4*s} ${-4*s} `+
                `l ${-4*s} ${-4*s} `+
                `l 0 ${-8*s} `+
                `l ${4*s} ${-4*s} `+
                `l ${-4*s} ${-4*s} `+
                `a ${4*s} ${4*s} 0 0 1 ${4*s} ${-4*s}`
            ]
        },
        rightPath: (block) => {
            const edgeWidth = block.edgeShapeWidth_
            const s = edgeWidth / 16
            return [
                `h ${12*s} `+
                `a ${4*s} ${4*s} 0 0 1 ${4*s} ${4*s}`+
                `l ${-4*s} ${4*s} `+
                `l ${4*s} ${4*s} `+
                `l 0 ${8*s} `+
                `l ${-4*s} ${4*s} `+
                `l ${4*s} ${4*s} `+
                `a ${4*s} ${4*s} 0 0 1 ${-4*s} ${4*s}`+
                `h ${-12*s}`
            ]
        },
    }
    } catch (error) {
        console.error(translatedMsg("[OOP Extension] Failed to create custom shape"), error)
    }
}

/************************************************************************************
*                             Wrapping Some PM Internals                            *
************************************************************************************/

/**
 * @param {ScratchObject} Scratch
 */
function applyInternalWrappers(Scratch) {
    const {IRGenerator, JSGenerator} = Scratch.vm.exports
    const {TypedInput, TYPE_UNKNOWN, TYPE_BOOLEAN} = JSGenerator.exports
    const ScriptTreeGenerator = IRGenerator.exports.ScriptTreeGenerator

    // wrap Scratch.Cast.toBoolean to return false for Nothing
    const oldToBoolean = Scratch.Cast.toBoolean
    
    // Avoid multiple wrappings
    if (!oldToBoolean.isGceOOPModified) {
        /**
         * @param {*} value
         * @returns {boolean}
         */
        Scratch.Cast.toBoolean = function modifiedToBoolean(value) {
            if (value instanceof NothingType) return false
            return oldToBoolean(value)
        }
        Scratch.Cast.toBoolean.isGceOOPModified = true
    }

    // Wrap ScriptTreeGenerator.descendInput to make
    // notequals, ltorequal and gtorequal compiled blocks (as the other comparison blocks are)
    // CAN BE REMOVED START: IF THIS IS MERGED: https://github.com/PenguinMod/PenguinMod-Vm/pull/188
    const oldDescendTreeGenInput = ScriptTreeGenerator.prototype.descendInput

    if (!oldDescendTreeGenInput.isGceOOPModified) {
        /**
         * @param {Object} block
         */
        ScriptTreeGenerator.prototype.descendInput = function modifiedDescendInput (block) {
            switch (block.opcode) {
                case "operator_notequal":
                case "operator_gtorequal":
                case "operator_ltorequal":
                    const input = {
                        left: this.descendInputOfBlock(block, "OPERAND1"),
                        right: this.descendInputOfBlock(block, "OPERAND2"),
                    }
                    if      (block.opcode === "operator_notequal") input.kind = "op.notequal"
                    else if (block.opcode === "operator_gtorequal") input.kind = "op.gtorequal"
                    else if (block.opcode === "operator_ltorequal") input.kind = "op.ltorequal"
                    return input
            }
            return oldDescendTreeGenInput.call(this, block)
        }
        ScriptTreeGenerator.prototype.descendInput.isGceOOPModified = true
    }
    // CAN BE REMOVED END


    // Wrap JSGenerator.descendInput for some operator blocks to allow classes to define custom handling
    const oldDescendJSGenInput = JSGenerator.prototype.descendInput

    if (!oldDescendJSGenInput.isGceOOPModified) {
        /**
         * @param {Object} node
         * @param {boolean} visualReport
         */
        JSGenerator.prototype.descendInput = function modifiedDescendInput (node, visualReport = false) {
            const OPCODE_INFOS = {
                "op.add": {operatorKind: "math", leftMethod: "__OM_LEFT_ADD__", rightMethod: "__OM_RIGHT_ADD__"},
                "op.subtract": {operatorKind: "math", leftMethod: "__OM_LEFT_SUBTRACT__", rightMethod: "__OM_RIGHT_SUBTRACT__"},
                "op.multiply": {operatorKind: "math", leftMethod: "__OM_LEFT_MULTIPLY__", rightMethod: "__OM_RIGHT_MULTIPLY__"},
                "op.divide": {operatorKind: "math", leftMethod: "__OM_LEFT_DIVIDE__", rightMethod: "__OM_RIGHT_DIVIDE__"},
                "op.mod": {operatorKind: "math", leftMethod: "__OM_LEFT_MOD__", rightMethod: "__OM_RIGHT_MOD__"},
                "op.power": {operatorKind: "math", leftMethod: "__OM_LEFT_POWER__", rightMethod: "__OM_RIGHT_POWER__"},

                "op.equals": {operatorKind: "comparison", leftMethod: "__OM_EQUALS__", rightMethod: "__OM_EQUALS__"},
                "op.notequal": {operatorKind: "comparison", leftMethod: "__OM_NOT_EQUALS__", rightMethod: "__OM_NOT_EQUALS__"},
                "op.greater": {operatorKind: "comparison", leftMethod: "__OM_GREATER_THAN__", rightMethod: "__OM_LESS_THAN__"},
                "op.gtorequal": {operatorKind: "comparison", leftMethod: "__OM_GREATER_OR_EQUAL__", rightMethod: "__OM_LESS_OR_EQUAL__"},
                "op.less": {operatorKind: "comparison", leftMethod: "__OM_LESS_THAN__", rightMethod: "__OM_GREATER_THAN__"},
                "op.ltorequal": {operatorKind: "comparison", leftMethod: "__OM_LESS_OR_EQUAL__", rightMethod: "__OM_GREATER_OR_EQUAL__"},
            }
            
            if (!(node.kind in OPCODE_INFOS)) {
                return oldDescendJSGenInput.call(this, node, visualReport)
            }

            const operatorKind = OPCODE_INFOS[node.kind]
            const leftMethod = quote(OPCODE_INFOS[node.kind].leftMethod)
            const rightMethod = quote(OPCODE_INFOS[node.kind].rightMethod)
            const leftCode = this.descendInput(node.left).asUnknown()
            const rightCode = this.descendInput(node.right).asUnknown()

            if (node.kind === "op.mod") this.descendedIntoModulo = true // ¯\_(ツ)_/¯ this seems to be necessary
            
            let handlerMethod
            switch (operatorKind.operatorKind) {
                case "math":
                    handlerMethod = "_binaryOperator"
                    break;
                case "comparison":
                    handlerMethod = "_comparisonOperator"
                    break;
                default: // Should never happen
                    throwInternal("lively-lynx")
            }
            // I cannot really use optimizations here
            return new TypedInput(`(yield* runtime.ext_gceOOP.${handlerMethod}(thread, ${leftCode}, ${rightCode}, ${leftMethod}, ${rightMethod}, ${quote(node.kind)}))`, TYPE_UNKNOWN)
        }
        JSGenerator.prototype.descendInput.isGceOOPModified = true
    }


    // Wrap Runtime._convertBlockForScratchBlocks to implement hover tooltips
    const oldConvertBlock = runtime._convertBlockForScratchBlocks.bind(runtime);

    if (!oldConvertBlock.isGceOOPModified) {
        /**
         * @param {Object} blockInfo
         * @param {Object} categoryInfo
         */
        runtime._convertBlockForScratchBlocks = function(blockInfo, categoryInfo) {
            const result = oldConvertBlock(blockInfo, categoryInfo);
            if (blockInfo.tooltip) {
                result.json.tooltip = blockInfo.tooltip
            }
            return result;
        }
        runtime._convertBlockForScratchBlocks.isGceOOPModified = true
    }
}

/************************************************************************************
*                            Internal Types and Constants                           *
************************************************************************************/

/**
 * @param {string} s
 * @returns {string}
 */
function quote(s) {
    if (typeof s !== "string") s = String(s)
    s = s.replace(/\\/g, "\\\\").replace(/'/g, "\\'")
    return `'${s}'`
}

/**
 * @param {string} text
 * @returns {string}
 */
function escapeHTML(text) {
    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;")
}

/**
 * @param {string} text
 * @returns {HTMLSpanElement}
 */
function span(text) {
    let element = document.createElement("span")
    element.innerHTML = escapeHTML(text)
    element.style.display = "hidden"
    element.style.width = "100%"
    element.style.textAlign = "center"
    return element
}

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
    if (deTranslations["__" + key] === null) {
        // Purposefully untranslated, return the English message template
        return Scratch.translate(englishMessageTemplate, values);
    } else if (!deTranslations || (deTranslations["_" + key] === undefined)) {
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
        "An internal error occured in the OOP extension. Please report it in the PenguinMod discord or on GitHub. {additionalMsg} [ERROR CODE: {code}]", {additionalMsg, code}
    )
}

/**
 * Ensure that no unintended types are handed to the user.
 * @template T
 * @param {string} errorCode 
 * @param {new (...args: any[]) => T} type
 * @param {*} value
 * @returns {T}
 */
function assertType(errorCode, type, value) {
    if (!(value instanceof type)) {
        throwInternal(errorCode)
    }
    return value
}

/**
 * Manages variables for a scope. ValueHolder can be referenced from multiple VariableManager instances.
 */
class VariableManager {
    /**
     * Implements a value storage, that can be set from multiple locations.
     */
    ValueHolder = class {
        /**
         * @param {*} value
         */
        constructor(value) {
            this.value = value
            this.isDeleted = false
        }
    }

    /**
     * @param {?Object<string, *>} startVars
     */
    constructor(startVars = null) {
        this.reset()
        if (startVars) {
            for (const [name, value] of Object.entries(startVars)) {
                this.set(name, value)
            }
        }
    }
    reset() {
        if (this._variables !== undefined) {
            this.getNames().forEach((name) => this.delete(name, false))
        }
        this._variables = {}
    }

    /**
     * @param {string} name
     * @param {*} value
     */
    set(name, value) {
        if (this.has(name)) {
            this._variables[name].value = value
        } else {
            this._variables[name] = new this.ValueHolder(value)
        }
    }

    /**
     * @param {string} name
     * @param {VariableManager.ValueHolder} holder
     */
    setHolder(name, holder) {
        if (this.has(name)) {
            throwError("Variable {name} already exists in the current scope, can not bind variable with the same name."), {name: quote(name)}
        }
        this._variables[name] = holder
    }

    /**
     * @param {string} name
     * @param {boolean} throwOnNotFound
     */
    delete(name, throwOnNotFound = true) {
        if (this.has(name)) {
            this._variables[name].isDeleted = true // Mark the variable deleted for all scopes
            delete this._variables[name]
        } else if (throwOnNotFound) {
            throwError("Variable {name} is not defined.", {name: quote(name)})
        }
    }

    /**
     * @param {string} name
     * @returns {boolean}
     */
    has(name) {
        return (name in this._variables) && (!this._variables[name].isDeleted)
    }

    /**
     * @param {string} name
     * @param {boolean} throwOnNotFound
     */
    get(name, throwOnNotFound = true) {
        if (!this.has(name)) {
            if (!throwOnNotFound) return undefined
            throwError("Variable {name} is not defined.", {name: quote(name)})
        }
        return this._variables[name].value
    }

    /**
     * @returns {Object<string, *>}
     */
    getAll() {
        const result = {}
        this.getNames().forEach((name) => {
            result[name] = this.get(name, true)
        })
        return result
    }

    /**
     * @param {string} name
     * @returns {VariableManager.ValueHolder}
     */
    getHolder(name) {
        if (!this.has(name)) {
            throwError("Variable {name} is not defined.", {name: quote(name)})
        }
        return this._variables[name]
    }

    /**
     * @returns {Array<string>} 
     */
    getNames() {
        return Object.keys(this._variables).filter(name => this.has(name))
    }
}

class ThreadUtil {
    /**
     * @param {Thread} thread
     * @returns {ScopeStackManager}
     */
    static getStackManager(thread) {
        thread.gceSSM ??= new ScopeStackManager()
        return thread.gceSSM
    }

    /**
     * @param {Thread} thread
     * @returns {ScopeStack}
     */
    static getCurrentStack(thread) {
        return ThreadUtil.getStackManager(thread).getCurrentStackFromManager()
    }

    /**
     * @param {Thread} thread
     * @param {ScopeStack} stack
     */
    static pushStack(thread, stack) {
        ThreadUtil.getStackManager(thread).pushStackToManager(stack)
    }

    /**
     * @param {Thread} thread
     */
    static popStack(thread) {
        return ThreadUtil.getStackManager(thread).popStackFromManager()
    }
}

// System to switch between multiple ScopeStack's (e.g. for different scopes in function calls)
class ScopeStackManager {
    constructor() {
        /** @type {Array<ScopeStack>} */
        this.stacks = [new ScopeStack()]; // Live default stack
    }

    /**
     * @returns {ScopeStack}
     */
    getCurrentStackFromManager() {
        return this.stacks[this.stacks.length - 1]
    }

    /**
     * @param {ScopeStack} stack
     */
    pushStackToManager(stack) {
        this.stacks.push(stack)
    }

    /**
     * @returns {ScopeStack}
     */
    popStackFromManager() {
        if (this.stacks.length <= 1) {
            throwInternal("stoic-penguin")
        }
        return this.stacks.pop();
    }

    // Enter Scopes

    /**
     * @param {BaseCallableType} callable
     * @param {ContextScope} scope
     */
    insertScopeAndPushStack(callable, scope) {
        const callableStack = callable.stack.shallowCopy()
        callableStack.insertScope(scope)
        this.pushStackToManager(callableStack)
    }

    /**
     * @param {BaseCallableType} callable
     * @param {Object<string, *>} args
     */
    enterFunctionCall(callable, args) {
        this.insertScopeAndPushStack(callable, {
            type: ScopeStack.FUNCTION,
            isCallable: true, supportsVars: true,
            vars: new VariableManager(args),
        })
    }

    /**
     * @param {BaseCallableType} callable
     * @param {ClassInstanceType} self
     * @param {Object<string, *>} args
     */
    enterMethodCall(callable, self, args) {
        this.insertScopeAndPushStack(callable, {
            type: ScopeStack.METHOD,
            supportsSelf: true, isCallable: true,
            supportsVars: true,
            self, vars: new VariableManager(args),
        })
    }

    /**
     * @param {BaseCallableType} callable
     * @param {ClassInstanceType} self
     */
    enterGetterMethodCall(callable, self) {
        this.insertScopeAndPushStack(callable, {
            type: ScopeStack.GETTER_METHOD,
            supportsSelf: true, isCallable: true,
            supportsVars: true,
            self, vars: new VariableManager(),
        })
    }

    /**
     * @param {BaseCallableType} callable
     * @param {ClassInstanceType} self
     * @param {*} setterValue
     */
    enterSetterMethodCall(callable, self, setterValue) {
        this.insertScopeAndPushStack(callable, {
            type: ScopeStack.SETTER_METHOD,
            supportsSelf: true, supportsSetterValue: true, isCallable: true,
            supportsVars: true,
            self, setterValue, vars: new VariableManager(),
        })
    }

    /**
     * @param {BaseCallableType} callable
     * @param {ClassInstanceType} self
     * @param {*} operatorValue
     */
    enterOperatorMethodCall(callable, self, operatorValue) {
        this.insertScopeAndPushStack(callable, {
            type: ScopeStack.OPERATOR_METHOD,
            supportsSelf: true, supportsOperatorValue: true, isCallable: true,
            supportsVars: true,
            self, operatorValue, vars: new VariableManager(),
        })
    }

    // Exit Scopes
    prepareReturn() {
        this.getCurrentStackFromManager().assertCanReturn()
        this.popStackFromManager()
    }

    // Measure Scopes

    /**
     * @returns {number}
     */
    getSize() {
        return this.stacks.length
    }

    /**
     * @param {number} size
     */
    trimSize(size) {
        if (size < 0) size = 0
        if (this.stacks.length <= size) return
        this.stacks.splice(0, this.stacks.length - size)
    }
}

// System for storing scope-like data
class ScopeStack {
    static GLOBALS = "GLOBALS"
    static FUNCTION = "FUNCTION"
    static METHOD = "METHOD"
    static GETTER_METHOD = "GETTER_METHOD"
    static SETTER_METHOD = "SETTER_METHOD"
    static OPERATOR_METHOD = "OPERATOR_METHOD"
    static CLASS_DEF = "CLASS_DEF"
    static USER_SCOPE = "USER_SCOPE"

    constructor() {

        /** @type {Array<ContextScope>} */
        this.scopes = [{
            type: ScopeStack.GLOBALS,
            isGlobalScope: true, supportsVars: true,
            vars: extensionClassInstance.globalVariables,
        }] // Item 0 is innermost
        // Use the global variables manager for all global scopes
        this.setNextFuncConfig()
    }

    /**
     * @returns {ScopeStack}
     */
    shallowCopy() { // Keep the same scope instances, but within a new array
        const newStack = new ScopeStack()
        newStack.scopes = [...this.scopes]
        return newStack
    }

    // Enter Scopes

    /**
     * @param {ContextScope} scope
     */
    insertScope(scope) {
        this.scopes.splice(0, 0, scope)
    }

    /**
     * @param {ClassType} cls
     */
    enterClassDefScope(cls) {
        this.insertScope({
            type: ScopeStack.CLASS_DEF,
            supportsCls: true,
            cls,
        })
    }

    enterUserScope() {
        this.insertScope({
            type: ScopeStack.USER_SCOPE,
            isUserScope: true,
            supportsVars: true,
            vars: new VariableManager(),
        })
    }

    // Get Scope

    /**
     * @param {function(ContextScope): boolean} qualified_fn
     * @returns {?ContextScope}
     */
    _getQualifiedScope(qualified_fn) {
        for (let i = 0; i < this.scopes.length; i++) {
            if (qualified_fn(this.scopes[i])) {
                return this.scopes[i]
            }
        }
        return null
    }

    /**
     * @returns {ContextScope}
     */
    _getInnermostScope() {
        const scope = this.scopes[0]
        if (!scope) {
            throwInternal("bold-koala")
        }
        return scope
    }

    /**
     * @returns {ClassInstanceType}
     */
    getSelfOrThrow() {
        const scope = this._getQualifiedScope(scope => scope.supportsSelf)
        if (!scope) {
            throwError("self can only be used within an instance, getter or setter method.")
        }
        return scope.self
    }

    /**
     * @returns {*}
     */
    getSetterValueOrThrow() {
        const scope = this._getQualifiedScope(scope => scope.supportsSetterValue)
        if (!scope) {
            throwError("setter value can only be used within a setter method.")
        }
        return scope.setterValue
    }

    /**
     * @returns {*}
     */
    getOperatorValueOrThrow() {
        const scope = this._getQualifiedScope(scope => scope.supportsOperatorValue)
        if (!scope) {
            throwError("operator value can only be used within an operator method.")
        }
        return scope.operatorValue
    }

    /**
     * @param {string} blockText
     * @returns {ClassType}
     */
    getClsOrThrow(blockText) {
        blockText = translatedMsg(blockText)
        const innermost = this._getInnermostScope()
        if (!innermost.supportsCls) {
            throwError('{blockText} can only be used within a class definition or "on class" block.', {blockText})
        }
        return innermost.cls
    }

    // Exit Scopes
    assertCanReturn() {
        const innermost = this._getInnermostScope()
        if (!innermost.isCallable) {
            throwError("return can only be used within a function or method.")
        }
    }
    exitClassDefScope() {
        const innermost = this._getInnermostScope()
        if (!innermost.supportsCls) {
            throwInternal("nimble-panda")
        }
        this.scopes.shift()
    }
    exitUserScope() {
        const innermost = this._getInnermostScope()
        if (!innermost.isUserScope) {
            throwInternal("curious-otter")
        }
        this.scopes.shift()
    }

    // Measure Scopes

    /**
     * @returns {number} 
     */
    getSize() {
        return this.scopes.length
    }

    /**
     * @param {number} size
     */
    trimSize(size) {
        if (size < 0) size = 0
        if (this.scopes.length <= size) return
        this.scopes.splice(0, this.scopes.length - size)
    }

    // Function Arguments

    /**
     * @param {?FunctionArgConfig} config
     */
    setNextFuncConfig(config) {
        config = config || ScopeStack.getDefaultFuncConfig()
        if (config.argDefaults.length > config.argNames.length) {
            throwError("There can only be as many default values as argument names.")
        }
        this.nextFuncConfig = config
    }

    /**
     * @returns {FunctionArgConfig}
     */
    getAndResetNextFuncConfig() {
        const config = this.nextFuncConfig
        this.setNextFuncConfig()
        return config
    }

    /**
     * @returns {FunctionArgConfig}
     */
    static getDefaultFuncConfig() {
        return {argNames: [], argDefaults: []}
    }

    // Access Scoped Variables

    /**
     * @param {string} name
     * @param {*} value
     */
    setScopeVar(name, value) {
        const innermost = this._getInnermostScope()
        if (!innermost.supportsVars) {
            throwError("Can not set a variable in a scope, which does not support variables (e.g. a class definition).")
        }
        innermost.vars.set(name, value)
    }

    /**
     * @param {string} name
     * @param {number} startIndex
     * @param {number} excludeLastIndecies
     * @param {boolean} throwOnNotFound
     * @returns {?ContextScope}
     */
    _getScopeOfVar(name, startIndex = 0, excludeLastIndecies = 0, throwOnNotFound = true) {
        for (let i = startIndex; i < (this.scopes.length - excludeLastIndecies); i++) {
            const scope = this.scopes[i]
            if (!scope.supportsVars) continue
            if (scope.vars.has(name)) return scope
        }
        if (!throwOnNotFound) {
            return null
        }
        // trick to raise:
        (new VariableManager()).get(name, true)
    }

    /**
     * @param {string} name
     * @param {boolean} throwOnNotFound
     * @returns {*}
     */
    getScopeVar(name, throwOnNotFound = true) {
        const varScope = this._getScopeOfVar(name, 0, 0, throwOnNotFound)
        if (!varScope) return undefined
        return varScope.vars.get(name, throwOnNotFound)
    }

    /**
     * @param {string} name
     */
    deleteScopeVar(name) {
        const innermost = this._getInnermostScope()
        if (!innermost.supportsVars) {
            throwError("Can not delete a variable in a scope, which does not support variables(e.g. a class definition).")
        }
        innermost.vars.delete(name)
    }

    /**
     * @param {string} name
     */
    bindScopeVarGlobal(name) {
        const globalScope = this._getQualifiedScope(scope => scope.isGlobalScope)
        if (!globalScope) {
            throwInternal("calm-seal")
        }
        if (!globalScope.vars.has(name)) {
            throwError("No global variable named {name} found.", {name: quote(name)})
        }

        const innermost = this._getInnermostScope()
        if (!innermost.supportsVars) {
            throwError("Can not bind a variable to a scope, which does not support variables(e.g. a class definition).")
        }
        innermost.vars.setHolder(name, globalScope.vars.getHolder(name))
    }

    /**
     * @param {string} name
     */
    bindScopeVarNonlocal(name) {
        let varScope
        try { // skip innermost(current) and global scope, as nonlocal variables can not be in either
            varScope = this._getScopeOfVar(name, 1, 1)
        } catch {
            throwError("No non-local variable named {name} found.", {name: quote(name)})
        }

        const innermost = this._getInnermostScope()
        if (!innermost.supportsVars) {
            throwError("Can not bind a variable to a scope, which does not support variables(e.g. a class definition).")
        }
        innermost.vars.setHolder(name, varScope.vars.getHolder(name))
    }

    /**
     * @param {boolean} onlyCurrentScope - if true, return names only from the innermost scope
     * @param {boolean} onlyGlobalScope - if true, return names only from the global scope
    * @returns {boolean}
     */
    hasScopeVar(name, onlyCurrentScope = false, onlyGlobalScope = false) {
        if (onlyCurrentScope && onlyGlobalScope) {
            throwInternal("bold-raven")
        }
        if (onlyCurrentScope) {
            const innermost = this._getInnermostScope()
            if (!innermost.supportsVars) return false
            return innermost.vars.has(name)
        }
        if (onlyGlobalScope) {
            const globalScope = this._getQualifiedScope(scope => scope.isGlobalScope)
            if (!globalScope) throwInternal("spry-fox")
            if (!globalScope.supportsVars) throwInternal("toic-panda")
            return globalScope.vars.has(name)
        }
        return this._getScopeOfVar(name, 0, 0, false) !== null
    }

    /**
     * Return an array with all variable names visible in the current thread environment.
     * Iterates from outermost to innermost so inner-scope variables override outer ones.
     * @param {boolean} onlyCurrentScope - if true, return names only from the innermost scope
     * @param {boolean} onlyGlobalScope - if true, return names only from the global scope
     * @returns {Array<string>}
     */
    getScopeVarNames(onlyCurrentScope = false, onlyGlobalScope = false) {
        if (onlyCurrentScope && onlyGlobalScope) throwInternal("brave-fox")
        if (onlyCurrentScope) {
            const innermost = this._getInnermostScope()
            if (!innermost.supportsVars) return []
            return innermost.vars.getNames()
        }
        if (onlyGlobalScope) {
            const globalScope = this._getQualifiedScope(scope => scope.isGlobalScope)
            if (!globalScope) throwInternal("mirthful-seal")
            if (!globalScope.supportsVars) throwInternal("quiet-heron")
            return globalScope.vars.getNames()
        }

        const map = new Map()
        for (let i = this.scopes.length - 1; i >= 0; i--) {
            // iterate outermost -> innermost so inner scopes override outer ones
            const scope = this.scopes[i]
            if (!scope.supportsVars) continue
            const names = scope.vars.getNames()
            for (const n of names) {
                if (map.has(n)) map.delete(n)
                map.set(n, true)
            }
        }
        return Array.from(map.keys())
    }
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
    CLASS_PROPERTY: new MenuManager("Invalid class property: {value}", [
        {value: "CP_INSTANCE_METHOD", text: "instance method"},
        {value: "CP_STATIC_METHOD", text: "static method"},
        {value: "CP_GETTER_METHOD", text: "getter method"},
        {value: "CP_SETTER_METHOD", text: "setter method"},
        {value: "CP_OPERATOR_METHOD", text: "operator method"},
        {value: "CP_CLASS_VARIABLE", text: "class variable"},
    ].map(item => ({...item, text: translatedMsg(item.text)}))),

    SPECIAL_METHOD: new MenuManager("Invalid special method: {value}", [
        {value: "__SM_INIT_METHOD__", text: "init"},
        {value: "__SM_AS_STRING_METHOD__", text: "as string"},
    ].map(item => ({...item, text: translatedMsg(item.text)}))),

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
    ]), // Not translated on purpose, because that could result in different behaviour of scripts

    OPERATOR_METHOD: new MenuManager("Invalid operator method: {value}", [
        {value: "__OM_LEFT_ADD__", text: "left add"},
        {value: "__OM_RIGHT_ADD__", text: "right add"},
        {value: "__OM_LEFT_SUBTRACT__", text: "left subtract"},
        {value: "__OM_RIGHT_SUBTRACT__", text: "right subtract"},
        {value: "__OM_LEFT_MULTIPLY__", text: "left multiply"},
        {value: "__OM_RIGHT_MULTIPLY__", text: "right multiply"},
        {value: "__OM_LEFT_DIVIDE__", text: "left divide"},
        {value: "__OM_RIGHT_DIVIDE__", text: "right divide"},
        {value: "__OM_LEFT_POWER__", text: "left power"},
        {value: "__OM_RIGHT_POWER__", text: "right power"},
        {value: "__OM_LEFT_MOD__", text: "left mod"},
        {value: "__OM_RIGHT_MOD__", text: "right mod"},
        {value: "__OM_EQUALS__", text: "equals"},
        {value: "__OM_NOT_EQUALS__", text: "not equals"},
        {value: "__OM_GREATER_THAN__", text: "greater than"},
        {value: "__OM_GREATER_OR_EQUAL__", text: "greater or equal"},
        {value: "__OM_LESS_THAN__", text: "less than"},
        {value: "__OM_LESS_OR_EQUAL__", text: "less or equal"},
    ].map(item => ({...item, text: translatedMsg(item.text)}))),
}


class TypeChecker {
    // All custom types (using `customId`) in PM (you can access most from a reporter)
    // (PenguinMod-Vm, PenguinMod-ExtensionsGallery, SharkPools-Extensions) (as of 14.04.2026)
    // agBuffer (AndrewGaming587)
    // agBufferPointer (AndrewGaming587)
    // canvasData (RedMan13)
    // ddeDateFormat (ddededodediamante)
    // ddeDateFormatV2 (ddededodediamante)
    // divEffect (Div)
    // divIterator (Div)
    // dogeiscutObject (DogeisCut)
    // dogeiscutRegularExpression (DogeisCut)
    // dogeiscutSet (DogeisCut)
    // externaltimer (steve0greatness)
    // jwArray (jwklong)
    // jwColor (jwklong)
    // jwDate (jwklong)
    // jwLambda (jwklong)
    // jwNum (jwklong)
    // jwTarget (jwklong)
    // jwVector (jwklong)
    // jwXML (jwklong)
    // paintUtilsColour (Fruits555000)

    // My Types
    // FunctionType
    // InstanceMethodType (and subclasses)
    // ClassType
    // ClassInstanceType
    // NothingType

    static is_agBuffer = TypeChecker._createVMTypeCheck("agBuffer")
    static is_agBufferPointer = TypeChecker._createVMTypeCheck("agBuffer", "PointerType")
    
    /**
     * @param {*} value
     * @returns {boolean}
     */
    static is_canvasData(value) {
        TypeChecker._assertRuntimeEnv()
        if (!runtime._extensionVariables) return false
        const type = runtime._extensionVariables.canvas
        if (!type) return false
        return value instanceof type
    }

    /**
     * @param {*} value
     * @returns {boolean}
     */
    static is_ddeDateFormat(value) {
        TypeChecker._assertRuntimeEnv()
        if (runtime.ext_ddeDateFormat) {
            try {
                const dateType = Object.getPrototypeOf(runtime.ext_ddeDateFormat.currentDate()).constructor
                if (value instanceof dateType) return true
            } catch {}
        }
    }
    
    /**
     * @param {*} value
     * @returns {boolean}
     */
    static is_ddeDateFormatV2(value) {
        TypeChecker._assertRuntimeEnv()
        if (runtime.ext_ddeDateFormatV2) {
            try {
                const dateType = Object.getPrototypeOf(runtime.ext_ddeDateFormatV2.currentDate()).constructor
                if (value instanceof dateType) return true
            } catch {}
        }
        return false
    }

    static is_divEffect = TypeChecker._createVMTypeCheck("divAlgEffects", "Effect")
    static is_divIterator = TypeChecker._createVMTypeCheck("divIterator")
    static is_dogeiscutObject = TypeChecker._createVMTypeCheck("dogeiscutObject", null, "Object extension was not loaded properly.")
    static is_dogeiscutRegularExpression = TypeChecker._createVMTypeCheck("dogeiscutRegularExpression")
    static is_dogeiscutSet = TypeChecker._createVMTypeCheck("dogeiscutSet")

    /**
     * @param {*} value
     * @returns {boolean}
     */
    static is_externaltimer(value) {
        TypeChecker._assertRuntimeEnv()
        if (!runtime._extensionVariables) return false
        const type = runtime._extensionVariables.externaltimer
        if (!type) return false
        return value instanceof type
    }

    static is_jwArray = TypeChecker._createVMTypeCheck("jwArray", null, "Array extension was not loaded properly.")
    static is_jwColor = TypeChecker._createVMTypeCheck("jwColor")
    static is_jwDate = TypeChecker._createVMTypeCheck("jwDate")
    static is_jwLambda = TypeChecker._createVMTypeCheck("jwLambda")
    static is_jwNum = TypeChecker._createVMTypeCheck("jwNum")
    static is_jwTarget = TypeChecker._createVMTypeCheck("jwTargets")
    static is_jwVector = TypeChecker._createVMTypeCheck("jwVector")
    static is_jwXML = TypeChecker._createVMTypeCheck("jwXML")
    
    /**
     * @param {*} value
     * @returns {boolean}
     */
    static is_paintUtilsColour(value) {
        TypeChecker._assertRuntimeEnv()
        try {
            const proto = Object.getPrototypeOf(runtime.ext_fruitsPaintUtils.getColour({COLOUR_NAME: "orange"})).constructor
            return value instanceof proto
        } catch {
            return false
        }
    }



    static _assertRuntimeEnv() {
        if (!isRuntimeEnv) {
            throwError("Type checking for extension types is not available in a non-runtime environment.")
        }
    }

    /**
     * @param {string} typeId
     * @param {?string} [overrideTypeProperty]
     * @param {?string} [errMsg] - optional error message if type missing
     * @returns {(value: *) => boolean}
     */
    static _createVMTypeCheck(typeId, overrideTypeProperty = null, typeMissingErrorMsg = null) {
        return function isType(value) {
            if (!isRuntimeEnv) return false
            const typeInfo = Scratch.vm[typeId]
            if (!typeInfo) {
                if (typeMissingErrorMsg) throwError(typeMissingErrorMsg)
                return false
            }

            let typeClass
            try {
                typeClass = overrideTypeProperty ? typeInfo[overrideTypeProperty] : typeInfo.Type
            } catch {
                if (typeMissingErrorMsg) throwError(typeMissingErrorMsg)
                return false
            }
            return value instanceof typeClass
        }
    }

    /**
     * @param {*} value
     * @returns {boolean}
     */
    static isMissingValue(value) {
        return ((value === undefined) || (value === null))
    }

    /**
     * @param {*} value
     * @returns {boolean}
     */
    static isClassicScratchValue(value) {
        return ((typeof value === "boolean") || (typeof value === "number") || (typeof value === "string"))
    }

    /**
     * @param {*} value
     * @returns {string}
     */
    static typeofCode(value) {
        // My Types
        if (value instanceof FunctionType) return "TO_FUNCTION_GCE"
        if (value instanceof InstanceMethodType) return "TO_INSTANCE_METHOD_GCE"
        if (value instanceof GetterMethodType) return "TO_GETTER_METHOD_GCE"
        if (value instanceof SetterMethodType) return "TO_SETTER_METHOD_GCE"
        if (value instanceof OperatorMethodType) return "TO_OPERATOR_METHOD_GCE"

        if (value instanceof ClassType) return "TO_CLASS_GCE"
        if (value instanceof ClassInstanceType) return "TO_INSTANCE_GCE"
        if (value instanceof NothingType) return "TO_NOTHING_GCE"

        // Common/Safe JS data types
        if (value === undefined) return "TO_UNDEFINED_JS"
        if (value === null) return "TO_NULL_JS"
        if (typeof value === "boolean") return "TO_BOOLEAN"
        if (typeof value === "number") return "TO_NUMBER"
        if (typeof value === "string") return "TO_STRING"

        // Custom Extension Types 
        if (TypeChecker.is_agBuffer(value)) return "TO_BUFFER_AG587"
        if (TypeChecker.is_agBufferPointer(value)) return "TO_BUFFER_POINTER_AG587"
        if (TypeChecker.is_ddeDateFormat(value)) return "TO_DATE_OLD_DDE"
        if (TypeChecker.is_ddeDateFormatV2(value)) return "TO_DATE_DDE"
        if (TypeChecker.is_divEffect(value)) return "TO_EFFECT_DIV"
        if (TypeChecker.is_divIterator(value)) return "TO_ITERATOR_DIV"
        if (TypeChecker.is_dogeiscutObject(value)) return "TO_OBJECT_DOGEISCUT"
        if (TypeChecker.is_dogeiscutRegularExpression(value)) return "TO_REGEXP_DOGEISCUT"
        if (TypeChecker.is_dogeiscutSet(value)) return "TO_SET_DOGEISCUT"
        if (TypeChecker.is_externaltimer(value)) return "TO_EXTERNAL_TIMER_S0G"
        if (TypeChecker.is_jwArray(value)) return "TO_ARRAY_JWKLONG"
        if (TypeChecker.is_jwColor(value)) return "TO_COLOR_JWKLONG"
        if (TypeChecker.is_jwDate(value)) return "TO_DATE_JWKLONG"
        if (TypeChecker.is_jwLambda(value)) return "TO_LAMBDA_JWKLONG"
        if (TypeChecker.is_jwNum(value)) return "TO_NUMBER_JWKLONG"
        if (TypeChecker.is_jwTarget(value)) return "TO_TARGET_JWKLONG"
        if (TypeChecker.is_jwVector(value)) return "TO_VECTOR_JWKLONG"
        if (TypeChecker.is_jwXML(value)) return "TO_XML_JWKLONG"
        if (TypeChecker.is_canvasData(value)) return "TO_CANVAS_REDMAN13"
        if (TypeChecker.is_paintUtilsColour(value)) return "TO_PAINT_UTILS_COLOUR_FRUITS"

        // Rare/Overlapping JS data types
        if (typeof value === "bigint") return "TO_BIGINT_JS"
        if (typeof value === "symbol") return "TO_SYMBOL_JS"
        if (typeof value === "function") return "TO_FUNCTION_JS"
        if (typeof value === "object") return "TO_OBJECT_JS"

        return "TO_UNKNOWN"
    }

    /**
     * @param {*} value
     * @returns {string}
     */
    static stringTypeof(value) {
        if (isRuntimeEnv) {
            return MENUS.TYPEOF_MENU.internalToPublic(TypeChecker.typeofCode(value))
        } else {
            return translatedMsg("Unknown (non-runtime environment)")
        }
    }
}


class Cast extends Scratch.Cast {
    static _assertRuntimeEnv() {
        if (!isRuntimeEnv) {
            throwError("Casting to extension types is not available in a non-runtime environment.")
        }
    }

    // Foreign

    /**
     * @param {*} value
     * @returns {Scratch.vm.jwArray.Type}
     */
    static toArray(value) {
        Cast._assertRuntimeEnv()
        if (!Scratch.vm.jwArray) throwError("Array extension was not loaded properly.")
        return Scratch.vm.jwArray.Type.toArray(value)
    }

    /**
     * @param {*} value
     * @param {boolean} copy
     * @returns {Scratch.vm.dogeiscutObject.Type}
     */
    static toObject(value, copy = false) {
        Cast._assertRuntimeEnv()
        if (!Scratch.vm.dogeiscutObject) throwError("Object extension was not loaded properly.")
        return Scratch.vm.dogeiscutObject.Type.toObject(value, copy)
    }

    // Helpers

    /**
     * @param {string} name
     * @param {?Thread} thread
     * @param {boolean} throwOnNotFound
     * @returns {*}
     */
    static _getNamedValue(name, thread = null) {
        if (thread) {
            return ThreadUtil.getCurrentStack(thread).getScopeVar(name, true)
        }
        return extensionClassInstance.globalVariables.get(name, true)
    }

    /**
     * @param {*} value
     * @param {?Thread} thread
     * @param {(value: *) => boolean} isValidVal
     * @param {string} expectedDescription
     * @returns {*}
     */
    static _toTypeFromValueOrVariable(value, thread, isValidVal, expectedDescription) {
        if (isValidVal(value)) return value
        if (TypeChecker.isMissingValue(value)) {
            throwError("Expected a {expectedDescription}, but got no input value.", {expectedDescription})
        }
        if (!(TypeChecker.isClassicScratchValue(value))) { // Allow access to a variable named e.g. 513
            throwError("Expected a {expectedDescription} not a {actualDescription}.", {
                expectedDescription, actualDescription: TypeChecker.stringTypeof(value),
            })
        }
        
        const name = Cast.toString(value)
        let varValue
        try {
            varValue = Cast._getNamedValue(name, thread)
        } catch {
            throwError("Expected a {expectedDescription}, but variable {value} is not defined.", {expectedDescription, value: quote(value)})
        }
        if (isValidVal(varValue)) return varValue
        throwError("Expected a {expectedDescription}, but variable {value} is a(n) {varValueName}.", {
            expectedDescription, value: quote(value), varValueName: TypeChecker.stringTypeof(varValue),
        })
    }

    // Own

    /**
     * @param {*} value
     * @param {?Thread} thread
     * @returns {ClassType}
     */
    static toClass(value, thread = null) {
        return Cast._toTypeFromValueOrVariable(value, thread, v => v instanceof ClassType, translatedMsg("class or class variable name"))
    }

    /**
     * @param {*} value
     * @param {?Thread} thread
     * @returns {ClassInstanceType}
     */
    static toClassInstance(value, thread = null) {
        return Cast._toTypeFromValueOrVariable(value, thread, v => v instanceof ClassInstanceType, translatedMsg("class instance or class instance variable name"))
    }

    /**
     * @param {*} value
     * @param {?Thread} thread
     * @returns {FunctionType}
     */
    static toFunction(value, thread = null) {
        return Cast._toTypeFromValueOrVariable(value, thread, v => v instanceof FunctionType, translatedMsg("function or function variable name"))
    }
}

/************************************************************************************
*                            Dependencies and Value Types                           *
************************************************************************************/

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

class CustomType {
    className = "Unknown"

    toMonitorContent() {
        return span(this.toString())
    }

    /**
     * @returns {string}
     */
    toJSON() {
        return `${this.className} can not be serialized.`
    }

    // Prevent dogeiscut rendering my custom types as objects
    dogeiscutObjectHandler() {
        return span(this.toString()).outerHTML
    }

    // Render my custom types fully, instead of "Object"
    jwArrayHandler() {
        return span(this.toString()).outerHTML
    }
}

class BaseCallableType extends CustomType {
    className = "Callable"
    // Technically this name will never be shown, as only subclasses actually have instances
    // Should allow s-plural

    /**
     * @param {string} name
     * @param {Function} jsFunc
     * @param {ScopeStack} stack
     * @param {FunctionArgConfig} config
     */
    constructor(name, jsFunc, stack, config) {
        super()
        this.name = name
        this.jsFunc = jsFunc
        this.stack = stack.shallowCopy()
        this.argNames = config.argNames
        this.argDefaults = config.argDefaults
    }

    /**
     * @returns {string}
     */
    toString() {
        return `<${this.className} ${quote(this.name)}>`
    }

    /**
     * @param {Thread} thread
     * @param {...*} paramsForEnterContext - class instance and other shadow values from the block (e.g., instance, posArgs, setter value, other operand)
     * @returns {*} the return value of the method
     */
    *execute(thread, ...paramsForEnterContext) {
        const sizeBefore = ThreadUtil.getCurrentStack(thread).getSize()
        this.enterContext(thread, ...paramsForEnterContext)

        let output
        let finished = false
        try {
            output = (yield* this.jsFunc(thread))
            finished = true
        } finally {
            if (finished) {
                if (sizeBefore !== ThreadUtil.getCurrentStack(thread).getSize()) {
                    throwInternal("clever-badger")
                }
            } else {
                // An error happend, so exit stack frames that where interrupted
                ThreadUtil.getCurrentStack(thread).trimSize(sizeBefore)
            }

        }
        this.checkOutputValue(output)
        return output
    }

    /**
     * @param {Thread} thread
     */
    enterContext(thread) {
        // Allow better subclassing
    }

    /**
     * @param {*} output
     */
    checkOutputValue(output) {
        // Allow better subclassing
    }


    /**
     * @param {Array} posArgs
     * @returns {Object<string, *>}
     */
    evaluateArgs(posArgs) {
        const args = {}
        let name
        let prefix

        if (this instanceof InstanceMethodType && (this.name === "__SM_INIT_METHOD__")) prefix = "Initializing object"
        else if (this instanceof InstanceMethodType) prefix = `Calling method ${quote(this.name)}`
        else prefix = `Calling function ${quote(this.name)}`

        // Ensure there are not too many arguments
        if (posArgs.length > this.argNames.length) {
            throwError("{prefix}: expected at most {maxArgCount} positional arguments, but got {argCount}.", {prefix, argCount: posArgs.length, maxArgCount: this.argNames.length})
        }

        // Count how many arguments do NOT have defaults
        const posOnlyCount = this.argNames.length - this.argDefaults.length

        // Ensure enough positional arguments
        if (posArgs.length < posOnlyCount) {
            throwError("{prefix}: expected at least {posOnlyCount} positional arguments, but got only {argCount}.", {prefix, posOnlyCount, argCount: posArgs.length})
        }

        // Assign positional arguments
        for (let i = 0; i < posArgs.length; i++) {
            name = this.argNames[i]
            args[name] = posArgs[i]
        }

        // Fill in defaults for missing arguments
        const defaultsStartIndex = this.argNames.length - this.argDefaults.length
        for (let i = posArgs.length; i < this.argNames.length; i++) {
            name = this.argNames[i]
            const defaultIndex = i - defaultsStartIndex
            args[name] = this.argDefaults[defaultIndex]
        }

        return args
    }
}

class FunctionType extends BaseCallableType {
    customId = "gceFunction"
    className = "Function"

    /**
     * @param {Thread} thread
     * @param {PositionalFunctionArgs} posArgs
     */
    enterContext(thread, posArgs) {
        // Allow better subclassing
        const args = this.evaluateArgs(posArgs)
        ThreadUtil.getStackManager(thread).enterFunctionCall(this, args)
    }
}

class InstanceMethodType extends BaseCallableType {
    customId = "gceMethod"
    className = "Instance Method"

    /**
     * @param {Thread} thread
     * @param {ClassInstanceType} instance
     * @param {PositionalFunctionArgs} posArgs
     */
    enterContext(thread, instance, posArgs) {
        // Allow better subclassing
        const args = this.evaluateArgs(posArgs)
        ThreadUtil.getStackManager(thread).enterMethodCall(this, instance, args)
    }
}

class GetterMethodType extends InstanceMethodType {
    customId = "gceGetterMethod"
    className = "Getter Method"

    /**
     * @param {Thread} thread
     * @param {ClassInstanceType} instance
     */
    enterContext(thread, instance) {
        ThreadUtil.getStackManager(thread).enterGetterMethodCall(this, instance)
    }
}
class SetterMethodType extends InstanceMethodType {
    customId = "gceSetterMethod"
    className = "Setter Method"

    /**
     * @param {Thread} thread
     * @param {ClassInstanceType} instance
     * @param {*} value
     */
    enterContext(thread, instance, value) {
        ThreadUtil.getStackManager(thread).enterSetterMethodCall(this, instance, value)
    }

    /**
     * @param {*} output
     */
    checkOutputValue(output) {
        if (output !== Nothing) throwError("Setter methods must return {nothingValue}.", {nothingValue: Nothing})
    }
}

class OperatorMethodType extends InstanceMethodType {
    customId = "gceOperatorMethod"
    className = "Operator Method"

    /**
     * @param {Thread} thread
     * @param {ClassInstanceType} instance
     * @param {*} other
     */
    enterContext(thread, instance, other) {
        ThreadUtil.getStackManager(thread).enterOperatorMethodCall(this, instance, other)
    }
}

class ClassType extends CustomType {
    customId = "gceClass"
    className = "Class"

    /**
     * @param {string} name
     * @param {?ClassType} superCls
     */
    constructor(name, superCls) {
        super()
        this.name = name
        this.superCls = superCls
        this.instanceMethods = {}
        this.staticMethods = {}
        this.getters = {}
        this.setters = {}
        this.operatorMethods = {}
        this.clsVariables = new VariableManager()
    }

    /**
     * @returns string
     */
    toString() {
        return `<Class ${quote(this.name)}>`
    }

    /**
     * @param {string} name
     * @param {boolean} recursive
     * @param {boolean} preferSetter
     * @returns {{type: ?string, value: *}}
     */
    getMember(name, recursive, preferSetter) {
        if (name in this.instanceMethods) return {type: "CP_INSTANCE_METHOD", value: this.instanceMethods[name]}
        else if (name in this.staticMethods) return {type: "CP_STATIC_METHOD", value: this.staticMethods[name]}
        else if ((name in this.getters) && (name in this.setters)) {
            if (preferSetter) return {type: "CP_SETTER_METHOD", value: this.setters[name]}
            else return {type: "CP_GETTER_METHOD", value: this.getters[name]}
        }
        else if (name in this.getters) return {type: "CP_GETTER_METHOD", value: this.getters[name]}
        else if (name in this.setters) return {type: "CP_SETTER_METHOD", value: this.setters[name]}
        else if (name in this.operatorMethods) return {type: "CP_OPERATOR_METHOD", value: this.operatorMethods[name]}
        else if (this.clsVariables.has(name)) return {type: "CP_CLASS_VARIABLE", value: this.clsVariables.get(name)}
        if (recursive) {
            if (!this.superCls) return {type: null}
            return this.superCls.getMember(name, recursive, preferSetter)
        } else {
            return {type: null}
        }
    }

    /**
     * @param {string} name
     * @param {string} expectedMemberTypeCode
     * @returns {*}
     */
    getMemberOfType(name, expectedMemberTypeCode) {
        const expectedMemberType = MENUS.CLASS_PROPERTY.internalToPublic(expectedMemberTypeCode)
        const {type, value} = this.getMember(name, true, expectedMemberTypeCode === "CP_SETTER_METHOD")

        if (!type) throwError("Undefined {expectedMemberType} {name}.", {expectedMemberType, name: quote(name)})
        if (type !== expectedMemberTypeCode) throwError("Class Method or Variable {name} is not a {expectedMemberType} but a {type}.", {name: quote(name), expectedMemberType, type})
        return value
    }

    /**
     * @returns {Array<Object<string, *>>}
     */
    getAllMembers() {
        let currentCls = this
        /** @type {Array<ClassType>} */
        const classChain = [] // From top superclass to subclass
        while (currentCls) {
            classChain.splice(0, 0, currentCls)
            currentCls = currentCls.superCls
        }
        const instanceMethods = {}
        const staticMethods = {}
        const getterMethods = {}
        const setterMethods = {}
        const operatorMethods = {}
        const clsVariables = {}
        classChain.forEach((cls) => {
            Object.assign(instanceMethods, cls.instanceMethods)
            Object.assign(staticMethods, cls.staticMethods)
            Object.assign(getterMethods, cls.getters)
            Object.assign(setterMethods, cls.setters)
            Object.assign(operatorMethods, cls.operatorMethods)
            Object.assign(clsVariables, cls.clsVariables.getAll())
        })
        return [instanceMethods, staticMethods, getterMethods, setterMethods, operatorMethods, clsVariables]
    }

    /**
     * @param {string} name
     * @param {string} newMemberType
     * @param {*} value
     */
    setMemberOfType(name, newMemberType, value) {
        const currentMemberType = this.getMember(name, false, false).type // preference does not matter
        if (currentMemberType && (currentMemberType !== newMemberType) && !(
            ((currentMemberType === "CP_GETTER_METHOD") && (newMemberType === "CP_SETTER_METHOD")) ||
            ((currentMemberType === "CP_SETTER_METHOD") && (newMemberType === "CP_GETTER_METHOD"))
        )) {
            throwError("Can not assign {newMemberType}: {currentMemberType} already exists with the same name {name}.", {newMemberType, currentMemberType, name: quote(name)})
        }
        if (newMemberType === "CP_INSTANCE_METHOD") this.instanceMethods[name] = value
        else if (newMemberType === "CP_STATIC_METHOD") this.staticMethods[name] = value
        else if (newMemberType === "CP_GETTER_METHOD") this.getters[name] = value
        else if (newMemberType === "CP_SETTER_METHOD") this.setters[name] = value
        else if (newMemberType === "CP_OPERATOR_METHOD") this.operatorMethods[name] = value
        else if (newMemberType === "CP_CLASS_VARIABLE") this.clsVariables.set(name, value)
    }

    /**
     * @param {string} name 
     * @param {string} memberType 
     */
    deleteMemberOfType(name, memberType) {
        this.getMemberOfType(name, memberType) // check if member exists and is of the right type, will throw an error if not
        switch (memberType) {
            case "CP_INSTANCE_METHOD":
                delete this.instanceMethods[name]
                break
            case "CP_STATIC_METHOD":
                delete this.staticMethods[name]
                break
            case "CP_GETTER_METHOD":
                delete this.getters[name]
                break
            case "CP_SETTER_METHOD":
                delete this.setters[name]
                break
            case "CP_OPERATOR_METHOD":
                delete this.operatorMethods[name]
                break
            case "CP_CLASS_VARIABLE":
                this.clsVariables.delete(name)
                break
        }
    }    

    /**
     * @param {Thread} thread
     * @param {PositionalFunctionArgs} posArgs
     * @returns {ClassInstanceType} the instance
     */
    *createInstance(thread, posArgs) {
        const instance = new ClassInstanceType(this)
        const output = yield* instance.executeInstanceMethod(thread, "__SM_INIT_METHOD__", posArgs) // an init method always exists
        if (output !== Nothing) throwError("Initialization methods must return {nothingValue}.", {nothingValue: Nothing})
        return instance
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {PositionalFunctionArgs} posArgs
     * @returns {*}
     */
    *executeStaticMethod(thread, name, posArgs) {
        const methodFunc = this.getStaticMethod(name)
        return yield* methodFunc.execute(thread, posArgs)
    }

    /**
     * @param {string} name 
     * @returns {FunctionType}
     */
    getStaticMethod(name) {
        return assertType("quiet-fox", FunctionType, this.getMemberOfType(name, "CP_STATIC_METHOD"))
    }

    /**
     * @param {ClassType} superCls
     * @returns {boolean}
     */
    isSubclassOf(superCls) {
        if (this === superCls) return true
        let currentCls = this
        while (currentCls.superCls) {
            if (currentCls.superCls === superCls) return true
            currentCls = currentCls.superCls
        }
        return false
    }
}

class ClassInstanceType extends CustomType {
    customId = "gceClassInstance"
    className = "Class Instance"

    /**
     * @param {ClassType} cls
     */
    constructor(cls) {
        super()
        this.cls = cls
        this.attributes = {}
    }

    toString() {
        return `<Instance of ${quote(this.cls.name)}>`
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {PositionalFunctionArgs} posArgs
     * @returns {*} the return value of the method
     */
    *executeInstanceMethod(thread, name, posArgs) {
        /** @type {InstanceMethodType} */
        const method = this.cls.getMemberOfType(name, "CP_INSTANCE_METHOD")
        return yield* method.execute(thread, this, posArgs)
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {PositionalFunctionArgs} posArgs
     * @returns {*} the return value of the method
     */
    *executeSuperMethod(thread, name, posArgs) {
        if (!this.cls.superCls) throwError("Can not call super instance method: class has no superclass.")

        /** @type {InstanceMethodType} */
        const method = this.cls.superCls.getMemberOfType(name, "CP_INSTANCE_METHOD")
        return yield* method.execute(thread, this, posArgs)
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {PositionalFunctionArgs} posArgs
     * @returns {*} the return value of the method
     */
    *executeSuperInitMethod(thread, name, posArgs) {
        const output = yield* this.executeSuperMethod(thread, name, posArgs)
        if (output !== Nothing) throwError("Initialization methods must return {nothingValue}.", {nothingValue: Nothing})
        return output
    }

    /**
     * @param {Thread} thread
     * @param {string} name public operator method name
     * @param {*} other
     * @returns {*} the return value of the operator method
     */
    *executeOperatorMethod(thread, name, other) {
        name = MENUS.OPERATOR_METHOD.standardizeBlockInput(name)
        /** @type {OperatorMethodType} */
        const method = this.cls.getMemberOfType(name, "CP_OPERATOR_METHOD")
        return yield* method.execute(thread, this, other)
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @returns {*} the attribute value or return value of getter method
     */
    *getAttribute(thread, name) {
        const {type, value} = this.cls.getMember(name, true, false)
        if (type === "CP_GETTER_METHOD") {
            /** @type {GetterMethodType} */
            const getterMethod = value
            return (yield* getterMethod.execute(thread, this))
        }
        if (name in this.attributes) {
            return this.attributes[name]
        }
        throwError("{instanceValue} has no attribute or getter method for {name}.", {instanceValue: this, name: quote(name)})
    }

    /**
     * @param {Thread} thread
     * @param {string} name
     * @param {string} value
     */
    *setAttribute(thread, name, value) {
        const methodMember = this.cls.getMember(name, true, true)
        if (methodMember && methodMember.type === "CP_SETTER_METHOD") {
            yield* methodMember.value.execute(thread, this, value)
        } else if (methodMember && methodMember.type === "CP_GETTER_METHOD") {
            throwError("Can not set attribute {name} of {instanceValue}: attribute only has a getter method.", {name: quote(name), instanceValue: this})
        } else {
            this.attributes[name] = value
        }
    }

    /**
     * @param {string} name public operator method name
     * @returns {boolean}
     */
    *hasOperatorMethod(name) {
        name = MENUS.OPERATOR_METHOD.standardizeBlockInput(name)
        try {
            this.cls.getMemberOfType(name, "CP_OPERATOR_METHOD")
            return true
        } catch {
            return false
        }
    }
}

class NothingType extends CustomType {
    customId = "gceNothing"
    className = "Nothing"

    toString() {
        return `<Nothing>`
    }
    toJSON() {
        return this.toString()
    }
}
const Nothing = new NothingType()

const gceFunction = {
    Type: FunctionType,
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
const gceMethod = {
    Type: InstanceMethodType,
    GetterType: GetterMethodType,
    SetterType: SetterMethodType,
    OperatorType: OperatorMethodType,
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: BlockShape.ARROW,
        forceOutputType: "gceMethod",
        disableMonitor: true,
    },
    Argument: {
        shape: BlockShape.ARROW,
        exemptFromNormalization: true,
        check: ["gceMethod"],
    },
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
        defaultValue: translatedMsg("MyClass"),
        exemptFromNormalization: true,
    },
    ArgumentSubclassOrVarName: {
        type: ArgumentType.STRING,
        defaultValue: translatedMsg("MySubclass"),
        exemptFromNormalization: true,
    },
}
const gceClassInstance = {
    Type: ClassInstanceType,
    Block: {
        blockType: BlockType.REPORTER,
        blockShape: "gceOOP-doublePlus",
        forceOutputType: "gceClassInstance",
        disableMonitor: true,
    },
    Argument: {
        shape: "gceOOP-doublePlus",
        exemptFromNormalization: true,
        check: ["gceClassInstance"],
    },
    ArgumentClassOrVarName: {
        type: ArgumentType.STRING,
        defaultValue: translatedMsg("myInstance"),
        exemptFromNormalization: true,
    },
}
if (!CUSTOM_SHAPE) {
    delete gceClassInstance.Block.blockShape
    delete gceClassInstance.Argument.shape
}
const gceNothing = {
    Type: NothingType,
    Singleton: Nothing,
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
        defaultValue: translatedMsg("MyClass"),
    },
    methodName: {
        type: ArgumentType.STRING,
        defaultValue: translatedMsg("myMethod"),
    },
    classVariableName: {
        type: ArgumentType.STRING,
        defaultValue: translatedMsg("myClassVariable"),
    },
    attributeName: {
        type: ArgumentType.STRING,
        defaultValue: translatedMsg("myAttr"),
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

class GCEOOPBlocks {
    /**
     * @returns {object} metadata for this extension and its blocks.
     */
    getInfo() {
        const makeLabel = (text) => ({blockType: BlockType.LABEL, text: text})
        const info = {
            id: "gceOOP",
            name: translatedMsg("OOP"),
            color1: "#428af5",
            menuIconURI: "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICB2aWV3Qm94PSIwIDAgMjAgMjAiCiAgdmVyc2lvbj0iMS4xIgogIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPGNpcmNsZQogICAgY3g9IjEwIgogICAgY3k9IjEwIgogICAgcj0iOSIKICAgIHN0eWxlPSJmaWxsOiM0MjhhZjVmZjsgc3Ryb2tlOiMyZDVmYTg7IHN0cm9rZS13aWR0aDoycHg7IGZpbGwtb3BhY2l0eToxOyBzdHJva2Utb3BhY2l0eToxOyBwYWludC1vcmRlcjpzdHJva2UiIC8+CiAgPHBhdGgKICAgIGQ9Im0gMy41LDEwIDQuNSwtNS41IDEuMiwwLjYgLTMuNyw0LjkgMy43LDQuOSAtMS4yLDAuNiB6CiAgICAgICBtIDEzLDAgLTQuNSwtNS41IC0xLjIsMC42IDMuNyw0LjkgLTMuNyw0LjkgMS4yLDAuNiB6IgogICAgc3R5bGU9ImZpbGw6I2ZmZmZmZiIgLz4KPC9zdmc+",
            blocks: [
                makeLabel("Missing Extensions?"),
                { // BUTTON
                    blockType: BlockType.BUTTON,
                    opcode: "addFuncsScopesExtension",
                    text: "Add Functions & Scopes Extension"
                },
                { // BUTTON
                    blockType: BlockType.BUTTON,
                    opcode: "addArrayExtension",
                    text: "Add Array Extension"
                },
                { // BUTTON
                    blockType: BlockType.BUTTON,
                    opcode: "addObjectExtension",
                    text: "Add Object Extension"
                },
                {
                    ...commonBlocks.command,
                    opcode: "logStacks",
                },
                makeLabel("Define Classes"),
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "createClassAt",
                    text: ["create class at var [NAME] [SHADOW]"],
                    tooltip: "Creates a new class, stores it in the chosen variable.",
                    arguments: {
                        NAME: commonArguments.classVarName,
                        SHADOW: {fillIn: "currentClass"},
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "createSubclassAt",
                    text: ["create subclass at var [NAME] with superclass [SUPERCLASS] [SHADOW]"],
                    tooltip: "Creates a subclass with the given superclass, stores it in a variable.",
                    arguments: {
                        NAME: gceClass.ArgumentSubclassOrVarName,
                        SUPERCLASS: gceClass.ArgumentClassOrVarName,
                        SHADOW: {fillIn: "currentClass"},
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "createClassNamed",
                    text: ["create class named [NAME] [SHADOW]"],
                    tooltip: "Creates and returns a new class with the given name.",
                    branchCount: 1,
                    arguments: {
                        NAME: commonArguments.classVarName,
                        SHADOW: {fillIn: "currentClass"},
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "createSubclassNamed",
                    text: ["create subclass named [NAME] with superclass [SUPERCLASS] [SHADOW]"],
                    tooltip: "Creates and returns a new subclass with the given superclass.",
                    branchCount: 1,
                    arguments: {
                        NAME: gceClass.ArgumentSubclassOrVarName,
                        SUPERCLASS: gceClass.ArgumentClassOrVarName,
                        SHADOW: {fillIn: "currentClass"},
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "onClass",
                    text: ["on class [CLASS] [SHADOW]"],
                    tooltip: "Runs the enclosed blocks as if they were inside the selected class definition. "+
                      "This allows you to e.g. add methods to already defined classes.",
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        SHADOW: {fillIn: "currentClass"},
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "currentClass",
                    text: "current class",
                    tooltip: "Returns the class currently being defined.",
                    canDragDuplicate: true,
                    hideFromPalette: true,
                },
                "---",
                makeLabel("Use Classes"),
                {
                    ...commonBlocks.returnsBoolean,
                    opcode: "isSubclass",
                    text: "is [SUBCLASS] a subclass of [SUPERCLASS] ?",
                    tooltip: "Checks whether one class inherits from another.",
                    arguments: {
                        SUBCLASS: gceClass.ArgumentSubclassOrVarName,
                        SUPERCLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "getSuperclass",
                    text: "get superclass of [CLASS]",
                    tooltip: "Returns the superclass of a class, or Nothing if it has none.",
                    arguments: {
                        CLASS: gceClass.ArgumentSubclassOrVarName,
                    },
                },
                "---",
                makeLabel("Class Members"),
                "---",
                makeLabel("Define Instance Methods"),
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineInstanceMethod",
                    text: ["define instance method [NAME] [SHADOW]"],
                    tooltip: "Defines an instance method on the current class.",
                    arguments: {
                        NAME: commonArguments.methodName,
                        SHADOW: {fillIn: "self"},
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineSpecialMethod",
                    text: ["define [SPECIAL_METHOD] instance method [SHADOW]"],
                    tooltip: "Defines a special instance method.",
                    arguments: {
                        SPECIAL_METHOD: {type: ArgumentType.STRING, menu: "specialMethod"},
                        SHADOW: {fillIn: "self"},
                    },
                },
                {
                    ...gceClassInstance.Block,
                    opcode: "self",
                    text: "self",
                    tooltip: "Reports the current instance inside a method.",
                    canDragDuplicate: true,
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "callSuperMethod",
                    text: "call super method [NAME] with positional args [POSARGS]",
                    tooltip: "Calls an instance method from the superclass of the current object.",
                    arguments: {
                        NAME: commonArguments.methodName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                {
                    ...gceNothing.Block,
                    opcode: "callSuperInitMethod",
                    text: "call super init method with positional args [POSARGS]",
                    tooltip: "Calls the superclass init method for the current object.",
                    arguments: {
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                "---",
                makeLabel("Define Getters & Setters"),
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineGetter",
                    text: ["define getter [NAME] [SHADOW]"],
                    tooltip: "Defines a getter method for an attribute on the current class.",
                    arguments: {
                        NAME: commonArguments.attributeName,
                        SHADOW: {fillIn: "self"},
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineSetter",
                    text: ["define setter [NAME] [SHADOW1] [SHADOW2]"],
                    tooltip: "Defines a setter method for an attribute on the current class.",
                    arguments: {
                        NAME: commonArguments.attributeName,
                        SHADOW1: {fillIn: "self"},
                        SHADOW2: {fillIn: "defineSetterValue"},
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "defineSetterValue",
                    text: "operator value",
                    tooltip: "Reports the incoming value inside a setter method.",
                    hideFromPalette: true,
                    canDragDuplicate: true,
                },
                "---",
                makeLabel("Define Operator Methods"),
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineOperatorMethod",
                    text: ["define operator method [OPERATOR_KIND] [SHADOW]"],
                    tooltip: "Defines custom behavior for an operator on instances of the current class.",
                    arguments: {
                        OPERATOR_KIND: {type: ArgumentType.STRING, menu: "operatorMethod"},
                        SHADOW: {fillIn: "operatorOperatorValue"},
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "operatorOperatorValue",
                    text: "operator value",
                    tooltip: "Reports the other operand inside an operator method.",
                    hideFromPalette: true,
                    canDragDuplicate: true,
                },
                "---",
                makeLabel("Define Static Methods & Class Variables"),
                {
                    ...commonBlocks.command,
                    opcode: "setClassVariable",
                    text: "on [CLASS] set class var [NAME] to [VALUE]",
                    tooltip: "Sets a class variable on the selected class.",
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        NAME: commonArguments.classVariableName,
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "getClassVariable",
                    text: "get class var [NAME] of [CLASS]",
                    tooltip: "Gets a class variable from the selected class.",
                    arguments: {
                        NAME: commonArguments.classVariableName,
                        CLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                {
                    ...commonBlocks.command,
                    opcode: "deleteClassVariable",
                    text: "on [CLASS] delete class var [NAME]",
                    tooltip: "Deletes a class variable from the selected class.",
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        NAME: commonArguments.classVariableName,
                    },
                },
                {
                    ...commonBlocks.commandWithBranch,
                    opcode: "defineStaticMethod",
                    text: ["define static method [NAME]"],
                    tooltip: "Defines a static method on the current class.",
                    arguments: {
                        NAME: commonArguments.methodName,
                    },
                },
                {
                    ...jwArrayStub.Block,
                    opcode: "propertyNamesOfClass",
                    text: "[PROPERTY] names of class [CLASS]",
                    tooltip: "Returns the names of members of the selected type for a class.",
                    arguments: {
                        PROPERTY: {type: ArgumentType.STRING, menu: "classProperty"},
                        CLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                "---",
                makeLabel("Working with Instances"),
                "---",
                makeLabel("Create & Inspect"),
                {
                    ...gceClassInstance.Block,
                    opcode: "createInstance",
                    text: "create instance of class [CLASS] with positional args [POSARGS]",
                    tooltip: "Creates an instance of a class and passes the given positional arguments to its init method.",
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                {
                    ...commonBlocks.returnsBoolean,
                    opcode: "isInstance",
                    text: "is [INSTANCE] an instance of [CLASS] ?",
                    tooltip: "Checks whether an instance belongs to a class or one of its subclasses.",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                        CLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
                {
                    ...gceClass.Block,
                    opcode: "getClassOfInstance",
                    text: "get class of [INSTANCE]",
                    tooltip: "Returns the class that created an instance.",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                    },
                },
                "---",
                makeLabel("Attributes"),
                {
                    ...commonBlocks.command,
                    opcode: "setAttribute",
                    text: "on [INSTANCE] set attribute [NAME] to [VALUE]",
                    tooltip: "Sets an attribute on an instance or calls its setter if one exists.",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                        NAME: commonArguments.attributeName,
                        VALUE: commonArguments.allowAnything,
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "getAttribute",
                    text: "on [INSTANCE] get attribute [NAME]",
                    tooltip: "Gets an attribute from an instance or calls its getter if one exists.",
                    arguments: {
                        NAME: commonArguments.attributeName,
                        INSTANCE: gceClassInstance.Argument,
                    },
                },
                {
                    ...dogeiscutObjectStub.Block,
                    opcode: "getAllAttributes",
                    text: "all attributes of [INSTANCE]",
                    tooltip: "Returns all direct instance attributes as an object.",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                    },
                },
                "---",
                makeLabel("Call Methods"),
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "callMethod",
                    text: "on [INSTANCE] call method [NAME] with positional args [POSARGS]",
                    tooltip: "Calls an instance method on an object with positional arguments.",
                    arguments: {
                        INSTANCE: gceClassInstance.Argument,
                        NAME: commonArguments.methodName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                {
                    ...commonBlocks.returnsAnything,
                    opcode: "callStaticMethod",
                    text: "on [CLASS] call static method [NAME] with positional args [POSARGS]",
                    tooltip: "Calls a static method on a class with positional arguments.",
                    arguments: {
                        CLASS: gceClass.ArgumentClassOrVarName,
                        NAME: commonArguments.methodName,
                        POSARGS: jwArrayStub.Argument,
                    },
                },
                {
                    ...gceFunction.Block,
                    opcode: "getStaticMethodFunc",
                    text: "get static method [NAME] of [CLASS] as function",
                    tooltip: "Returns a static method from a class as a callable function value.",
                    arguments: {
                        NAME: commonArguments.methodName,
                        CLASS: gceClass.ArgumentClassOrVarName,
                    },
                },
            ],
            menus: {
                classProperty: {
                    acceptReporters: false,
                    items: MENUS.CLASS_PROPERTY.getMenuItems(),
                },
                operatorMethod: {
                    acceptReporters: false,
                    items: MENUS.OPERATOR_METHOD.getMenuItems(),
                },
                specialMethod: {
                    acceptReporters: false,
                    items: MENUS.SPECIAL_METHOD.getMenuItems(),
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

    /**
     * @param {boolean} includeOOPBlocks
     * @param {boolean} includeFuncScopesBlocks
     * @returns {object} compilation information and implementation for some blocks of the selected extensions
     */
    getCompileInfo(includeOOPBlocks = true, includeFuncScopesBlocks = true) {
        const createIRGenerator = (kind, inputs, fields, yieldRequired = false) => ((generator, block) => {
            if (yieldRequired) generator.script.yields = true
            const result = { kind }

            inputs.forEach(inputName => {
                result[inputName] = inputName === "SUBSTACK"
                    ? generator.descendSubstack(block, inputName)
                    : generator.descendInputOfBlock(block, inputName)
            })

            fields.forEach(fieldName => {
                result[fieldName] = block.fields[fieldName].value
            })
            return result
        })

        const EXTENSION_PREFIX = "runtime.ext_gceOOP"
        const ENV_PREFIX = `${EXTENSION_PREFIX}.environment`
        const THREAD_UTIL_PREFIX = `${EXTENSION_PREFIX}.ThreadUtil`
        const CURRENT_STACK = `${THREAD_UTIL_PREFIX}.getCurrentStack(thread)`
        const STACK_MANAGER = `${THREAD_UTIL_PREFIX}.getStackManager(thread)`
        const CAST_PREFIX = `${EXTENSION_PREFIX}.Cast`
        const MENUS_PREFIX = `${EXTENSION_PREFIX}.MENUS`

        const createClassCore = (node, compiler, setVariable, superClsCode = null) => {
            const nameCode = compiler.descendInput(node.NAME).asString()
            const clsLocal = compiler.localVariables.next()
            const superClass = superClsCode ? `${CAST_PREFIX}.toClass(${superClsCode}, thread)`: `${ENV_PREFIX}.commonSuperClass`

            return {
                setup: `const ${clsLocal} = new ${ENV_PREFIX}.ClassType(${nameCode}, ${superClass});` +
                    (setVariable ? `${CURRENT_STACK}.setScopeVar(${clsLocal}.name, ${clsLocal});` : "") +
                    `${CURRENT_STACK}.enterClassDefScope(${clsLocal});`,
                cleanup: `${CURRENT_STACK}.exitClassDefScope();`,
                clsLocal
            }
        }

        const createWrappedGenerator = (setupCode, stackCode, cleanup, returnVar = null) => {
            return `(yield* (function*() {${setupCode}${stackCode}${cleanup}${returnVar ? `return ${returnVar};` : ""}})())`
        }

        const createMethodDefinition = (
            node, compiler, imports,
            nameCode, classId, memberType,
            disableFuncConfig,
        ) => {
            const nameLocal = compiler.localVariables.next()

            compiler.source += `const ${nameLocal} = ${nameCode};` +
                `${CURRENT_STACK}.getClsOrThrow("define method").setMemberOfType(${nameLocal}, ${quote(memberType)}, `+
                `new ${ENV_PREFIX}.${classId}(${nameLocal}, function* (thread) {`
            addSubstackCode(compiler, node.SUBSTACK, imports)
            compiler.source += `${STACK_MANAGER}.prepareReturn();` +
                // Nothing is indepedent of function context, so we can exit context before
                `return ${ENV_PREFIX}.Nothing;` +
                `}, ${CURRENT_STACK}, ` +
                `${CURRENT_STACK}.` + (disableFuncConfig ? "constructor.getDefaultFuncConfig()" : "getAndResetNextFuncConfig()") + "));\n"
        }

        const createCallCode = (castMethod, castArgs, m, ...args) => {
            return `(yield* ${CAST_PREFIX}.${castMethod}(${castArgs.join(", ")}).${m}(thread, ${args.join(", ")}))`
        }

        const addSubstackCode = (compiler, substack, imports) => {
            compiler.descendStack(substack, new imports.Frame(false, undefined, true))
        }

        const getSubstackCode = (compiler, substack, imports) => {
            const oldSource = compiler.source
            compiler.source = ""
            addSubstackCode(compiler, substack, imports)
            const substackCode = compiler.source
            compiler.source = oldSource
            return substackCode
        }

        let irInfo = {}
        let jsInfo = {}

        if (includeOOPBlocks) {
            Object.assign(irInfo, {
                // Define Classes
                createClassAt: createIRGenerator("stack", ["NAME", "SUBSTACK"], [], true),
                createSubclassAt: createIRGenerator("stack", ["NAME", "SUPERCLASS", "SUBSTACK"], [], true),
                createClassNamed: createIRGenerator("input", ["NAME", "SUBSTACK"], [], true),
                createSubclassNamed: createIRGenerator("input", ["NAME", "SUPERCLASS", "SUBSTACK"], [], true),

                // Define Instance Methods
                defineInstanceMethod: createIRGenerator("stack", ["NAME", "SUBSTACK"], []),
                defineSpecialMethod: createIRGenerator("stack", ["SUBSTACK"], ["SPECIAL_METHOD"]),
                callSuperMethod: createIRGenerator("input", ["NAME", "POSARGS"], [], true),
                callSuperInitMethod: createIRGenerator("input", ["POSARGS"], [], true),

                // Define Getters & Setters
                defineGetter: createIRGenerator("stack", ["NAME", "SUBSTACK"], []),
                defineSetter: createIRGenerator("stack", ["NAME", "SUBSTACK"], []),

                // Define Operator Methods
                defineOperatorMethod: createIRGenerator("stack", ["SUBSTACK"], ["OPERATOR_KIND"]),

                // Define Static Methods & Class Variables
                defineStaticMethod: createIRGenerator("stack", ["NAME", "SUBSTACK"], []),


                // Create & Inspect
                createInstance: createIRGenerator("input", ["CLASS", "POSARGS"], [], true),

                // Attributes
                setAttribute: createIRGenerator("stack", ["INSTANCE", "NAME", "VALUE"], [], true),
                getAttribute: createIRGenerator("input", ["INSTANCE", "NAME"], [], true),

                // Call Methods
                callMethod: createIRGenerator("input", ["INSTANCE", "NAME", "POSARGS"], [], true),
                callStaticMethod: createIRGenerator("input", ["CLASS", "NAME", "POSARGS"], [], true),
            })
            Object.assign(jsInfo, {
                // Define Classes
                createClassAt: (node, compiler, imports) => {
                    const { setup, cleanup } = createClassCore(node, compiler, true)
                    compiler.source += setup
                    addSubstackCode(compiler, node.SUBSTACK, imports)
                    compiler.source += cleanup + "\n"
                },
                createSubclassAt: (node, compiler, imports) => {
                    const superClsCode = compiler.descendInput(node.SUPERCLASS).asUnknown()
                    const { setup, cleanup } = createClassCore(node, compiler, true, superClsCode)
                    compiler.source += setup
                    addSubstackCode(compiler, node.SUBSTACK, imports)
                    compiler.source += cleanup + "\n"
                },
                createClassNamed: (node, compiler, imports) => {
                    const { setup, cleanup, clsLocal } = createClassCore(node, compiler, false)
                    const substackCode = getSubstackCode(compiler, node.SUBSTACK, imports)
                    const generatedCode = createWrappedGenerator(setup, substackCode, cleanup, clsLocal)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
                createSubclassNamed: (node, compiler, imports) => {
                    const superClsCode = compiler.descendInput(node.SUPERCLASS).asUnknown()
                    const { setup, cleanup, clsLocal } = createClassCore(node, compiler, false, superClsCode)
                    const substackCode = getSubstackCode(compiler, node.SUBSTACK, imports)
                    const generatedCode = createWrappedGenerator(setup, substackCode, cleanup, clsLocal)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Define Instance Methods
                defineInstanceMethod: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    createMethodDefinition(node, compiler, imports, nameCode, "InstanceMethodType", "CP_INSTANCE_METHOD", false)
                },
                defineSpecialMethod: (node, compiler, imports) => {
                    const nameCode = `${MENUS_PREFIX}.SPECIAL_METHOD.standardizeBlockInput(${quote(node.SPECIAL_METHOD)})`
                    createMethodDefinition(node, compiler, imports, nameCode, "InstanceMethodType", "CP_INSTANCE_METHOD", false)
                },
                callSuperMethod: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = `(yield* ${CURRENT_STACK}.getSelfOrThrow().executeSuperMethod(thread, ${nameCode}, ${posArgsCode}))`
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
                callSuperInitMethod: (node, compiler, imports) => {
                    const nameCode = quote("__SM_INIT_METHOD__")
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = `(yield* ${CURRENT_STACK}.getSelfOrThrow().executeSuperInitMethod(thread, ${nameCode}, ${posArgsCode}))`
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Define Getters & Setters
                defineGetter: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    createMethodDefinition(node, compiler, imports, nameCode, "GetterMethodType", "CP_GETTER_METHOD", true)
                },
                defineSetter: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    createMethodDefinition(node, compiler, imports, nameCode, "SetterMethodType", "CP_SETTER_METHOD", true)
                },

                // Define Operator Methods
                defineOperatorMethod: (node, compiler, imports) => {
                    const nameCode = `${MENUS_PREFIX}.OPERATOR_METHOD.standardizeBlockInput(${quote(node.OPERATOR_KIND)})`
                    createMethodDefinition(node, compiler, imports, quote(node.OPERATOR_KIND), "OperatorMethodType", "CP_OPERATOR_METHOD", true)
                },

                // Define Static Methods & Class Variables
                defineStaticMethod: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    createMethodDefinition(node, compiler, imports, nameCode, "FunctionType", "CP_STATIC_METHOD", false)
                },


                // Create & Inspect
                createInstance: (node, compiler, imports) => {
                    const classCode = compiler.descendInput(node.CLASS).asUnknown()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = createCallCode("toClass", [classCode, "thread"], "createInstance", posArgsCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Attributes
                setAttribute: (node, compiler, imports) => {
                    const instanceCode = compiler.descendInput(node.INSTANCE).asUnknown()
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const valueCode = compiler.descendInput(node.VALUE).asUnknown()
                    compiler.source += createCallCode("toClassInstance", [instanceCode, "thread"], "setAttribute", nameCode, valueCode) + ";\n"
                },
                getAttribute: (node, compiler, imports) => {
                    const instanceCode = compiler.descendInput(node.INSTANCE).asUnknown()
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const generatedCode = createCallCode("toClassInstance", [instanceCode, "thread"], "getAttribute", nameCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Call Methods
                callMethod: (node, compiler, imports) => {
                    const instanceCode = compiler.descendInput(node.INSTANCE).asUnknown()
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = createCallCode("toClassInstance", [instanceCode, "thread"], "executeInstanceMethod", nameCode, posArgsCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
                callStaticMethod: (node, compiler, imports) => {
                    const classCode = compiler.descendInput(node.CLASS).asUnknown()
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = createCallCode("toClass", [classCode, "thread"], "executeStaticMethod", nameCode, posArgsCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
            })
        }
        
        if (includeFuncScopesBlocks) {
            Object.assign(irInfo, {
                // Define
                createFunctionAt: createIRGenerator("stack", ["NAME", "SUBSTACK"], []),
                createFunctionNamed: createIRGenerator("input", ["NAME", "SUBSTACK"], []),

                // Inside Functions & Methods
                returnValue: createIRGenerator("stack", ["VALUE"], []),

                // Use Functions
                callFunction: createIRGenerator("input", ["FUNC", "POSARGS"], [], true),


                // Utilities
                objectAsString: createIRGenerator("input", ["VALUE"], [], true),
            })
            Object.assign(jsInfo, {
                // Define
                createFunctionAt: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const nameLocal = compiler.localVariables.next()

                    compiler.source += `const ${nameLocal} = ${nameCode};` +
                        `${CURRENT_STACK}.setScopeVar(${nameLocal}, new ${ENV_PREFIX}.FunctionType(${nameLocal}, function* (thread) {`
                    addSubstackCode(compiler, node.SUBSTACK, imports)
                    compiler.source += `${STACK_MANAGER}.prepareReturn();` +
                        // Nothing is indepedent of function context, so we can exit context before
                        `return ${ENV_PREFIX}.Nothing;` +
                        `}, ${CURRENT_STACK},`+
                        `${CURRENT_STACK}.getAndResetNextFuncConfig()));\n`
                },
                createFunctionNamed: (node, compiler, imports) => {
                    const nameCode = compiler.descendInput(node.NAME).asString()
                    const generatedCode = `(new ${ENV_PREFIX}.FunctionType(${nameCode}, function* (thread) {`+
                        getSubstackCode(compiler, node.SUBSTACK, imports)+
                        `${STACK_MANAGER}.prepareReturn();` +
                        // Nothing is indepedent of function context, so we can exit context before
                        `return ${ENV_PREFIX}.Nothing;` +
                        `}, ${CURRENT_STACK},` +
                        `${CURRENT_STACK}.getAndResetNextFuncConfig()))`
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },

                // Inside Functions & Methods
                returnValue: (node, compiler, imports) => {
                    const returnValueLocal = compiler.localVariables.next()
                    // We need to cache the return value before exiting context, as it might depend on it
                    compiler.source += `const ${returnValueLocal} = ${compiler.descendInput(node.VALUE).asUnknown()};` +
                        `${STACK_MANAGER}.prepareReturn();` +
                        `return ${returnValueLocal};\n`
                },

                // Use Functions
                callFunction: (node, compiler, imports) => {
                    const funcCode = compiler.descendInput(node.FUNC).asUnknown()
                    const posArgsCode = `${CAST_PREFIX}.toArray(${compiler.descendInput(node.POSARGS).asUnknown()}).array`
                    const generatedCode = createCallCode("toFunction", [funcCode, "thread"], "execute", posArgsCode)
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },


                // Utilities
                objectAsString: (node, compiler, imports) => {
                    const objectCode = compiler.descendInput(node.VALUE).asUnknown()
                    const generatedCode = `(yield* ${EXTENSION_PREFIX}._objectAsString(${objectCode}, thread))`
                    return new (imports.TypedInput)(generatedCode, imports.TYPE_UNKNOWN)
                },
            })
        }

        return {ir: irInfo, js: jsInfo}
    }

    constructor() {
        // to allow other extensions access from the extension class
        if (isRuntimeEnv) {
            Object.assign(Scratch.vm, {gceFunction, gceMethod, gceClass, gceClassInstance, gceNothing})
        }
        this.Cast = Cast
        this.MENUS = MENUS
        this.ThreadUtil = ThreadUtil
        // to allow other extensions access to all internal classes
        this.environment = {
            doublePlusShape: CUSTOM_SHAPE, TRANSLATIONS, applyInternalWrappers,
            quote, escapeHTML, span, translatedMsg, throwError, throwInternal, assertType,
            VariableManager, ThreadUtil, ScopeStackManager, ScopeStack, MenuManager, MENU_ITEMS: MENUS,
            TypeChecker, Cast, CustomType, BaseCallableType, FunctionType,
            InstanceMethodType, GetterMethodType, SetterMethodType, OperatorMethodType,
            ClassType, commonSuperClass: null, ClassInstanceType, NothingType, Nothing,
            gceFunction, gceMethod, gceClass, gceClassInstance, gceNothing,
        }
        
        if (isRuntimeEnv) {
            runtime.registerSerializer(
                "gceNothing",
                v => (v instanceof NothingType ? v.toJSON() : null),
                v => Nothing,
            )
            Scratch.gui.getBlockly().then(ScratchBlocks => {
                ScratchBlocks.BlockSvg.registerCustomShape("gceOOP-doublePlus", CUSTOM_SHAPE)
            })
            
            applyInternalWrappers(Scratch)
        }

        this.globalVariables = new VariableManager()
    }

    setup() {
        if (!isRuntimeEnv) return
        
        this.addFuncsScopesExtension()
        this.addArrayExtension()
        this.addObjectExtension()

        const commonSuperClass = new ClassType("Superclass", null)
        commonSuperClass.instanceMethods["__SM_INIT_METHOD__"] = new InstanceMethodType(
            "__SM_INIT_METHOD__",
            function* (thread) {
                ThreadUtil.getStackManager(thread).prepareReturn()
                // Nothing is indepedent of function context, so we can exit context before
                return Nothing
            },
            new ScopeStack(),
            ScopeStack.getDefaultFuncConfig(),
        )
        this.environment.commonSuperClass = commonSuperClass
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

    addFuncsScopesExtension() { // BUTTON
        if (isRuntimeEnv && !Scratch.vm.extensionManager.isExtensionLoaded("gceFuncsScopes")) {
            this._addLocalhostOrProdExtension(
                "http://localhost:5173/extensions/gceFuncsScopes.js",
                "https://germancodeengineer.github.io/PM-Extensions/extensions/gceFuncsScopes.js"
            )
        }
    }
    
    addArrayExtension() { // BUTTON
        if (isRuntimeEnv &&!Scratch.vm.extensionManager.isExtensionLoaded("jwArray")) {
            Scratch.vm.extensionManager.loadExtensionIdSync("jwArray")
        }
    }

    addObjectExtension() { // BUTTON
        if (isRuntimeEnv &&!Scratch.vm.extensionManager.isExtensionLoaded("dogeiscutObject")) {
            Scratch.vm.extensionManager.loadExtensionURL(
                "https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutObject.js"
            )
        }
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    logStacks(args, util) {
        console.log("Current thread stacks:", JSON.stringify([...ThreadUtil.getStackManager(util.thread).stacks], null, 2))
    }

    /******************** Scoped Variables ********************/

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    setScopeVar(args, util) {
        const name = Cast.toString(args.NAME)
        ThreadUtil.getCurrentStack(util.thread).setScopeVar(name, args.VALUE)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    getScopeVar(args, util) {
        const name = Cast.toString(args.NAME)
        return ThreadUtil.getCurrentStack(util.thread).getScopeVar(name)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    scopeVarExists(args, util) {
        const name = Cast.toString(args.NAME)
        const currentStack = ThreadUtil.getCurrentStack(util.thread)
        let hasVar
        switch (args.KIND) {
            case "all scopes":
                hasVar = currentStack.hasScopeVar(name, false, false)
                break
            case "local scope":
                hasVar = currentStack.hasScopeVar(name, true, false)
                break
            case "global scope":
                hasVar = currentStack.hasScopeVar(name, false, true)
                break
        }
        return Cast.toBoolean(hasVar)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    deleteScopeVar(args, util) {
        const name = Cast.toString(args.NAME)
        ThreadUtil.getCurrentStack(util.thread).deleteScopeVar(name)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    allVariables(args, util) {
        const currentStack = ThreadUtil.getCurrentStack(util.thread)
        let varNames
        switch (args.KIND) {
            case "all scopes":
                varNames = currentStack.getScopeVarNames(false, false)
                break
            case "local scope":
                varNames = currentStack.getScopeVarNames(true, false)
                break
            case "global scope":
                varNames = currentStack.getScopeVarNames(false, true)
                break
        }
        return Cast.toArray(varNames)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    createVarScope(args, util) {
        ThreadUtil.getCurrentStack(util.thread).enterUserScope()
        util.startBranch(1, false, () => {
            ThreadUtil.getCurrentStack(util.thread).exitUserScope()
        })
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    bindVarToScope(args, util) {
        const name = Cast.toString(args.NAME)
        switch (args.KIND) {
            case "non-local":
                ThreadUtil.getCurrentStack(util.thread).bindScopeVarNonlocal(name)
                break
            case "global":
                ThreadUtil.getCurrentStack(util.thread).bindScopeVarGlobal(name)
                break
        }
    }

    /******************** Classes ********************/

    // Define Classes
    createClassAt = this._isACompiledBlock
    createSubclassAt = this._isACompiledBlock
    createClassNamed = this._isACompiledBlock
    createSubclassNamed = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    onClass(args, util) {
        const cls = Cast.toClass(args.CLASS, util.thread)
        ThreadUtil.getCurrentStack(util.thread).enterClassDefScope(cls)
        util.startBranch(1, false, () => {
            ThreadUtil.getCurrentStack(util.thread).exitClassDefScope()
        })
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    currentClass(args, util) {
        return ThreadUtil.getCurrentStack(util.thread).getClsOrThrow("current class")
    }

    // Use Classes

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    isSubclass(args, util) {
        const subCls = Cast.toClass(args.SUBCLASS, util.thread)
        const superCls = Cast.toClass(args.SUPERCLASS, util.thread)
        return Cast.toBoolean(subCls.isSubclassOf(superCls))
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    getSuperclass(args, util) {
        const cls = Cast.toClass(args.CLASS, util.thread)
        if (cls.superCls) {
            return assertType("calm-hare", ClassType, cls.superCls)
        } else {
            return Nothing
        }
    }

    /******************** Class Members ********************/

    // Define Instance Methods
    defineInstanceMethod = this._isACompiledBlock
    defineSpecialMethod = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    self(args, util) {
        const value =  ThreadUtil.getCurrentStack(util.thread).getSelfOrThrow()
        return assertType("mirthful-dolphin", ClassInstanceType, value)
    }
    callSuperMethod = this._isACompiledBlock
    callSuperInitMethod = this._isACompiledBlock

    // Define Getters & Setters
    defineGetter = this._isACompiledBlock
    defineSetter = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    defineSetterValue(args, util) {
        return ThreadUtil.getCurrentStack(util.thread).getSetterValueOrThrow()
    }

    // Define Operator Methods
    defineOperatorMethod = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    operatorOperatorValue(args, util) {
        return ThreadUtil.getCurrentStack(util.thread).getOperatorValueOrThrow()
    }

    // Define Static Methods & Class Variables

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    setClassVariable(args, util) {
        const cls = Cast.toClass(args.CLASS, util.thread)
        const name = Cast.toString(args.NAME)
        const value = args.VALUE
        cls.setMemberOfType(name, value, "CP_CLASS_VARIABLE")
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    getClassVariable(args, util) {
        const cls = Cast.toClass(args.CLASS, util.thread)
        const name = Cast.toString(args.NAME)
        const value = cls.getMemberOfType(name, "CP_CLASS_VARIABLE")
        return value
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    deleteClassVariable(args, util) {
        const cls = Cast.toClass(args.CLASS, util.thread)
        const name = Cast.toString(args.NAME)
        cls.deleteMemberOfType(name, "CP_CLASS_VARIABLE")
    }
    defineStaticMethod = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    propertyNamesOfClass(args, util) {
        const property = MENUS.CLASS_PROPERTY.standardizeBlockInput(args.PROPERTY)
        const cls = Cast.toClass(args.CLASS, util.thread)
        const [instanceMethods, staticMethods, getterMethods, setterMethods, operatorMethods, classVariables] = cls.getAllMembers()
        let values = []
        switch (property) {
            case "CP_INSTANCE_METHOD":
                values = instanceMethods; break
            case "CP_STATIC_METHOD":
                values = staticMethods; break
            case "CP_GETTER_METHOD":
                values = getterMethods; break
            case "CP_SETTER_METHOD":
                values = setterMethods; break
            case "CP_OPERATOR_METHOD":
                values = operatorMethods; break
            case "CP_CLASS_VARIABLE":
                values = classVariables; break
        }
        let names = Object.keys(values)
        if (property == "CP_INSTANCE_METHOD") {
            let index
            index = names.indexOf("__SM_INIT_METHOD__")
            if (index !== -1) names[index] = "[special] init"
            index = names.indexOf("__SM_AS_STRING_METHOD__")
            if (index !== -1) names[index] = "[special] as string"
        }
        else if (property === "CP_OPERATOR_METHOD") {
            names = names.map(name => MENUS.OPERATOR_METHOD.internalToPublic(name))
        }
        return Cast.toArray(names)
    }

    /******************** Working with Instances ********************/

    // Create & Inspect
    createInstance = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    isInstance(args, util) {
        const instance = Cast.toClassInstance(args.INSTANCE, util.thread)
        const cls = Cast.toClass(args.CLASS, util.thread)
        return Cast.toBoolean(instance.cls.isSubclassOf(cls))
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    getClassOfInstance(args, util) {
        const instance = Cast.toClassInstance(args.INSTANCE, util.thread)
        const value = instance.cls
        return assertType("calm-weasel", ClassType, value)
    }

    // Attributes
    setAttribute = this._isACompiledBlock
    getAttribute = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    getAllAttributes(args, util) {
        const instance = Cast.toClassInstance(args.INSTANCE, util.thread)
        return Cast.toObject(instance.attributes)
    }

    // Call Methods
    callMethod = this._isACompiledBlock
    callStaticMethod = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    getStaticMethodFunc(args, util) {
        const cls = Cast.toClass(args.CLASS, util.thread)
        const name = Cast.toString(args.NAME)
        const value = cls.getStaticMethod(name)
        return assertType("nimble-heron", FunctionType, value)
    }

    /******************** Functions ********************/

    // Configure Before Define

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    configureNextFunctionArgs(args, util) {
        const argNames = Cast.toArray(args.ARGNAMES).array.map(name => Cast.toString(name))
        const argDefaults = Cast.toArray(args.ARGDEFAULTS).array
        ThreadUtil.getCurrentStack(util.thread).setNextFuncConfig({argNames, argDefaults})
    }

    // Define
    createFunctionAt = this._isACompiledBlock
    createFunctionNamed = this._isACompiledBlock

    // Inside Functions & Methods
    returnValue = this._isACompiledBlock

    // Use Functions
    callFunction = this._isACompiledBlock

    /******************** Utilities ********************/
    objectAsString = this._isACompiledBlock

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    typeofValue(args, util) {
        return TypeChecker.stringTypeof(args.VALUE)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    typeofValueIsMenu(args, util) {
        return (MENUS.TYPEOF_MENU.standardizeBlockInput(args.TYPE) === TypeChecker.typeofCode(args.VALUE))
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    checkIdentity(args, util) {
        return Object.is(args.VALUE1, args.VALUE2)
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    nothing(args, util) {
        return Nothing
    }

    /**
     * @param {BlockArgs} args
     * @param {BlockUtil} util
     */
    executeExpression(args, util) {
        // do nothing
    }

    /************************************************************************************
    *                        Implementation (Helpers) for Blocks                        *
    ************************************************************************************/

    /**
     * @param {*} object
     * @param {Thread} thread
     * @returns {string} the return value of the as string method
     */
    *_objectAsString(object, thread) {
        if (!(object instanceof ClassInstanceType)) return object.toString()
        let method
        try {
            /** @type {InstanceMethodType} */
            method = object.cls.getMemberOfType("__SM_AS_STRING_METHOD__", "CP_INSTANCE_METHOD")
        } catch {}
        if (!method) return object.toString()
        const output = yield* method.execute(thread, object, [])
        if (typeof output !== "string") throwError("As String methods must always return a string.")
        return output
    }

    // Copied from PenguinMod-Vm/src/compiler/jexecute.js
    _mod(n, modulus) {
        let result = n % modulus;
        if (result / modulus < 0) result += modulus;
        return result;
    }



    /**
     * @param {Thread} thread
     * @param {*} left
     * @param {*} right
     * @param {string} leftMethod
     * @param {string} rightMethod
     * @param {string} nodeKind
     * @returns {*}
     */
    *_binaryOperator(thread, left, right, leftMethod, rightMethod, nodeKind) {
        if ((left instanceof ClassInstanceType) && left.hasOperatorMethod(leftMethod)) {
            return yield* left.executeOperatorMethod(thread, leftMethod, right)
        } else if ((right instanceof ClassInstanceType) && right.hasOperatorMethod(rightMethod)) {
            return yield* right.executeOperatorMethod(thread, rightMethod, left)
        }
        // default implementation
        left = Cast.toNumber(left)
        right = Cast.toNumber(right)
        switch (nodeKind) {
            case "op.add": return left + right
            case "op.subtract": return left - right
            case "op.multiply": return left * right
            case "op.divide": return left / right
            case "op.mod":
                return this._mod(left, right)
            case "op.power": return Math.pow(left, right)
        }
        return null
    }

    /**
     * @param {Thread} thread
     * @param {*} left
     * @param {*} right
     * @param {string} oppositeMethod
     * @param {string} method
     * @param {string} nodeKind
     * @returns {boolean|null}
     */
    *_comparisonOperator(thread, left, right, method, oppositeMethod, nodeKind) {
        let foundMethod = false
        let output = undefined
        if ((left instanceof ClassInstanceType) && left.hasOperatorMethod(method)) {
            foundMethod = true
            output = yield* left.executeOperatorMethod(thread, method, right)
        } else if ((right instanceof ClassInstanceType) && right.hasOperatorMethod(oppositeMethod)) {
            foundMethod = true
            output = yield* right.executeOperatorMethod(thread, oppositeMethod, left)
        }
        if (foundMethod) {
            if (typeof output !== "boolean") throwError("Comparison Operator methods must always return a boolean.")
            return output
        }
        // default implementation(see scratch3_operators.js)
        const compareResult = Cast.compare(left, right)
        switch (nodeKind) {
            case "op.equals": return compareResult === 0
            case "op.notequal": return compareResult !== 0
            case "op.greater": return compareResult > 0
            case "op.gtorequal": return compareResult >= 0
            case "op.less": return compareResult < 0
            case "op.ltorequal": return compareResult <= 0
        }
        return null
    }

    /************************************************************************************
    *                                      Helpers                                      *
    ************************************************************************************/

    _isACompiledBlock() {
        throwInternal("spry-hare")
    }
}

const extensionClassInstance = new GCEOOPBlocks()
extensionClassInstance.setup()
Scratch.extensions.register(extensionClassInstance)
if (isRuntimeEnv) {
    runtime.registerCompiledExtensionBlocks("gceOOP", extensionClassInstance.getCompileInfo(true, false))
    runtime.registerCompiledExtensionBlocks("gceFuncsScopes", extensionClassInstance.getCompileInfo(false, true))
}
if (!isRuntimeEnv) {
    console.log("Imported OOP extension in non-runtime environment")
}
})(Scratch)

/************************************************************************************
*                                 Type Definitions                                  *
************************************************************************************/

/**
 * A thread is a running stack context and all the metadata needed.
 * @typedef {Object} Thread
 * @property {ScopeStackManager} [gceSSM]
 */

/**
 * @typedef {Object} ExtensionManager
 * @property {function(string): boolean} isExtensionLoaded
 * @property {function(string): void} loadExtensionIdSync
 * @property {function(string): void} loadExtensionURL
 */

/**
 * @typedef {Object} jwStyleExtensionType
 * @property {Object} Type
 */

/**
 * @typedef {Object} VirtualMachine
 * @property {Object} exports
 * @property {Runtime} runtime
 * @property {ExtensionManager} extensionManager
 * 
 * @property {jwStyleExtensionType} dogeiscutObject - Object Type from extension
 * @property {jwStyleExtensionType} dogeiscutSet - Set Type from extension
 * @property {jwStyleExtensionType} jwArray - Array Type from extension
 * @property {jwStyleExtensionType} jwColor - Color Type from extension
 * @property {jwStyleExtensionType} jwDate - One possible Date Type from extension
 * @property {jwStyleExtensionType} jwLambda - Lambda Type from extension
 * @property {jwStyleExtensionType} jwNum - UnlimitedNum Type from extension
 * @property {jwStyleExtensionType} jwTargets - Target Type (not internal one) from extension
 * @property {jwStyleExtensionType} jwXML - XML Type from extension
 */

/**
 * @typedef {Object} Runtime
 * @property {function(object, object): object} _convertBlockForScratchBlocks
 * @property {function(string, object): void} registerCompiledExtensionBlocks
 * @property {function(string, Function, Function): void} registerSerializer
 * 
 * @property {Object} ext_ddeDateFormat
 * @property {Object} ext_ddeDateFormatV2
 * @property {GCEOOPBlocks} ext_gceOOP
 * @property {GCEFuncsScopesBlocks} [ext_gceFuncsScopes]
 */

/**
 * @typedef {Object} ScratchExtensions
 * @property {boolean} unsandboxed
 * @property {Function} register
 * @property {boolean} isPenguinMod
 * @property {boolean} [isTestingEnv]
 */

/**
 * @typedef {Object} ScratchCast
 * @property {function(*): number} toNumber
 * @property {function(*): boolean} toBoolean
 * @property {function(*): string} toString - Hint to avoid confusion: Cast.toString converts a Scratch value to a string, it does NOT stringify a Cast instance.
 * @property {function(*): Array.<number>} toRgbColorList
 * @property {function(*): {r: number, g: number, b: number, a: number}} toRgbColorObject
 * @property {function(*, number, boolean): (number|string)} toListIndex
 * @property {function(*, *): number} compare
 */

/**
 * @typedef {Object} ScratchObject
 * @property {Object<string, string>} ArgumentType
 * @property {Object<string, ?string>} ArgumentAlignment
 * @property {Object<string, string>} BlockType
 * @property {Object<string, number>} BlockShape
 * @property {Object<string, string>} NotchShape
 * @property {Object<string, string>} TargetType
 * @property {ScratchExtensions} extensions
 * @property {Function} translate
 * @property {VirtualMachine} vm
 * @property {ScratchCast} Cast
 * @property {Object} Clone
 * @property {Object} Color
 */

/**
 * @typedef {Object} ContextScope
 * @property {string} type
 * @property {boolean} [isGlobalScope]
 * @property {boolean} [isUserScope]
 * @property {boolean} [isCallable]
 * @property {boolean} [supportsVars]
 * @property {boolean} [supportsSelf]
 * @property {boolean} [supportsSetterValue]
 * @property {boolean} [supportsOperatorValue]
 * @property {boolean} [supportsCls]
 * @property {VariableManager} [vars]
 * @property {ClassInstanceType} [self]
 * @property {*} [setterValue]
 * @property {*} [other]
 * @property {ClassType} [cls]
 */

/**
 * @typedef {Object} FunctionArgConfig
 * @property {Array<string>} argNames
 * @property {PositionalFunctionArgs} argDefaults
 */

/**
 * @typedef {Array<*>} PositionalFunctionArgs
 */

/**
 * @typedef {Object} BlockArgs
 */

/**
 * @typedef {Object} BlockUtil
 * @property {Thread} thread
 * @property {function(number, boolean, function(): void): void} startBranch
 */


/**
 * TODO
 * 
 * + WORKING ON
 * + - finish project tests
 * + - ensure all menu value handling is consistent and no translated immediate strings are used in code
 * + - properly namespace class members (prefixes) and keep a list of occupied names or so
 * + - why no error raised in funcs scopes (german locale)
 * + - ensure blocks work consistently independent of translation (e.g. stringTypeof)
 * + - typeof block: maybe menu-only block, maybe add "id" vs. "pretty name" option
 * + - proper error framework (maybe in seperate extension)
 * + - ~ throw all errors so that they remember their type
 * + - ~ add catch error of type block
 * + - ~ add get error type block
 *
 * + HIGH PRIORITY
 * + - allow strings for class instance inputs
 * + - consider different architecture for storing block implementations
 * + - consider splitting "OOP" extension again
 * + - update test runner in gallery
 *
 * + MID PRIORITY
 * + - maybe use better custom block shape (example: divIterators.js)
 * + - maybe reorganize block cagegories
 * + - option to exclude super classes when asking for members
 * + - implement right-click switch options for similar blocks
 * + - name of class/function block
 * + - add "all current variable names" or similar block to function definitions
 * + - possibly make "self", "other" and "value" available as a variable in methods
 * + - "delete member of class" block
 * + - reconsider to standardize stacks and scopes index order style
 * + - convert call super init method to call super special method
 * + - "delete", "has", "all" blocks for attributes, class members
 * + - think about other missing blocks accross features
 *
 * + LOW PRIORITY (optional in future)
 * + - button on blocks that opens a section in the documentation about that block
 * + - implement translations
 * + - change font of blocks and inputs?
 * + - define toReporterContent e.g. on ClassInstanceType for better visualization
 * + - investigate why inputs are not supported in shadow blocks
 * + - make as string work for arrays, objects too
 * + - "all variables that are classes/functions" block
 * 
 * + QUICK TASKS
 *
 * + DURING TESTING (do not forget):
 * + - test and/or rework enterClassDefScope
 * + - add project tests for TypeChecker, Cast
 * + - specially test special cases of propertyNamesOfClass
 * + - ensure scopeVarExists is tested properly, especially with multiple scopes
 * + - ensure allVariables is tested properly, especially with multiple scopes
 * + - ensure bindVarToScope is tested properly
 * + - ensure getSuperclass is tested properly
 * + - ensure propertyNamesOfClass edge cases are tested
 * + - test that createVarScope and onClass branch callbacks execute even on error
 *
 * + ON RELEASE / AFTER TESTING:
 * + - remove temporary logStacks block
 * + - change both localhost URLs to extensions.penguinmod URL
 *
 * + DOC NOTES TO REMEMBER
 */
