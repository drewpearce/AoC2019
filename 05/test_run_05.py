from helpers import IntcodeComputer


def test_parameter_mode():
    test = IntcodeComputer([1002, 4, 3, 4, 33])
    test.run()
    assert test.instructions[4] == 99


def test_op_code_3():
    test = IntcodeComputer([3, 2, 0], 99)
    test.save_in([(0, 2)])
    assert test.instructions[2] == 99

    test = IntcodeComputer([3, 2, 0], 99)
    test.run()
    assert test.inputs == 99
    assert test.instructions == [3, 2, 99]


def test_op_code_4():
    test = IntcodeComputer([104, 6, 104, 7, 99])
    test.save_out([(1, 6)])
    assert test.output == [6]

    test = IntcodeComputer([104, 6, 104, 7, 99])
    test.run()
    assert test.output == [6, 7]


def test_op_code_5():
    test = IntcodeComputer([1105, 0, 4, 1105, 1, 10, 0, 4, 6, 34, 99])
    test.jump_if_true([(1, 0), (1, 4)])
    assert test.ptr == 3
    test.jump_if_true([(1, 1), (1, 10)])
    assert test.ptr == 10

    test = IntcodeComputer([1105, 0, 4, 1105, 1, 10, 0, 4, 6, 34, 99])
    test.run()
    assert test


def test_op_code_6():
    test = IntcodeComputer([1106, 1, 4, 1106, 0, 10, 0, 4, 6, 34, 99])
    test.jump_if_false([(1, 1), (1, 4)])
    assert test.ptr == 3
    test.jump_if_false([(1, 0), (1, 10)])
    assert test.ptr == 10

    test = IntcodeComputer([1106, 1, 4, 1106, 0, 10, 0, 4, 6, 34, 99])
    test.run()
    assert test


def test_op_code_7():
    test = IntcodeComputer([11107, 4, 5, 3, 99])
    test.less_than([(1, 5), (1, 4), (1, 3)])
    assert test.instructions[3] == 0
    test.less_than([(1, 4), (1, 5), (1, 3)])
    assert test.instructions[3] == 1

    test = IntcodeComputer([11107, 4, 5, 3, 99])
    test.run()
    assert test.instructions[3] == 1


def test_op_code_8():
    test = IntcodeComputer([11108, 4, 4, 3, 99])
    test.equals([(1, 5), (1, 4), (1, 3)])
    assert test.instructions[3] == 0
    test.equals([(1, 4), (1, 4), (1, 3)])
    assert test.instructions[3] == 1

    test = IntcodeComputer([11108, 4, 4, 3, 99])
    test.run()
    assert test.instructions[3] == 1


def test_run():
    cases = [
        {
            'data': [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8],
            'input': 8,
            'expected': 1
        },
        {
            'data': [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8],
            'input': 7,
            'expected': 0
        },
        {
            'data': [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8],
            'input': 8,
            'expected': 0
        },
        {
            'data': [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8],
            'input': 7,
            'expected': 1
        },
        {
            'data': [3, 3, 1108, -1, 8, 3, 4, 3, 99],
            'input': 8,
            'expected': 1
        },
        {
            'data': [3, 3, 1108, -1, 8, 3, 4, 3, 99],
            'input': 7,
            'expected': 0
        },
        {
            'data': [3, 3, 1107, -1, 8, 3, 4, 3, 99],
            'input': 7,
            'expected': 1
        },
        {
            'data': [3, 3, 1107, -1, 8, 3, 4, 3, 99],
            'input': 8,
            'expected': 0
        },
        {
            'data': [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9],
            'input': 0,
            'expected': 0
        },
        {
            'data': [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9],
            'input': 4,
            'expected': 1
        },
        {
            'data': [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1],
            'input': 0,
            'expected': 0
        },
        {
            'data': [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1],
            'input': 4,
            'expected': 1
        },
        {
            'data': [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20,
                     1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4,
                     20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20,
                     4, 20, 1105, 1, 46, 98, 99],
            'input': 7,
            'expected': 999
        },
        {
            'data': [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20,
                     1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4,
                     20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20,
                     4, 20, 1105, 1, 46, 98, 99],
            'input': 8,
            'expected': 1000
        },
        {
            'data': [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20,
                     1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4,
                     20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20,
                     4, 20, 1105, 1, 46, 98, 99],
            'input': 9,
            'expected': 1001
        }
    ]

    for case in cases:
        this = IntcodeComputer(case['data'], case['input'])
        this.run()
        assert this.output[-1] == case['expected']
