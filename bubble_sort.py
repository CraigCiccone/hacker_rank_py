# EASY

from typing import List


def countSwaps(a: List[int]) -> int:
    swaps = 0

    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j + 1] < a[j]:
                swaps += 1
                a[j], a[j + 1] = a[j + 1], a[j]

    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


def bubble_sort_better(a: List[int]) -> List[int]:
    swaps = 0

    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - i - 1):
            if a[j + 1] < a[j]:
                swaps += 1
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        if not swapped:
            break

    return a, swaps


if __name__ == "__main__":
    countSwaps([6, 4, 1])
    countSwaps([1, 2, 3])
    countSwaps([19, 1, 4, 7, 9, 0, -2, 3, 6, 16])
    print(bubble_sort_better([6, 4, 1]))
    print(bubble_sort_better([1, 2, 3]))
    print(bubble_sort_better([19, 1, 4, 7, 9, 0, -2, 3, 6, 16]))
