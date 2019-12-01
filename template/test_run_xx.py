from run_xx import main1
from run_xx import main2


TEST_VALS = {
    'inputs': [],
    'result1': 'main1',
    'result2': 'main2'
}


def test_main1():
    assert main1(TEST_VALS['inputs']) == TEST_VALS['result1']


def test_main2():
    assert main2(TEST_VALS['inputs']) == TEST_VALS['result2']
