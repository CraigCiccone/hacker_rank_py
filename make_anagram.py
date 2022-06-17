# EASY

def makeAnagram(a, b):
    removals = 0
    chars_a = {}
    chars_b = {}

    for char in a:
        chars_a[char] = chars_a.get(char, 0) + 1

    for char in b:
        chars_b[char] = chars_b.get(char, 0) + 1

    keys_a = []
    for key, val in chars_a.items():
        if key not in chars_b:
            keys_a.append(key)
            removals += val
        else:
            removals += abs(chars_b[key] - val)

    for key in keys_a:
        chars_a.pop(key)

    keys_b = []
    for key, val in chars_b.items():
        if key not in chars_a:
            removals += val
            keys_b.append(key)

    return removals


if __name__ == '__main__':
    print(makeAnagram("cde", "dcf"))
    print(makeAnagram("cde", "abc"))
    print(makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"))
