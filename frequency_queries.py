# MEDIUM

from collections import defaultdict


def freqQuery(queries):
    d_totals = defaultdict(int)
    d_freq = defaultdict(int)
    results = []

    for q in queries:
        action = q[0]
        val = q[1]

        if action == 1:
            if d_totals[val] in d_freq:
                d_freq[d_totals[val]] -= 1
                if d_freq[d_totals[val]] == 0:
                    del d_freq[d_totals[val]]
            d_totals[val] += 1
            d_freq[d_totals[val]] += 1
        elif action == 2:
            if d_totals[val] > 0:
                d_freq[d_totals[val]] -= 1
                if d_freq[d_totals[val]] == 0:
                    del d_freq[d_totals[val]]
                d_totals[val] -= 1
                if d_totals[val] != 0:
                    d_freq[d_totals[val]] += 1
        elif action == 3:
            if val in d_freq:
                results.append(1)
            else:
                results.append(0)

    return results


if __name__ == "__main__":
    print(freqQuery([(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]))
