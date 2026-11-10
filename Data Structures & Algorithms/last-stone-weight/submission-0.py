class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if x == y:
                continue
            elif x < y:
                heapq.heappush(heap, -(y - x))
        
        if not heap:
            return 0
        else:
            return -heapq.heappop(heap)