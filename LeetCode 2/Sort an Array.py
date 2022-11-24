class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        arr = nums[0]
        left = list(filter(lambda x: x < arr, nums))
        mid = [item for item in nums if item == arr]
        right = list(filter(lambda x: x > arr, nums))

        return self.sortArray(left) + mid + self.sortArray(right)