# MEDIUM

from typing import List


def segments(message) -> List[str]:
    max_len = 155
    results = []
    tokens = message.split()
    cur_segment = []

    for idx in range(len(tokens)):
        cur_segment.append(tokens[idx])

        cur_str = "".join(cur_segment)
        if len(cur_str) == max_len:
            results.append(cur_str)

            if idx != len(tokens) - 1:
                cur_segment = [" "]
            else:
                cur_segment = []
        elif len(cur_str) > max_len:
            new_cur = []

            while len(cur_str) > max_len:
                new_cur.append(cur_segment.pop())
                cur_str = "".join(cur_segment)

            results.append(cur_str)
            cur_segment = new_cur

            if idx != len(tokens) - 1:
                cur_segment.append(" ")
        else:
            cur_segment.append(" ")

    if cur_segment:
        results.append("".join(cur_segment))

    results[-1] = results[-1].rstrip()

    total = len(results)
    if total > 1:
        for idx in range(len(results)):
            results[idx] += f"({idx+1}/{total})"

    return results


if __name__ == "__main__":
    print(
        segments(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id tristique quam, in ullamcorper metus. Duis lacinia dolor non quam porta, non turpis duis."
        )
    )
    print(
        segments(
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis partu sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore ver rup. Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, litot Europa."
        )
    )
    print(
        segments(
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus"
        )
    )
