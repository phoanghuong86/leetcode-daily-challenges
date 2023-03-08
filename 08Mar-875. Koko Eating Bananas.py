class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(piles, H, K):
            hours = 0
            for x in piles:
                if x % K == 0:
                    hours += x // K
                else:
                    hours += x // K + 1
            return hours > H
        
        low, high = 1, max(piles)
        while low < high:
            mid = low + (high - low) // 2
            if eat(piles, h, mid):
                low = mid + 1
            else:
                high = mid
        return low
        
