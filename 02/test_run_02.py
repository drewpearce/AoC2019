from run_02 import main1
from run_02 import main2


TEST_VALS = {
    'inputs': [
        [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
        [1, 0, 0, 0, 99],
        [2, 3, 0, 3, 99],
        [2, 4, 4, 5, 99, 0],
        [1, 1, 1, 4, 99, 5, 6, 0, 99]
    ],
    'result1': [
        [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        [2, 0, 0, 0, 99],
        [2, 3, 0, 6, 99],
        [2, 4, 4, 5, 99, 9801],
        [30, 1, 1, 4, 2, 5, 6, 0, 99]
    ],
    'result2': 'main2'
}


def test_main1():
    for i,  val in enumerate(TEST_VALS['inputs']):
        assert main1(val) == TEST_VALS['result1'][i]


def test_main2():
    assert main2(TEST_VALS['inputs'][0]) == TEST_VALS['result2']
