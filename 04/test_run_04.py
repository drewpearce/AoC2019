from run_04 import has_double
from run_04 import has_isolated_double
from run_04 import next_up


def test_next_up():
    cases = [
        {
            'in': '12343',
            'out': '12344'
        },
        {
            'in': '435234',
            'out': '444444'
        },
        {
            'in': '115344',
            'out': '115555'
        },
        {
            'in': '234567',
            'out': '234577'
        },
        {
            'in': '356889',
            'out': '356889'
        },
        {
            'in': '123456',
            'out': '123466'
        }
    ]

    for case in cases:
        assert next_up(case['in']) == case['out']


def test_has_double():
    cases = [
        {
            'in': '1234',
            'out': False
        },
        {
            'in': '1232',
            'out': False
        },
        {
            'in': '1',
            'out': False
        },
        {
            'in': '1223',
            'out': True
        }
    ]

    for case in cases:
        assert has_double(case['in']) == case['out']


def test_has_isolated_double():
    cases = [
        {
            'in': '1234',
            'out': False
        },
        {
            'in': '1232',
            'out': False
        },
        {
            'in': '1',
            'out': False
        },
        {
            'in': '1223',
            'out': True
        },
        {
            'in': '111234',
            'out': False
        },
        {
            'in': '112233',
            'out': True
        },
        {
            'in': '123444',
            'out': False
        },
        {
            'in': '122223',
            'out': False
        },
        {
            'in': '111123',
            'out': False
        },
        {
            'in': '111122',
            'out': True
        }
    ]

    for case in cases:
        assert has_isolated_double(case['in']) == case['out']
