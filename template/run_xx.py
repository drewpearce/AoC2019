import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

from helpers import load_inputs_lines  # noqa E402
from helpers import Timer  # noqa E402


def main1(data=None):
    if not data:
        data = load_inputs_lines('xx', 'inputs.txt', 'int')

    return 'main1'


def main2(data=None):
    if not data:
        data = load_inputs_lines('xx', 'inputs.txt', 'int')

    return 'main2'


if __name__ == "__main__":
    timer = Timer()
    result1 = main1()
    timer.stop()
    print(result1)
    print(f'{timer.duration} ms')

    timer.start()
    result2 = main2()
    timer.stop()
    print(result2)
    print(f'{timer.duration} ms')
