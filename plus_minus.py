# EASY


def plusMinus(arr):
    size = len(arr)
    pos = 0
    neg = 0
    zero = 0

    for val in arr:
        if val > 0:
            pos += 1
        elif val < 0:
            neg += 1
        else:
            zero += 1

    if size > 0:
        print(f"{pos / size}\n{neg / size}\n{zero / size}")
    else:
        print("0\n0\n0")


if __name__ == "__main__":
    plusMinus([-4, 3, -9, 0, 4, 1])
    plusMinus([1])
    plusMinus([])
