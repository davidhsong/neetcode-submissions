class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        checked = {}
        for i, v in enumerate(numbers):
            comp = target - v
            if comp in checked.keys():
                return [checked.get(comp) + 1, i + 1]
            checked[v] = i
        

