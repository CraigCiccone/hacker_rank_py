# MEDIUM


from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} {self.score}"

    @staticmethod
    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        else:
            if a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
            else:
                return 0


if __name__ == "__main__":
    n = 3
    data = [
        ("amy", 100),
        ("david", 100),
        ("heraldo", 50),
        ("aakansha", 75),
        ("aleksa", 150),
    ]

    players = []
    for d in data:
        n, s = d
        player = Player(n, s)
        players.append(player)

    sorted_players = sorted(players, key=cmp_to_key(Player.comparator))

    for p in sorted_players:
        print(p.name, p.score)
