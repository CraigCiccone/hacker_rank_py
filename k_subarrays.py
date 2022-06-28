# MEDIUM


def kSub(k, nums) -> int:
    count = 0
    cur_sum = 0
    prefixes = {}

    for idx in range(len(nums)):
        cur_sum += nums[idx]

        if cur_sum % k == 0:
            count += 1

        if cur_sum % k in prefixes:
            count += prefixes[cur_sum % k]

        prefixes[cur_sum % k] = prefixes.get(cur_sum % k, 0) + 1

    return count


if __name__ == "__main__":
    print(kSub(5, [5, 10, 11, 9, 5]))
    print(kSub(3, [1, 2, 3, 4, 1]))
