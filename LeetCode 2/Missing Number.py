class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        return (1 + l) * l // 2 - sum(nums)