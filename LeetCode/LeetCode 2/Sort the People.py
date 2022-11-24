class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:    
        res = []
        sort_heights = sorted(heights, reverse = True)
        for item in sort_heights:
            index = heights.index(item)
            res.append(names[index])
        return res