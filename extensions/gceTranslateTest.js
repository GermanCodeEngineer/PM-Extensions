(/** @param {ScratchObject} Scratch */ function (Scratch) {
"use strict"

const TRANSLATIONS = {
    en: {
        "_M_TRANSLATE_TEST": "Translate Test",
        "_M_HELLO_BLOCK": "hello [NAME]",
        "_M_RETURNS": "Returns a translated greeting",
        "_M_HELLO_MSG": "Hello {name}!",
    },
}
Scratch.translate.setup(TRANSLATIONS)

const {BlockType, ArgumentType} = Scratch

function translatedMsg(englishMessageTemplate, values = {}) {
    return Scratch.translate(englishMessageTemplate, values)
}

class GCETranslateTest {
    getInfo() {
        return {
            id: "gceTranslateTest",
            name: translatedMsg("M_TRANSLATE_TEST"),
            color1: "#4a90e2",
            blocks: [
                {
                    blockType: BlockType.REPORTER,
                    opcode: "greetName",
                    text: translatedMsg("M_HELLO_BLOCK"),
                    tooltip: translatedMsg("M_RETURNS"),
                    arguments: {
                        NAME: {
                            type: ArgumentType.STRING,
                            defaultValue: "World",
                        },
                    },
                },
            ],
        }
    }

    greetName(args) {
        return translatedMsg("M_HELLO_MSG", {name: args.NAME})
    }
}

Scratch.extensions.register(new GCETranslateTest())
})(Scratch)
