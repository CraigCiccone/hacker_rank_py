# EASY


def luckBalance(k, contests):
    contests.sort(key=lambda x: (x[1], -x[0]))
    luck = important_losses = 0

    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        elif important_losses < k:
            luck += contest[0]
            important_losses += 1
        else:
            luck -= contest[0]

    return luck


if __name__ == "__main__":
    print(luckBalance(2, [(5, 1), (1, 1), (4, 0)]))
    print(luckBalance(1, [(5, 1), (1, 1), (4, 0)]))
    print(luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))
