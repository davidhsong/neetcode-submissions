class Solution:

    # input type: list, int
    # output type: list

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            comp = target - v
            if comp in seen:
                return [seen.get(comp), i]
            else:
                seen[v] = i