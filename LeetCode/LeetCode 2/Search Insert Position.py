class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums==[]:
            return 0
        l = len(nums)
        i = 0
        j = l-1
        if target > nums[j]:
            return l
        elif target<nums[i]:
            return 0
        while (i<=j):
    
            mid = i + ((j-i)//2)        
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                j=mid-1
            elif target > nums[mid]:
                i=mid+1
        return i