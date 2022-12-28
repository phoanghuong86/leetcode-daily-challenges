import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []
        for stones in piles:
            heapq.heappush(max_heap, -stones)
        
        while k:
            greatest = heapq.heappop(max_heap)
            heapq.heappush(max_heap, greatest // 2)
            k -= 1
        
        return -sum(max_heap)
