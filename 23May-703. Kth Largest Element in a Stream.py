import heapq as hp
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.heap = []
        self.flag = True
        
    def add(self, val: int) -> int:
        if self.flag:
            for i in self.nums:
                hp.heappush(self.heap,i)
                if len(self.heap) > self.k:
                    hp.heappop(self.heap)
            self.flag = False
            
        hp.heappush(self.heap,val)
        if len(self.heap) > self.k:
            hp.heappop(self.heap)
        return self.heap[0]
