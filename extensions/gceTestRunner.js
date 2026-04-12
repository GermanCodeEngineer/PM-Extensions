(/** @param {ScratchObject} Scratch */ (Scratch) => {
const {BlockType, ArgumentType, Cast} = Scratch
const isRuntimeEnv = !Scratch.extensions.isTestingEnv

/**
 * @param {string} s
 * @returns {string}
 */
function quote(s) {
    s = Cast.toString(s)
    s = s.replace(/\\/g, "\\\\").replace(/'/g, "\\'")
    return `'${s}'`
}

class TestError extends Error {
    /**
     * @param {string} message
     * @param {{cause?: *, actualMessage?: ?string, scopePrefix?: ?string}} [options]
     */
    constructor (message, options = {}) {
        super(message, options)
        this.name = "TestError"
        // Full message like a normal error has
        this.fullMessage = message
        // The actual error message (excludes prefixes)
        this.actualMessage = options.actualMessage || null
        // The scope prefixes (e.g., 'test scope "scope name":')
        this.scopePrefix = options.scopePrefix || null
    }

    /**
     * @param {*} error
     * @returns {string}
     */
    static getActualErrorMessage(error) {
        if (error instanceof TestError && error.actualMessage) {
            return error.actualMessage
        }
        if (error instanceof Error) {
            return error.message
        }
        return String(error)
    }

    /**
     * @param {*} error
     * @param {string} substring
     * @returns {boolean}
     */
    static errorContainsMsg(error, substring) {
        if (!substring) return true
        const message = TestError.getActualErrorMessage(error)
        return message.toLowerCase().includes(substring.toLowerCase())
    }

    /**
     * @param {?string} fallback
     * @param {*} cause
     * @returns {?string}
     */
    static preserveActualMessage(fallback, cause) {
        if (fallback !== null && fallback !== undefined) {
            return fallback
        }
        if (cause instanceof TestError && cause.actualMessage) {
            return cause.actualMessage
        }
        return null
    }
}

class TypeChecker {
    static _isVMType(value, vmExtensionKey) {
        if (!isRuntimeEnv) return false
        const vmExtension = Scratch.vm[vmExtensionKey]
        if (!vmExtension || !vmExtension.Type) return false
        return value instanceof vmExtension.Type
    }

    static _stringTypeof(value) {
        if (value === undefined) return "JavaScript Undefined"
        if (value === null) return "JavaScript Null"
        if (typeof value === "boolean") return "Boolean"
        if (typeof value === "number") return "Number"
        if (typeof value === "string") return "String"

        if (TypeChecker._isVMType(value, "jwArray")) return "Array"
        if (TypeChecker._isVMType(value, "dogeiscutObject")) return "Object"
        if (TypeChecker._isVMType(value, "jwDate")) return "Date"
        if (TypeChecker._isVMType(value, "dogeiscutSet")) return "Set"
        if (TypeChecker._isVMType(value, "jwLambda")) return "Lambda"
        if (TypeChecker._isVMType(value, "jwColor")) return "Color"
        if (TypeChecker._isVMType(value, "jwNum")) return "Unlimited Number"
        if (TypeChecker._isVMType(value, "jwTargets")) return "Target"
        if (TypeChecker._isVMType(value, "jwXML")) return "XML"

        if (typeof value === "bigint") return "JavaScript BigInt"
        if (typeof value === "symbol") return "JavaScript Symbol"
        if (typeof value === "function") return "JavaScript Function"
        if (typeof value === "object") return "JavaScript Object"
        return "Unknown"
    }

    static string_typeof(value) {
        return TypeChecker._stringTypeof(value)
    }
}

class TestRunner {
    constructor () {
        this._testScopes = []
        this.quote = quote
        this.TypeChecker = TypeChecker
        this.TestError = TestError
    }

    /** @returns {Object} */
    getInfo () {
        const info = {
            id: 'gceTestRunner',
            name: 'Test Runner',
            color1: '#4a9e6b',
            color2: '#3d8a5e',
            color3: '#2e7050',
            blocks: [
                {
                    opcode: 'testScope',
                    blockType: BlockType.CONDITIONAL,
                    text: 'test scope named [NAME]',
                    arguments: {
                        NAME: { type: ArgumentType.STRING, defaultValue: 'scope name' }
                    }
                },
                '---',
                {
                    opcode: 'assert',
                    blockType: BlockType.COMMAND,
                    text: 'assert [CONDITION]',
                    arguments: {
                        CONDITION: { type: ArgumentType.BOOLEAN }
                    }
                },
                {
                    opcode: 'assertNot',
                    blockType: BlockType.COMMAND,
                    text: 'assert not [CONDITION]',
                    arguments: {
                        CONDITION: { type: ArgumentType.BOOLEAN }
                    }
                },
                {
                    opcode: 'assertMsg',
                    blockType: BlockType.COMMAND,
                    text: 'assert [CONDITION] message [MSG]',
                    arguments: {
                        CONDITION: { type: ArgumentType.BOOLEAN },
                        MSG: { type: ArgumentType.STRING, defaultValue: 'assertion failed' }
                    }
                },
                {
                    opcode: 'assertNotMsg',
                    blockType: BlockType.COMMAND,
                    text: 'assert not [CONDITION] message [MSG]',
                    arguments: {
                        CONDITION: { type: ArgumentType.BOOLEAN },
                        MSG: { type: ArgumentType.STRING, defaultValue: 'assertion failed' }
                    }
                },
                "---",
                {
                    opcode: 'assertStrictEqual',
                    blockType: BlockType.COMMAND,
                    text: 'assert typed equality [A] = [B]',
                    tooltip: 'Compares A and B as raw values without converting to strings (strict typed check).',
                    arguments: {
                        A: { type: ArgumentType.STRING, defaultValue: '' },
                        B: { type: ArgumentType.STRING, defaultValue: '' }
                    }
                },
                {
                    opcode: 'assertStrictNotEqual',
                    blockType: BlockType.COMMAND,
                    text: 'assert typed inequality [A] != [B]',
                    tooltip: 'Compares A and B as raw values without converting to strings (strict typed check).',
                    arguments: {
                        A: { type: ArgumentType.STRING, defaultValue: '' },
                        B: { type: ArgumentType.STRING, defaultValue: '' }
                    }
                },
                {
                    opcode: 'assertUnstrictEqual',
                    blockType: BlockType.COMMAND,
                    text: 'assert string equality [A] = [B]',
                    tooltip: 'Converts both inputs to strings first, then checks for equal text.',
                    arguments: {
                        A: { type: ArgumentType.STRING, defaultValue: '' },
                        B: { type: ArgumentType.STRING, defaultValue: '' }
                    }
                },
                {
                    opcode: 'assertUnstrictNotEqual',
                    blockType: BlockType.COMMAND,
                    text: 'assert string inequality [A] != [B]',
                    tooltip: 'Converts both inputs to strings first, then checks they differ as text.',
                    arguments: {
                        A: { type: ArgumentType.STRING, defaultValue: '' },
                        B: { type: ArgumentType.STRING, defaultValue: '' }
                    }
                },
                {
                    opcode: 'assertTextInValue',
                    blockType: BlockType.COMMAND,
                    text: 'assert text [TEXT] in value [VALUE]',
                    tooltip: 'Converts both inputs to strings and asserts value contains text.',
                    arguments: {
                        TEXT: { type: ArgumentType.STRING, defaultValue: '' },
                        VALUE: { type: ArgumentType.STRING, defaultValue: '' }
                    }
                },
                {
                    opcode: 'assertTextNotInValue',
                    blockType: BlockType.COMMAND,
                    text: 'assert text [TEXT] not in value [VALUE]',
                    tooltip: 'Converts both inputs to strings and asserts value does not contain text.',
                    arguments: {
                        TEXT: { type: ArgumentType.STRING, defaultValue: '' },
                        VALUE: { type: ArgumentType.STRING, defaultValue: '' }
                    }
                },
                {
                    opcode: 'assertType',
                    blockType: BlockType.COMMAND,
                    text: 'assert type of [VALUE] is [EXPECTED]',
                    tooltip: 'Checks the runtime type name of VALUE against the selected expected type.',
                    arguments: {
                        VALUE: { type: ArgumentType.STRING, defaultValue: '' },
                        EXPECTED: { type: ArgumentType.STRING, menu: 'expectedType' }
                    }
                },
                "---",
                {
                    opcode: 'assertThrows',
                    blockType: BlockType.CONDITIONAL,
                    branchCount: 1,
                    text: 'assert throws error',
                },
                {
                    opcode: 'assertThrowsContains',
                    blockType: BlockType.CONDITIONAL,
                    branchCount: 1,
                    text: 'assert throws error containing [MSG]',
                    arguments: {
                        MSG: { type: ArgumentType.STRING, defaultValue: '' }
                    }
                },
                {
                    opcode: 'assertDoesNotThrow',
                    blockType: BlockType.CONDITIONAL,
                    branchCount: 1,
                    text: 'assert does not throw error',
                    arguments: {}
                },
                "---",
                {
                    opcode: 'failTest',
                    blockType: BlockType.COMMAND,
                    text: 'fail test [MSG]',
                    arguments: {
                        MSG: { type: ArgumentType.STRING, defaultValue: 'test failed' }
                    }
                },
            ],
            menus: {
                expectedType: {
                    acceptReporters: false,
                    items: [
                        'Boolean',
                        'Number',
                        'String',
                        'Array',
                        'Object',
                        'Date',
                        'Set',
                        'Lambda',
                        'Color',
                        'Unlimited Number',
                        'Target',
                        'XML',
                        'JavaScript Undefined',
                        'JavaScript Null',
                        'JavaScript BigInt',
                        'JavaScript Symbol',
                        'JavaScript Function',
                        'JavaScript Object',
                        'Unknown'
                    ]
                }
            }
        }
        return info
    }

    /** @returns {{ir: Object<string, Function>, js: Object<string, Function>}} */
    getCompileInfo() {
        const EXTENSION_PREFIX = "runtime.ext_gceTestRunner"

        /**
         * @param {string} kind
         * @param {Array<string>} inputs
         * @returns {(generator: *, block: *) => Object<string, *>}
         */
        const createIRGenerator = (kind, inputs) => ((generator, block) => {
            const result = { kind }
            inputs.forEach(inputName => {
                result[inputName] = inputName === "SUBSTACK"
                    ? generator.descendSubstack(block, inputName)
                    : generator.descendInputOfBlock(block, inputName)
            })
            return result
        })

        /**
         * @param {*} compiler
         * @param {*} substack
         * @param {*} imports
         * @returns {void}
         */
        const addSubstackCode = (compiler, substack, imports) => {
            compiler.descendStack(substack, new imports.Frame(false, undefined, true))
        }

        const irInfo = {
            testScope:            createIRGenerator("stack", ["NAME", "SUBSTACK"]),
            assertThrows:         createIRGenerator("stack", ["SUBSTACK"]),
            assertThrowsContains: createIRGenerator("stack", ["MSG", "SUBSTACK"]),
            assertDoesNotThrow:   createIRGenerator("stack", ["SUBSTACK"]),
        }

        const jsInfo = {
            testScope: (node, compiler, imports) => {
                const nameLocal = compiler.localVariables.next()
                const errLocal = compiler.localVariables.next()
                compiler.source += `const ${nameLocal} = ${compiler.descendInput(node.NAME).asString()};\n`
                compiler.source += `${EXTENSION_PREFIX}._testScopes.push(${nameLocal})\n`
                compiler.source += `try {\ntry {\n`
                addSubstackCode(compiler, node.SUBSTACK, imports)
                compiler.source += `} catch (${errLocal}) {\n`
                compiler.source += `  throw ${EXTENSION_PREFIX}._wrapError(\`test scope \${${EXTENSION_PREFIX}.quote(${nameLocal})}:\`, ${errLocal});\n`
                compiler.source += `}} finally {\n${EXTENSION_PREFIX}._testScopes.pop();\n}\n`
            },
            assertThrows: (node, compiler, imports) => {
                const errLocal = compiler.localVariables.next()
                compiler.source += `let ${errLocal};\n`
                compiler.source += `try {\n`
                addSubstackCode(compiler, node.SUBSTACK, imports)
                compiler.source += `} catch (${errLocal}) {}\n`
                compiler.source += `if (!${errLocal}) throw new ${EXTENSION_PREFIX}.TestError("Expected exception but none was thrown");\n`
            },
            assertThrowsContains: (node, compiler, imports) => {
                const errLocal = compiler.localVariables.next()
                const expectedLocal = compiler.localVariables.next()
                compiler.source += `let ${errLocal};\n`
                compiler.source += `try {\n`
                addSubstackCode(compiler, node.SUBSTACK, imports)
                compiler.source += `} catch (${errLocal}) {}\n`
                compiler.source += `const ${expectedLocal} = ${compiler.descendInput(node.MSG).asString()};\n`
                compiler.source += `if (!${errLocal}) throw new ${EXTENSION_PREFIX}.TestError("Expected exception but none was thrown");\n`
                compiler.source += `if (!${EXTENSION_PREFIX}.TestError.errorContainsMsg(${errLocal}, ${expectedLocal})) `+
                    `throw ${EXTENSION_PREFIX}._errorWithCause(\`Expected exception containing \${${EXTENSION_PREFIX}.quote(${expectedLocal})} but got \${${EXTENSION_PREFIX}.quote(${EXTENSION_PREFIX}.TestError.getActualErrorMessage(${errLocal}))}\`, ${errLocal});\n`
            },
            assertDoesNotThrow: (node, compiler, imports) => {
                const errLocal = compiler.localVariables.next()
                compiler.source += `let ${errLocal};\n`
                compiler.source += `try {\n`
                addSubstackCode(compiler, node.SUBSTACK, imports)
                compiler.source += `} catch (${errLocal}) {}\n`
                compiler.source += `if (${errLocal}) throw ${EXTENSION_PREFIX}._errorWithCause(\`Unexpected exception: \${${EXTENSION_PREFIX}._errorMessage(${errLocal})}\`, ${errLocal});\n`
            },
            failTest: (node, compiler) => {
                compiler.source += `throw new ${EXTENSION_PREFIX}.TestError(\`Test failed: \${${compiler.descendInput(node.MSG).asString()}}\`);\n`
            },
        }

        return { ir: irInfo, js: jsInfo }
    }

    // Compiled-only blocks
    testScope = this._isACompiledBlock
    assertThrows = this._isACompiledBlock
    assertThrowsContains = this._isACompiledBlock
    assertDoesNotThrow = this._isACompiledBlock

    _isACompiledBlock() {
        throw new TestError(
            "This block only works in compiled mode. " +
            "Make sure the Test Runner extension is registered with compiled block support."
        )
    }

    /** @param {Object} args */
    assert ({CONDITION}) {
        CONDITION = Cast.toBoolean(CONDITION)
        if (!CONDITION) throw new TestError("Assertion failed: condition was false")
    }

    /** @param {Object} args */
    assertNot ({CONDITION}) {
        CONDITION = Cast.toBoolean(CONDITION)
        if (CONDITION) throw new TestError("Assertion failed: condition was true")
    }

    /** @param {Object} args */
    assertMsg ({CONDITION, MSG}) {
        CONDITION = Cast.toBoolean(CONDITION)
        MSG = Cast.toString(MSG)
        if (!CONDITION) throw new TestError(`Assertion failed: condition was false: ${MSG}`)
    }

    /** @param {Object} args */
    assertNotMsg ({CONDITION, MSG}) {
        CONDITION = Cast.toBoolean(CONDITION)
        MSG = Cast.toString(MSG)
        if (CONDITION) throw new TestError(`Assertion failed: condition was true: ${MSG}`)
    }

    /** @param {Object} args */
    assertStrictEqual ({A, B}) {
        if (A !== B) throw new TestError(`Assertion failed: got ${this._valueWithType(A)}, expected ${this._valueWithType(B)}`)
    }

    /** @param {Object} args */
    assertStrictNotEqual ({A, B}) {
        if (A === B) throw new TestError(`Assertion failed: values unexpectedly equal: ${this._valueWithType(A)} and ${this._valueWithType(B)}`)
    }

    /** @param {Object} args */
    assertUnstrictEqual ({A, B}) {
        const aStr = Cast.toString(A)
        const bStr = Cast.toString(B)
        if (aStr !== bStr) throw new TestError(`Assertion failed: got ${quote(aStr)}, expected ${quote(bStr)}`)
    }

    /** @param {Object} args */
    assertUnstrictNotEqual ({A, B}) {
        const aStr = Cast.toString(A)
        const bStr = Cast.toString(B)
        if (aStr === bStr) throw new TestError(`Assertion failed: values unexpectedly equal: ${quote(aStr)}`)
    }

    /** @param {Object} args */
    assertTextInValue ({TEXT, VALUE}) {
        const textStr = Cast.toString(TEXT)
        const valueStr = Cast.toString(VALUE)
        if (!valueStr.includes(textStr)) throw new TestError(`Assertion failed: text ${quote(textStr)} not found in value ${quote(valueStr)}`)
    }

    /** @param {Object} args */
    assertTextNotInValue ({TEXT, VALUE}) {
        const textStr = Cast.toString(TEXT)
        const valueStr = Cast.toString(VALUE)
        if (valueStr.includes(textStr)) throw new TestError(`Assertion failed: text ${quote(textStr)} unexpectedly found in value ${quote(valueStr)}`)
    }

    /** @param {Object} args */
    assertType ({VALUE, EXPECTED}) {
        const expectedType = Cast.toString(EXPECTED)
        const actualType = this.TypeChecker.string_typeof(VALUE)
        if (actualType !== expectedType) {
            throw new TestError(
                `Assertion failed: expected type ${quote(expectedType)} but got ${quote(actualType)} for value ${quote(VALUE)}`
            )
        }
    }

    /** @param {Object} args */
    failTest ({MSG}) {
        throw new TestError(`Test failed: ${Cast.toString(MSG)}`)
    }


    
    /**
     * @param {*} error
     * @returns {string}
     */
    _errorMessage (error) {
        return this._formatErrorLines(error).join("\n")
    }

    /**
     * @param {*} value
     * @returns {string}
     */
    _typeLabel (value) {
        if (value === null) return "null"
        if (value === undefined) return "undefined"
        const baseType = typeof value
        const ctorName = value && value.constructor && value.constructor.name
        return ctorName ? `${baseType} (${ctorName})` : baseType
    }

    /**
     * @param {*} value
     * @returns {string}
     */
    _valueWithType (value) {
        return `${quote(value)} [${this._typeLabel(value)}]`
    }

    /**
     * @param {string} message
     * @param {*} cause
     * @returns {TestError}
     */
    _wrapError (message, cause) {
        const combinedMessage = [
            message,
            ...this._formatErrorLines(cause)
        ].join("\n")
        const innerActualMessage = TestError.preserveActualMessage(null, cause)
        return this._errorWithCause(combinedMessage, cause, message, innerActualMessage)
    }

    /**
     * @param {string} message
     * @param {*} cause
     * @param {?string} [scopePrefix]
     * @param {?string} [actualMessage]
     * @returns {TestError}
     */
    _errorWithCause (message, cause, scopePrefix = null, actualMessage = null) {
        return new TestError(message, { 
            cause,
            scopePrefix,
            actualMessage: TestError.preserveActualMessage(actualMessage, cause)
        })
    }

    /**
     * @param {*} error
     * @returns {Array<string>}
     */
    _formatErrorLines (error) {
        if (!(error instanceof Error)) return [String(error)]
        return String(error.message).split("\n")
    }
}

const testRunnerInstance = new TestRunner()

if (isRuntimeEnv) {
    const runtime = Scratch.vm.runtime
    const oldConvertBlock = runtime._convertBlockForScratchBlocks.bind(runtime)
    if (!oldConvertBlock.tooltipImplementationAdded) {
        /**
         * @param {Object} blockInfo
         * @param {Object} categoryInfo
         * @returns {Object}
         */
        runtime._convertBlockForScratchBlocks = function (blockInfo, categoryInfo) {
            const result = oldConvertBlock(blockInfo, categoryInfo)
            if (blockInfo.tooltip) {
                result.json.tooltip = blockInfo.tooltip
            }
            return result
        }
        runtime._convertBlockForScratchBlocks.tooltipImplementationAdded = true
    }
}

Scratch.extensions.register(testRunnerInstance)
if (isRuntimeEnv) {
    Scratch.vm.runtime.registerCompiledExtensionBlocks(
        "gceTestRunner", testRunnerInstance.getCompileInfo(),
    )
}
})(Scratch)
