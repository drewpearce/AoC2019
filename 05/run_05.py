import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

from helpers import IntcodeComputer  # noqa E401
from helpers import load_inputs_lines  # noqa E402
from helpers import Timer  # noqa E402


def main1(data=None):
    if not data:
        data = load_inputs_lines('05', 'inputs.txt')
        data = data[0]
        data = [int(d) for d in data.split(',')]

    diagnostics = IntcodeComputer(data, 1)
    diagnostics.run()

    return diagnostics.output


def main2(data=None):
    if not data:
        data = load_inputs_lines('05', 'inputs.txt')
        data = data[0]
        data = [int(d) for d in data.split(',')]

    diagnostics = IntcodeComputer(data, 5)
    diagnostics.run()

    return diagnostics.output


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
