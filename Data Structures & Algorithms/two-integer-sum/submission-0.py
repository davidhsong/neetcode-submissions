class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i, v in enumerate(nums):
            comp = target - v
            if comp in checked.keys():
                return [checked.get(comp), i]
            checked[v] = i