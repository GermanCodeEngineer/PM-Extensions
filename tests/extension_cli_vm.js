// Adapted from https://github.com/GermanCodeEngineer/py-pmp-manip/blob/main/pmp_manip/ext_info_gen/direct_extractor.js

const fs = require("fs")
const path = require("path")
const vm = require("vm")

// ---------- Setup Stubs and Proxy ----------

let registeredExtensionInstance = null
let defaultStubValue

// This design was chosen because all these three will work with the above value as X
// const y = new X()
// X()
// const {a, b} = X
// X.a.b ...
// ... (keep your other imports and code)    

function makeConfiguredStub({
    basis = null,
    valueProps = {},
    funcProps = [],
    allowStaticGet = false,
} = {}) {
    // The stub function/object to return for everything else
    if (basis === null) {
        basis = Object.create(null)
    }

    basis.toString = basis.valueOf = basis[Symbol.toPrimitive] = () => "[STUB PROPERTY]"

    // Assign known props
    for (const [key, value] of Object.entries(valueProps)) {
        basis[key] = value
    }
    for (const funcName of funcProps) {
        basis[funcName] = function () {
            return defaultStubValue
        }
    }

    // Proxy only property accesses, not apply/construct
    return new Proxy(basis, {
        get(target, prop, receiver) {
            if (Object.prototype.hasOwnProperty.call(target, prop)) {
                return target[prop]
            }
            if (allowStaticGet && typeof prop === "string" && /^[A-Z0-9_]+$/.test(prop)) {
                return prop
            }
            if (prop === Symbol.toStringTag) return "Function"
            if (prop === "prototype") return target.prototype
            if (prop === "constructor") return target.constructor
            return defaultStubValue
        },
    })
}

// Create the ultimate stub globally
defaultStubValue = makeConfiguredStub({
  basis: function () {return defaultStubValue},
  valueProps: {},
  funcProps: [],
  allowStaticGet: false,
})



// Derived from https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/engine/runtime.js
const runtimeStub = makeConfiguredStub({
    basis: Object.create(null),
    allowStaticGet: true, // allow e.g. PROJECT_START
})

const ScratchVar = makeConfiguredStub({
    basis: Object.create(null),
    valueProps: {
        // Derived from https://github.com/PenguinMod/PenguinMod-Vm/blob/develop/src/extension-support/tw-extension-api-common.js
        ArgumentType: {
            "ANGLE": "angle",
            "BOOLEAN": "Boolean",
            "COLOR": "color",
            "NUMBER": "number",
            "STRING": "string",
            "MATRIX": "matrix",
            "NOTE": "note",
            "IMAGE": "image",
            "POLYGON": "polygon",
            "CUSTOM": "custom",
            "COSTUME": "costume",
            "SOUND": "sound",
            "VARIABLE": "variable",
            "LIST": "list",
            "BROADCAST": "broadcast",
            "SEPERATOR": "seperator"
        },
        ArgumentAlignment: {
            "DEFAULT": null,
            "LEFT": "LEFT",
            "CENTER": "CENTRE",
            "RIGHT": "RIGHT"
        },
        BlockType: {
            "BOOLEAN": "Boolean",
            "BUTTON": "button",
            "LABEL": "label",
            "COMMAND": "command",
            "CONDITIONAL": "conditional",
            "EVENT": "event",
            "HAT": "hat",
            "LOOP": "loop",
            "REPORTER": "reporter",
            "XML": "xml"
        },
        BlockShape: {
            "HEXAGONAL": 1,
            "ROUND": 2,
            "SQUARE": 3,
            "LEAF": 4,
            "PLUS": 5
        },
        NotchShape: {
            "SWITCH": "switchCase",
            "HEXAGON": "hexagon",
            "ROUND": "round",
            "SQUARE": "square",
            "LEAF": "leaf",
            "PLUS": "plus",
            "OCTAGONAL": "octagonal",
            "BUMPED": "bumped",
            "INDENTED": "indented",
            "SCRAPPED": "scrapped",
            "ARROW": "arrow",
            "TICKET": "ticket",
            "JIGSAW": "jigsaw",
            "INVERTED": "inverted",
            "PINCER": "pincer",
        },
        TargetType: {
            "SPRITE": "sprite",
            "STAGE": "stage"
        },
        extensions: makeConfiguredStub({
            basis: Object.create(null),
            valueProps: {
                unsandboxed: true,
                register: (ext) => { registeredExtensionInstance = ext },
                isPenguinMod: true,
                // Custom property to detect the test environment
                isTestingEnv: true,
            },
        }),
        translate: makeConfiguredStub({
            basis: (m) => (typeof m === "string" ? m : m.default || ""),
            valueProps: {
                setup: makeConfiguredStub({
                    basis: (newTranslations) => makeConfiguredStub({
                        basis: Object.create(null),
                        valueProps: {
                            locale: "en",
                        },
                    }),
                }),
            },
        }),

        vm: makeConfiguredStub({
            basis: Object.create(null),
            valueProps: {
                runtime: runtimeStub,
            },
        }),
        // I only included the properties which a resonable outer extension code or getInfo should use

        // To allow builtin PM extension to import them (they are not used in outer extension or getInfo)
        Cast: makeConfiguredStub({
            basis: function () { return defaultStubValue },
            valueProps: {
                toString: (value) => String(value),
            },
        }),
        Clone: defaultStubValue,
        Color: defaultStubValue,
    },
})



const vmEnvironment = {
    ...global,
    // Important:
    console,  // not enumerable on global, must be explicit
    module: { exports: {} },
    require: () => defaultStubValue,
    Scratch: ScratchVar,
    vm: ScratchVar.vm,
    
    window: makeConfiguredStub({
        basis: Object.create(null),
        valueProps: {
            vm: ScratchVar.vm,
        },
    }),
    document: defaultStubValue,
    localStorage: defaultStubValue,
    MutationObserver: defaultStubValue,
}


// ---------- VM execution wrapper ----------

function importExtensionByCode(code, filename) {
    registeredExtensionInstance = null
    try {
        vm.createContext(vmEnvironment)
        vm.runInContext(code, vmEnvironment, { filename })
        return registeredExtensionInstance
    } catch (error) {
        if (error && error.stack) {
            console.error(error.stack)
        } else {
            console.error(error)
        }
        process.exit(1)
    }
}

function importExtensionByPath(filePath) {
    const fullExtensionPath = path.resolve(filePath)
    const code = fs.readFileSync(fullExtensionPath, "utf-8")
    return importExtensionByCode(code, fullExtensionPath)
}

// ---------- Entry point ----------

if (require.main === module) { // like if __name__ == "__main__"
    const filePath = process.argv[2]
    importExtensionByPath(filePath)
    process.exit(0)
}

module.exports = {
    vmEnvironment,
    defaultStubValue,
    importExtensionByCode,
    importExtensionByPath,
}
