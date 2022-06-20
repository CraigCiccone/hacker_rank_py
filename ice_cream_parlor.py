def whatFlavors(cost, money):
    compliments = {}

    for idx in range(len(cost)):
        compliment = money - cost[idx]

        if compliment in compliments:
            answer = [idx + 1, compliments[compliment] + 1]
            answer.sort()
            print(answer[0], answer[1])
            return
        compliments[cost[idx]] = idx


if __name__ == "__main__":
    whatFlavors([2, 1, 3, 5, 6], 5)
