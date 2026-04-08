((Scratch) => {
const {BlockType, ArgumentType, Cast} = Scratch

class TestRunner {
    constructor () {
        this._passed = 0
        this._failed = 0
        this._currentTest = ''
        this._testFailed = false
        this._testErrors = []
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
                    opcode: 'describe',
                    blockType: BlockType.LOOP,
                    text: 'describe [NAME]',
                    arguments: {
                        NAME: { type: ArgumentType.STRING, defaultValue: 'suite name' }
                    }
                },
                {
                    opcode: 'runTest',
                    blockType: BlockType.LOOP,
                    branchCount: 1,
                    text: 'test [NAME]',
                    arguments: {
                        NAME: { type: ArgumentType.STRING, defaultValue: 'test name' }
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
                    opcode: 'assertEqual',
                    blockType: BlockType.COMMAND,
                    text: 'assert [A] = [B]',
                    arguments: {
                        A: { type: ArgumentType.STRING, defaultValue: '' },
                        B: { type: ArgumentType.STRING, defaultValue: '' }
                    }
                },
                {
                    opcode: 'assertThrows',
                    blockType: BlockType.LOOP,
                    branchCount: 1,
                    text: 'assert throws [MSG]',
                    arguments: {
                        MSG: { type: ArgumentType.STRING, defaultValue: '' }
                    }
                },
                {
                    opcode: 'assertDoesNotThrow',
                    blockType: BlockType.LOOP,
                    branchCount: 1,
                    text: 'assert does not throw',
                    arguments: {}
                },
                {
                    opcode: 'fail',
                    blockType: BlockType.COMMAND,
                    text: 'fail [MSG]',
                    arguments: {
                        MSG: { type: ArgumentType.STRING, defaultValue: 'test failed' }
                    }
                },
                '---',
                {
                    opcode: 'reportResults',
                    blockType: BlockType.COMMAND,
                    text: 'report results'
                },
                {
                    opcode: 'resetResults',
                    blockType: BlockType.COMMAND,
                    text: 'reset results'
                },
                {
                    opcode: 'getPassed',
                    blockType: BlockType.REPORTER,
                    disableMonitor: true,
                    text: 'passed'
                },
                {
                    opcode: 'getFailed',
                    blockType: BlockType.REPORTER,
                    disableMonitor: true,
                    text: 'failed'
                }
            ]
        }
    }

    // Logs a suite header with no indentation (indentation not needed per requirements).
    describe (args, util) {
        console.log(`\n${Cast.toString(args.NAME)}`)
        util.startBranch(1, true)
    }

    // C-shaped block. First call sets up test state and starts the branch once.
    // After the branch finishes the VM calls the block again; the second call
    // logs the result and does NOT re-enter the branch, ending the "loop".
    runTest (args, util) {
        if (!util.stackFrame.initialized) {
            util.stackFrame.initialized = true
            this._currentTest = Cast.toString(args.NAME)
            this._testFailed = false
            this._testErrors = []
            util.startBranch(1, true)
        } else {
            if (this._testFailed) {
                console.error(`✗ ${this._currentTest}`)
                for (const err of this._testErrors) {
                    console.error(`  ${err}`)
                }
                this._failed++
            } else {
                console.log(`✓ ${this._currentTest}`)
                this._passed++
            }
        }
    }

    assert (args) {
        if (!Cast.toBoolean(args.CONDITION)) {
            this._failTest('Assertion failed')
        }
    }

    assertNot (args) {
        if (Cast.toBoolean(args.CONDITION)) {
            this._failTest('Assertion failed: expected false but got true')
        }
    }

    assertMsg (args) {
        if (!Cast.toBoolean(args.CONDITION)) {
            this._failTest(Cast.toString(args.MSG))
        }
    }

    assertEqual (args) {
        const a = Cast.toString(args.A)
        const b = Cast.toString(args.B)
        if (a !== b) {
            this._failTest(`Expected "${b}" but got "${a}"`)
        }
    }

    assertThrows (args, util) {
        if (!util.stackFrame.initialized) {
            util.stackFrame.initialized = true
            util.stackFrame.expectedMsg = Cast.toString(args.MSG)
            util.stackFrame.threw = false
            util.stackFrame.caughtMsg = null
            try {
                util.startBranch(1, false)
            } catch (error) {
                util.stackFrame.threw = true
                util.stackFrame.caughtMsg = error?.message ?? String(error)
            }
        } else {
            const { expectedMsg, threw, caughtMsg } = util.stackFrame
            if (!threw) {
                this._failTest('Expected function to throw, but it did not')
            } else if (expectedMsg && !caughtMsg.toLowerCase().includes(expectedMsg.toLowerCase())) {
                this._failTest(`Expected error containing "${expectedMsg}" but got: "${caughtMsg}"`)
            }
        }
    }

    assertDoesNotThrow (args, util) {
        if (!util.stackFrame.initialized) {
            util.stackFrame.initialized = true
            util.stackFrame.threw = false
            util.stackFrame.caughtMsg = null
            try {
                util.startBranch(1, false)
            } catch (error) {
                util.stackFrame.threw = true
                util.stackFrame.caughtMsg = error?.message ?? String(error)
            }
        } else {
            if (util.stackFrame.threw) {
                this._failTest(`Expected no throw, but got: ${util.stackFrame.caughtMsg}`)
            }
        }
    }

    fail (args) {
        this._failTest(Cast.toString(args.MSG))
    }

    reportResults () {
        const total = this._passed + this._failed
        console.log(`\n${this._passed}/${total} passed, ${this._failed} failed`)
    }

    resetResults () {
        this._passed = 0
        this._failed = 0
    }

    getPassed () { return this._passed }
    getFailed () { return this._failed }

    _failTest (message) {
        this._testFailed = true
        this._testErrors.push(message)
    }
}

Scratch.extensions.register(new TestRunner())
})(Scratch)
