# EASY


def maximumToys(prices, k):
    prices.sort()
    bought = 0

    for price in prices:
        if price > k:
            break
        else:
            bought += 1
            k -= price

    return bought


if __name__ == "__main__":
    print(maximumToys([1, 2, 3, 4], 7))
    print(
        maximumToys(
            [
                1,
                12,
                5,
                111,
                200,
                1000,
                10,
            ],
            7,
        )
    )
