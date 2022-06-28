# EASY


def minNum(samDaily, kellyDaily, difference):
    sam_count = difference
    kelly_count = 0
    days = 0

    if kellyDaily <= samDaily:
        return -1

    while kelly_count <= sam_count:
        days += 1
        kelly_count += kellyDaily
        sam_count += samDaily

    return days


if __name__ == "__main__":
    print(minNum(3, 5, 5))
    print(minNum(4, 5, 1))
