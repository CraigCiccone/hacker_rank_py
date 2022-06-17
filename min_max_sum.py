# EASY


def miniMaxSum(arr):
    least = float("inf")
    most = 0

    for idx in range(len(arr)):
        tmp = arr.copy()
        tmp.pop(idx)
        amt = sum(tmp)
        least = min(least, amt)
        most = max(most, amt)

    print(f"{least} {most}")


if __name__ == "__main__":
    miniMaxSum([1, 3, 5, 7, 9])
    miniMaxSum([1, 2, 3, 4, 5])
