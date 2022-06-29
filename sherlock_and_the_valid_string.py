# MEDIUM

from collections import defaultdict


def isValid(s):
    chars = [char for char in s]
    counts = defaultdict(int)

    for char in chars:
        counts[char] += 1

    values = list(counts.values())
    values.sort(reverse=True)

    if sum(values) == values[0] * len(values):
        return "YES"

    values[0] -= 1
    if sum(values) == values[0] * len(values):
        return "YES"

    values[0] += 1
    if values[-1] == 1 and values[0] * (len(values) - 1) == sum(values[:-1]):
        return "YES"

    return "NO"

    # values.sort(reverse=True)
    # desired1 = values[0] * len(values)
    # desired2 = (values[0]-1) * len(values)
    # sum_values1 = sum(values)
    #
    # print(values)
    # print("sum_values1", sum_values1)
    #
    # values[0] -= 1
    # sum_values2 = sum(values)
    #
    # print(counts)
    #
    # print("desired1", desired1)
    # print("desired2", desired2)
    # print(values)
    # print("sum_values1", sum_values1)
    # print("sum_values2", sum_values2)
    #
    # if desired1 == sum_values1 or desired2 == sum_values2:
    #     return "YES"
    #
    # return "NO"


if __name__ == "__main__":
    print(isValid("aabbcd"))  # NO
    print(isValid("aabbccddeefghi"))  # NO
    print(isValid("abcdefghhgfedecba"))  # YES
    print(isValid("aabbc"))  # YES
