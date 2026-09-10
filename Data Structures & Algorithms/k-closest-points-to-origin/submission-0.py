class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #intiailze a maxheap that will keep track of the k closest elements
        #tuples of (distance, index)
        max_heap = [(float('-inf'), 0, 0)] * k
        heapq.heapify(max_heap)

        for x, y in points:
            distance = ((x**2) + (y**2))**0.5 * -1

            if distance > max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (distance, x, y))

        result = []
        for dist, x, y in max_heap:
            result.append([x, y])

        return result