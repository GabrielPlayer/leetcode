class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for _ in range(k):
            nums.insert(0,nums[n-1])
            del nums[n]