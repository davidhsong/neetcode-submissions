class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []

        for point in points:
            point.append(math.sqrt((point[0] ** 2) + (point[1] ** 2)))

        heap = [(point[2], point) for point in points]
        heapq.heapify(heap)
        #print(heap)

        for i in range(k):
            result.append(heapq.heappop(heap)[1][:2])

        return result