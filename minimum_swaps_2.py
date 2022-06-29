# MEDIUM


def minimumSwaps(arr):
    swaps = 0

    for idx in range(len(arr)):
        while arr[idx] != idx + 1:
            tmp = arr[arr[idx] - 1]
            arr[arr[idx] - 1] = arr[idx]
            arr[idx] = tmp

            swaps += 1

    return swaps


if __name__ == "__main__":
    print(minimumSwaps([4, 3, 1, 2]))
    print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))
    print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))
