# EASY

def sockMerchant(n, ar):
    counts = {}

    for num in ar:
        counts[num] = counts.get(num, 0) + 1

    return sum([count // 2 for count in counts.values()])


if __name__ == "__main__":
    print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
