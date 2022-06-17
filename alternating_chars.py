# EASY


def alternatingCharacters(s):
    deletions = 0

    for idx in range(len(s)):
        if idx + 1 != len(s) and s[idx] == s[idx + 1]:
            deletions += 1

    return deletions


if __name__ == "__main__":
    print(alternatingCharacters("AAAA"))
    print(alternatingCharacters("BBBBB"))
    print(alternatingCharacters("ABABABAB"))
    print(alternatingCharacters("BABABA"))
    print(alternatingCharacters("AAABBB"))
