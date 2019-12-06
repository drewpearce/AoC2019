import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

from helpers import load_inputs_lines  # noqa E402
from helpers import IntcodeComputer


def main1(inputs):
    comp = IntcodeComputer(inputs)
    comp.run()
    return comp.instructions


def load_inputs_1():
    inputs = load_inputs_lines('02', 'inputs.txt')
    inputs = [int(x) for x in inputs[0].split(',')]
    inputs[1] = 12
    inputs[2] = 2
    return inputs


def load_inputs_2():
    inputs = load_inputs_lines('02', 'inputs.txt')
    inputs = [int(x) for x in inputs[0].split(',')]
    return inputs


def main2():
    for x in range(100):
        for y in range(100):
            inputs = load_inputs_2()
            inputs[1] = x
            inputs[2] = y
            result = main1(inputs)
            if result[0] == 19690720:
                break
        if result[0] == 19690720:
            break

    noun = result[1]
    verb = result[2]
    print(f'{noun}, {verb}')
    return noun * 100 + verb


if __name__ == "__main__":
    inputs = load_inputs_1()
    result1 = main1(inputs)
    print(result1[0])
    result2 = main2()
    print(result2)
