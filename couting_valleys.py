# EASY


def countingValleys(steps, path):
    valleys = 0
    height = 0

    for char in path:
        was_zero = height == 0

        if char == "D":
            height -= 1
        else:
            height += 1
        # match char:
        #     case 'D':
        #         height -= 1
        #     case 'U':
        #         height += 1

        if was_zero and height < 0:
            valleys += 1

    return valleys


if __name__ == "__main__":
    print(countingValleys(8, "UDDDUDUU"))
