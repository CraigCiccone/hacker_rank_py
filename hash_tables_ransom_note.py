# EASY


def checkMagazine(magazine, note):
    words = {}

    for word in magazine:
        words[word] = words.get(word, 0) + 1

    for word in note:
        if word in words and words[word] > 0:
            words[word] -= 1
            continue
        else:
            return "No"

    return "Yes"


if __name__ == "__main__":
    print(
        checkMagazine(
            ["give", "me", "one", "grand", "today", "night"],
            ["give", "one", "grand", "today"],
        )
    )
    print(
        checkMagazine(
            ["two", "times", "three", "is", "not", "four"],
            ["two", "times", "two", "is", "four"],
        )
    )
    print(
        checkMagazine(
            ["ive", "got", "a", "lovely", "bunch", "of", "coconuts"],
            ["ive", "got", "some", "coconuts"],
        )
    )
