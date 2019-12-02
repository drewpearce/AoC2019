import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

from helpers import load_inputs_lines  # noqa E402


def main1(inputs):
    i = 0
    while True:
        op_code = inputs[i]

        if op_code == 99:
            break

        pos1 = inputs[i + 1]
        pos2 = inputs[i + 2]
        pos3 = inputs[i + 3]
        val1 = inputs[pos1]
        val2 = inputs[pos2]

        if op_code == 1:
            result = val1 + val2
        elif op_code == 2:
            result = val1 * val2
        else:
            msg = f'Invalid op code {op_code} at position {i}.\n\n{inputs}'
            raise Exception(msg)

        inputs[pos3] = result
        i += 4
    
    return inputs


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
