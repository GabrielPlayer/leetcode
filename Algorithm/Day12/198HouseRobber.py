class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if (n == 0): return 0
        memo = [0 for i in range(n+1)]
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1,n):
            val = nums[i]
            memo[i+1] = max(memo[i], memo[i-1] + val)
        return memo[n]