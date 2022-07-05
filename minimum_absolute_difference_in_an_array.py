# EASY


def minimumAbsoluteDifference(arr):
    min_abs_diff = float("inf")
    arr.sort()

    for i in range(len(arr)):
        if i + 1 != len(arr):
            min_abs_diff = min(min_abs_diff, abs(arr[i] - arr[i + 1]))

    return min_abs_diff


if __name__ == "__main__":
    print(minimumAbsoluteDifference([3, -7, 0]))
    print(minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))
    print(minimumAbsoluteDifference([1, -3, 71, 68, 17]))
