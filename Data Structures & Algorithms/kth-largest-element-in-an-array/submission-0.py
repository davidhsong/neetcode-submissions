class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-1 * x for x in nums]
        heapq.heapify(heap)

        res = 0

        for i in range(k):
            res = heapq.heappop(heap)
        
        return -res
