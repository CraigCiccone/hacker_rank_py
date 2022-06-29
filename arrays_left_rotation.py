# EASY

from collections import deque


def rotLeft(a, d):
    dq = deque(a)
    dq.rotate(-d)
    return dq


# def rotLeft(a, d):
#     for _ in range(d):
#         val = a.pop(0)
#         a.append(val)
#     return a


if __name__ == "__main__":
    print(rotLeft([1, 2, 3, 4, 5], 4))
