class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # O(1) lookup
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

# Overall Complexity:
#   Time: O(n)
#   Space: O(n)