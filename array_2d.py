# EASY


def hourglassSum(arr):
    sums = []

    for row in range(4):
        for col in range(1, 5):
            sums.append(
                arr[row][col - 1]
                + arr[row][col]
                + arr[row][col + 1]
                + arr[row + 1][col]
                + arr[row + 2][col - 1]
                + arr[row + 2][col]
                + arr[row + 2][col + 1]
            )

    return max(sums)


if __name__ == "__main__":
    print(
        hourglassSum(
            [
                [-9, -9, -9, 1, 1, 1],
                [0, -9, 0, 4, 3, 2],
                [-9, -9, -9, 1, 2, 3],
                [0, 0, 8, 6, 6, 0],
                [0, 0, 0, -2, 0, 0],
                [0, 0, 1, 2, 4, 0],
            ]
        )
    )
