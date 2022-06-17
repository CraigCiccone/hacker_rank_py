# EASY


def twoStrings(s1, s2):
    for char in [c for c in s1]:
        if char in s2:
            return "YES"
    return "NO"


if __name__ == "__main__":
    print(twoStrings("and", "art"))
    print(twoStrings("be", "cat"))
