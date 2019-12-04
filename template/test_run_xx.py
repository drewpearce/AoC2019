from run_xx import main1
from run_xx import main2


TEST_VALS = {
    'inputs': [
        ['test']
    ],
    'result1': ['main1'],
    'result2': ['main2']
}


def test_main1():
    for i, val in enumerate(TEST_VALS['inputs']):
        assert main1(val) == TEST_VALS['result1'][i]


def test_main2():
    for i, val in enumerate(TEST_VALS['inputs']):
        assert main2(val) == TEST_VALS['result2'][i]
