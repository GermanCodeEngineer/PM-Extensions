((Scratch) => {
const {BlockType, ArgumentType, Cast} = Scratch

class TestRunner {
    constructor () {
        this._testScopes = []
    }

    getInfo () {
        return {
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
                        NAME: { type: ArgumentType.STRING, defaultValue: 'suite name' }
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
                    opcode: 'assertEqual',
                    blockType: BlockType.COMMAND,
                    text: 'assert [A] = [B]',
                    arguments: {
                        A: { type: ArgumentType.STRING, defaultValue: '' },
                        B: { type: ArgumentType.STRING, defaultValue: '' }
                    }
                },
                {
                    opcode: 'assertNotEqual',
                    blockType: BlockType.COMMAND,
                    text: 'assert [A] != [B]',
                    arguments: {
                        A: { type: ArgumentType.STRING, defaultValue: '' },
                        B: { type: ArgumentType.STRING, defaultValue: '' }
                    }
                },
                {
                    opcode: 'assertEqualMsg',
                    blockType: BlockType.COMMAND,
                    text: 'assert [A] = [B] message [MSG]',
                    arguments: {
                        A: { type: ArgumentType.STRING, defaultValue: '' },
                        B: { type: ArgumentType.STRING, defaultValue: '' },
                        MSG: { type: ArgumentType.STRING, defaultValue: 'assertion failed' }
                    }
                },
                {
                    opcode: 'assertNotEqualMsg',
                    blockType: BlockType.COMMAND,
                    text: 'assert [A] != [B] message [MSG]',
                    arguments: {
                        A: { type: ArgumentType.STRING, defaultValue: '' },
                        B: { type: ArgumentType.STRING, defaultValue: '' },
                        MSG: { type: ArgumentType.STRING, defaultValue: 'assertion failed' }
                    }
                },
                "---",
                {
                    opcode: 'assertThrows',
                    blockType: BlockType.CONDITIONAL,
                    branchCount: 1,
                    text: 'assert throws',
                },
                {
                    opcode: 'assertThrowsContains',
                    blockType: BlockType.CONDITIONAL,
                    branchCount: 1,
                    text: 'assert throws [MSG]',
                    arguments: {
                        MSG: { type: ArgumentType.STRING, defaultValue: '' }
                    }
                },
                {
                    opcode: 'assertDoesNotThrow',
                    blockType: BlockType.CONDITIONAL,
                    branchCount: 1,
                    text: 'assert does not throw',
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
            ]
        }
    }

    testScope (args, util) {
        this._testScopes.push(Cast.toString(args.NAME))
        
        try {
            try {
                util.startBranch(1, false)
            } catch (err) {
                throw this._errorWithCause(
                    `TestScope "${Cast.toString(args.NAME)}": ${this._errorMessage(err)}`,
                    err
                )
            }
        } finally {
            this._testScopes.pop()
        }
    }

    assert (args) {
        if (!Cast.toBoolean(args.CONDITION)) {
            throw new Error("BoolAssertion: condition is unexpectedly false")
        }
    }

    assertNot (args) {
        if (Cast.toBoolean(args.CONDITION)) {
            throw new Error("BoolAssertion: condition is unexpectedly true")
        }
    }

    assertMsg (args) {
        if (!Cast.toBoolean(args.CONDITION)) {
            throw new Error(`BoolAssertion: condition is unexpectedly false: ${Cast.toString(args.MSG)}`)
        }
    }

    assertNotMsg (args) {
        if (Cast.toBoolean(args.CONDITION)) {
            throw new Error(`BoolAssertion: condition is unexpectedly true: ${Cast.toString(args.MSG)}`)
        }
    }

    assertEqual (args) {
        const a = Cast.toString(args.A)
        const b = Cast.toString(args.B)
        if (a !== b) {
            throw new Error(`ComparisonAssertion: expected "${b}" but got "${a}"`)
        }
    }

    assertNotEqual (args) {
        const a = Cast.toString(args.A)
        const b = Cast.toString(args.B)
        if (a === b) {
            throw new Error(`ComparisonAssertion: expected not, but still got: "${a}"`)
        }
    }

    assertEqualMsg (args) {
        const a = Cast.toString(args.A)
        const b = Cast.toString(args.B)
        if (a !== b) {
            throw new Error(`ComparisonAssertion: expected "${b}" but got "${a}": ${Cast.toString(args.MSG)}`)
        }
    }

    assertNotEqualMsg (args) {
        const a = Cast.toString(args.A)
        const b = Cast.toString(args.B)
        if (a === b) {
            throw new Error(`ComparisonAssertion: expected not, but still got: "${a}": ${Cast.toString(args.MSG)}`)
        }
    }

    assertThrows(args, util) {
        let error = undefined
        try {
            util.startBranch(1, false)
        } catch (err) {
            error = err
        }
        if (!error) {
            throw new Error(`InvalidThrow: Expected error, but no error was thrown`)
        }
    }

    assertThrowsContains(args, util) {
        let error = undefined
        try {
            util.startBranch(1, false)
        } catch (err) {
            error = err
        }
        const expectedMsg = Cast.toString(args.MSG)
        const actualMsg = this._errorMessage(error)
        if (expectedMsg && !actualMsg.toLowerCase().includes(expectedMsg.toLowerCase())) {
            throw this._errorWithCause(
                `InvalidThrow: Expected error containing "${expectedMsg}" but got: "${actualMsg}"`,
                error
            )
        }
    }

    assertDoesNotThrow(args, util) {
        let error = undefined
        try {
            util.startBranch(1, false)
        } catch (err) {
            error = err
        }
        if (error) {
            throw this._errorWithCause(
                `InvalidThrow: Expected no error, but got: ${this._errorMessage(error)}`,
                error
            )
        }
    }

    failTest(args) {
        throw new Error(`FailTest: ${Cast.toString(args.MSG)}`)
    }


    _errorMessage (error) {
        if (error instanceof Error) return error.message
        return String(error)
    }

    _errorWithCause (message, cause) {
        return new Error(message, { cause })
    }

    _formatErrorLines (error) {
        if (!(error instanceof Error)) return [String(error)]

        const lines = [error.message]
        let cause = error.cause
        while (cause !== undefined) {
            if (cause instanceof Error) {
                lines.push(`caused by: ${cause.message}`)
                cause = cause.cause
            } else {
                lines.push(`caused by: ${String(cause)}`)
                break
            }
        }
        return lines
    }
}

Scratch.extensions.register(new TestRunner())
})(Scratch)
