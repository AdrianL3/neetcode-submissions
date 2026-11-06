import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # first calculate euclidean distance
        distances = []
        for point in points:
            x1, x2 = point[0], point[1]

            distance = (x1**2 + x2**2)
            distances.append([distance, point])

        heapq.heapify(distances)
        res = []
        for i in range(k):
            res.append(heapq.heappop(distances)[1])

        return res