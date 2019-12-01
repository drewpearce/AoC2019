import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

from helpers import load_inputs_lines  # noqa E402


def main1(inputs):
    return 'main1'


def main2(inputs):
    return 'main2'


if __name__ == "__main__":
    inputs = load_inputs_lines('xx', 'inputs.txt', 'int')
    result1 = main1(inputs)
    result2 = main2(inputs)
    print(result1)
    print(result2)
