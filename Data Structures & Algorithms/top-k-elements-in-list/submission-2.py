from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) # -> counts = {1:1, 2:2, 3:3} <- { num : count }
        sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_counts.keys())[:k]



# Complexity: 
# 
# Time: O()
# 
# Space: O()
# 