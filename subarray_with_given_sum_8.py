# EASY


def countNumberOfSubarrays(arr, k):
    count = 0
    prefix_sum = {}
    cur_sum = 0

    for idx in range(len(arr)):
        cur_sum += arr[idx]

        if cur_sum == k:
            count += 1

        if cur_sum - k in prefix_sum:
            count += prefix_sum[cur_sum - k]

        prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1

    return count


if __name__ == "__main__":
    print(countNumberOfSubarrays([1, 2, 3, 0], 3))
    print(countNumberOfSubarrays([10, 2, -2, -20, 10], -10))
    print(countNumberOfSubarrays([1, 1, 1, 1], 2))
