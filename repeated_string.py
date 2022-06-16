# EASY

def repeatedString(s, n):
    s_size = len(s)
    num_in_s = sum([1 for char in s if char == 'a'])
    repeats = n // s_size
    mod = n % s_size

    if mod == 0:
        return num_in_s * repeats
    else:
        return num_in_s * repeats + sum([1 for char in s[:mod] if char == 'a'])


if __name__ == "__main__":
    print(repeatedString("aba", 10))
    print(repeatedString("a", 1000000000000))
