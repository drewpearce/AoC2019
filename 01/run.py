import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

from helpers import load_inputs_lines  # noqa E402


def calculate_reqs(i):
    out = i // 3
    out = out - 2
    return out


def sum_reqs(i):
    return sum(i)


def main1(inputs):
    reqs = []
    for i in inputs:
        reqs.append(calculate_reqs(i))
    return sum_reqs(reqs)


def main2(inputs):
    reqs = []
    for i in inputs:
        req = i
        while req > 0:
            req = calculate_reqs(req)
            if req > 0:
                reqs.append(req)

    return sum_reqs(reqs)


if __name__ == "__main__":
    inputs = load_inputs_lines('01', 'inputs.txt', 'int')
    result = main1(inputs)
    result2 = main2(inputs)
    print(result)
    print(result2)
