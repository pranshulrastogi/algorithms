def rob(nums) -> int:
    n = len(nums)
    dp = [0 for i in range(n)]
    dp_2 = [0 for i in range(n)]

    if n <= 3:
        return max(nums)
    dp[0] = nums[0]
    dp[1] = nums[1]
    dp_2[0] = -1
    dp_2[1] = nums[1]
    dp_2[2] = nums[2]
    for i in range(2, n - 1):
        dp[i] = max(dp[: i - 1]) + nums[i]

    # case where last element inclusion might create maximum
    for i in range(3, n):
        dp_2[i] = max(dp_2[: i - 1]) + nums[i]

    ans = max(dp)

    ans2 = max(dp_2)

    ans = max(ans, ans2)
    print(ans)
    return ans
