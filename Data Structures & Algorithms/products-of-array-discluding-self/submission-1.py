class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            before = 1
            if nums[:i]:
                for y in range(i):
                    before *= nums[y]
            after = 1
            if nums[i + 1:]:
                for y in range(i + 1, len(nums)):
                    after *= nums[y]
            result.append(before * after)
        return result