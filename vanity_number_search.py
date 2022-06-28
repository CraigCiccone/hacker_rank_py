# MEDIUM


def vanity(codes, numbers):
    num_map = {
        "A": "2",
        "B": "2",
        "C": "2",
        "D": "3",
        "E": "3",
        "F": "3",
        "G": "4",
        "H": "4",
        "I": "4",
        "J": "5",
        "K": "5",
        "L": "5",
        "M": "6",
        "N": "6",
        "O": "6",
        "P": "7",
        "Q": "7",
        "R": "7",
        "S": "7",
        "T": "8",
        "U": "8",
        "V": "8",
        "W": "9",
        "X": "9",
        "Y": "9",
        "Z": "9",
    }

    num_codes = []
    for code in codes:
        cur = []
        for char in code:
            cur.append(num_map[char])
        num_codes.append("".join(cur))

    matched = set()
    for number in numbers:
        for code in num_codes:
            if code in number:
                matched.add(number)
                break

    matched = list(matched)
    matched.sort()
    return matched


if __name__ == "__main__":
    print(
        vanity(
            ["TWLO", "CODE", "HTCH"],
            [
                "+17474824380",
                "+14157088956",
                "+919810155555",
                "+15109926333",
                "+1415123456",
            ],
        )
    )
