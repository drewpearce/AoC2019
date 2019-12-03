from run_03 import main1
from run_03 import main2


TEST_VALS = {
    'inputs': [
        [
            'R75,D30,R83,U83,L12,D49,R71,U7,L72',
            'U62,R66,U55,R34,D71,R55,D58,R83'
        ],
        [
            'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
            'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
        ]
    ],
    'result1': [
        159,
        135
    ],
    'result2': [
        610,
        410
    ]
}


def test_main1():
    for i, val in enumerate(TEST_VALS['inputs']):
        assert main1(val) == TEST_VALS['result1'][i]


def test_main2():
    for i, val in enumerate(TEST_VALS['inputs']):
        assert main2(val) == TEST_VALS['result2'][i]
