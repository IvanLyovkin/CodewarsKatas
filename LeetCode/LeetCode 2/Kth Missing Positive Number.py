class Solution:
    def findKthPositive(self, a: List[int], k: int) -> int:
        s = set(a)
        count = 0
        for i in range(1, max(s)):
            if i not in s:
                count += 1
                if count == k:
                    return i
        return max(s) + k - count 