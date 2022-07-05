# MEDIUM

import math


def minTime(machines, goal):
    machines.sort()
    min_days = math.ceil(goal / len(machines)) * machines[0]
    max_days = math.ceil(goal / len(machines)) * machines[-1]

    while min_days < max_days:
        cur_days = min_days + (max_days - min_days) // 2
        day_sum = sum([cur_days // machine for machine in machines])

        if day_sum < goal:
            min_days = cur_days + 1
        elif day_sum >= goal:
            max_days = cur_days

    return min_days


if __name__ == "__main__":
    print(minTime([2, 3, 2], 10))
    print(minTime([2, 3], 5))
    print(minTime([1, 3, 4], 10))
    print(minTime([4, 5, 6], 12))
