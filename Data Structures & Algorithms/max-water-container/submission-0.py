class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxVol = 0
        while l < r:
            curVol = (r - l) * min(heights[l], heights[r])
            maxVol = max(curVol, maxVol)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1
                r -= 1
        return maxVol
