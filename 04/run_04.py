import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

from helpers import load_inputs_lines  # noqa E402
from helpers import Timer  # noqa E402


def has_double(digits):
    collect = []
    for i, d in enumerate(digits):
        if i == 0:
            collect.append([d])
        else:
            if d in collect[-1]:
                collect[-1].append(d)
            else:
                collect.append([d])

    return any(len(c) > 1 for c in collect)


def has_isolated_double(digits):
    collect = []
    for i, d in enumerate(digits):
        if i == 0:
            collect.append([d])
        else:
            if d in collect[-1]:
                collect[-1].append(d)
            else:
                collect.append([d])

    return any(len(c) == 2 for c in collect)


def next_up(digits):
    for i in range(1, len(digits)):
        if int(digits[i]) < int(digits[i - 1]):
            digits = ''.join([
                d if i > en else digits[i - 1]
                for en, d in enumerate(digits)
            ])

    while not has_double(digits):
        digits = str(int(digits) + 1)

    return digits


def main1(data):
    points = data.split('-')
    matches = []
    matches.append(next_up(points[0]))
    cap = int(points[1])

    while True:
        val = next_up(str(int(matches[-1]) + 1))
        if int(val) <= cap:
            matches.append(val)
        else:
            break

    return matches


def main2(matches):
    return [m for m in matches if has_isolated_double(m)]


if __name__ == "__main__":
    timer = Timer()
    result1 = main1('245318-765747')
    timer.stop()
    print(len(result1))
    print(f'{timer.duration} ms')

    timer.start()
    result2 = main2(result1)
    timer.stop()
    print(len(result2))
    print(f'{timer.duration} ms')
