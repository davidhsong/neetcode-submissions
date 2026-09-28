class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        
        for i, v in enumerate(nums):
            if v == target:
                return i