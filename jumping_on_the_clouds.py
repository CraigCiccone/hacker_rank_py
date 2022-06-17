# EASY


def jumpingOnClouds(c):
    path = [0]
    pos = 0

    for idx in range(0, len(c)):
        if idx < pos:
            continue
        elif pos == len(c) - 1:
            break

        if idx + 2 < len(c) and c[idx + 2] == 0:
            pos += 2
            path.append(pos)
        else:
            pos += 1
            path.append(pos)

    return len(path) - 1


if __name__ == "__main__":
    print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
    print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))
