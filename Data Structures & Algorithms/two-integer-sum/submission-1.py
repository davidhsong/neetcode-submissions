class Solution:

    # input type: list, int
    # output type: list

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, v in enumerate(nums):
            comp = target - v
            if comp in dic.keys():
                return [dic.get(comp), i]
            dic[v] = i
                