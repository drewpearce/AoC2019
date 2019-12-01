from run_01 import calculate_reqs
from run_01 import main1
from run_01 import main2
from run_01 import sum_reqs


TEST_VALS = [12, 14, 1969, 100756]
FUEL_REQS = [2, 2, 654, 33583]
TOTAL_FUEL = sum(FUEL_REQS)


def test_calculate_reqs():
    for i, val in enumerate(TEST_VALS):
        assert calculate_reqs(val) == FUEL_REQS[i]


def test_sum_reqs():
    assert sum_reqs(FUEL_REQS) == TOTAL_FUEL


def test_main1():
    assert main1(TEST_VALS) == TOTAL_FUEL


def test_main2():
    assert main2([14]) == 2
    assert main2([1969]) == 966
    assert main2([100756]) == 50346
