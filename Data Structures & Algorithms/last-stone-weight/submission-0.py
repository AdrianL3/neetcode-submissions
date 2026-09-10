class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        #make the nums in stones negative to properly allow use of maxHeap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) >= 2:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            if y != x:
                heapq.heappush(max_heap, -(y - x))
        
        if max_heap:
            return -max_heap[0]
        else:
            return 0