def rob(nums):
    # edge cases:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    # dynamic programming - decide each problem by its sub-problems:
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    print(dp)
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        print(dp)
    return dp[-1]


nums = [2, 7, 9, 3, 1]
print(rob(nums))
