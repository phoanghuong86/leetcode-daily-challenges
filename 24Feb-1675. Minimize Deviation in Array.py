class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        n = len(nums)
        pq = []
        min_val = nums[0]*2

        for num in nums:
            if num % 2 != 0:
                num *= 2
            heapq.heappush(pq, -num)
            min_val = min(num, min_val)

        ans = -pq[0] - min_val
        while pq[0] % 2 == 0:
            top = -heapq.heappop(pq)
            heapq.heappush(pq, -(top // 2))
            ans = min(ans, top - min_val)
            min_val = min(min_val, top // 2)

        return min(ans, -pq[0] - min_val)
