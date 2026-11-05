class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k

        for num in nums:
            if len(self.minHeap) < k:
                heapq.heappush(self.minHeap, num)
            else:
                if self.minHeap[0] < num:
                    heapq.heappop(self.minHeap)
                    heapq.heappush(self.minHeap, num)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
