import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

from helpers import load_inputs_lines  # noqa E402
from helpers import Timer  # noqa E402


def get_movement(m):
    if not m:
        return (0, 0)

    dir = m[0]
    mag = int(m[1:])

    if dir == 'U':
        return (1, mag)
    elif dir == 'D':
        return (1, -mag)
    elif dir == 'L':
        return (0, -mag)
    elif dir == 'R':
        return (0, mag)


def get_next(last, m):
    if m[0] == 0:
        return (last[0] + m[1], last[1])
    elif m[0] == 1:
        return (last[0], last[1] + m[1])


def find_intersections(a, b):
    intersections = []

    for ai, av in enumerate(a):
        if ai == len(a) - 1:
            break

        av2 = a[ai + 1]

        for i, bv in enumerate(b):
            if i == len(b) - 1:
                break

            bv2 = b[i + 1]

            axmax = max(av[0], av2[0])
            aymax = max(av[1], av2[1])
            axmin = min(av[0], av2[0])
            aymin = min(av[1], av2[1])

            bxmax = max(bv[0], bv2[0])
            bymax = max(bv[1], bv2[1])
            bxmin = min(bv[0], bv2[0])
            bymin = min(bv[1], bv2[1])

            if bv[0] <= axmax and bv[0] >= axmin:
                if av[1] <= bymax and av[1] >= bymin:
                    intersections.append((bv[0], av[1], {
                        'd': abs(bv[0]) + abs(av[1]),
                        'ai': ai,
                        'bi': i,
                        'ad': abs(bv[0] - av[0]),
                        'bd': abs(av[1] - bv[1])
                    }))

            if av[0] <= bxmax and av[0] >= bxmin:
                if bv[1] <= aymax and bv[1] >= aymin:
                    intersections.append((av[0], bv[1], {
                        'd': abs(av[0]) + abs(bv[1]),
                        'ai': ai,
                        'bi': i,
                        'ad': abs(av[0] - bv[0]),
                        'bd': abs(bv[1] - av[1])
                    }))

    return intersections


def get_total_steps(data, point):
    total = 0
    ai = 0
    while ai <= point[2]['ai']:
        amt = abs(get_movement(data[0][ai])[1])
        total += amt
        ai += 1

    total += abs(point[2]['ad'])

    bi = 0
    while bi <= point[2]['bi']:
        amt = abs(get_movement(data[1][bi])[1])
        total += amt
        bi += 1

    return total + abs(point[2]['bd'])


def get_points(data):
    length = max(len(data[0]), len(data[1]))

    i = 0
    a = [(0, 0)]
    b = [(0, 0)]

    for i in range(length):
        if i < len(data[0]):
            i1 = get_movement(data[0][i])
        else:
            i1 = get_movement(None)

        if i < len(data[1]):
            i2 = get_movement(data[1][i])
        else:
            i2 = get_movement(None)

        a.append(get_next(a[-1], i1))
        b.append(get_next(b[-1], i2))

    return a[1:], b[1:]


def main1(data=None):
    if not data:
        data = load_inputs_lines('03', 'inputs.txt')

    data = [d.split(',') for d in data]
    a, b = get_points(data)
    intersections = find_intersections(a, b)
    return min([i[2]['d'] for i in intersections])


def main2(data=None):
    if not data:
        data = load_inputs_lines('03', 'inputs.txt')

    data = [d.split(',') for d in data]
    a, b = get_points(data)
    intersections = find_intersections(a, b)
    steps = [get_total_steps(data, i) for i in intersections]

    return min(steps)


if __name__ == "__main__":
    timer = Timer()
    result1 = main1()
    timer.stop()
    print(result1)
    print(timer.duration)

    timer.start()
    result2 = main2()
    timer.stop()
    print(result2)
    print(timer.duration)
