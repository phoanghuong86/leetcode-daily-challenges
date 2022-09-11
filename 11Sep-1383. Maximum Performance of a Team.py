import heapq

class Solution:
	def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
		M = 10 ** 9 + 7
		l = list()
		for i in range(n):
			l.append((-efficiency[i], speed[i]))
		l.sort()
		res = 0
		heap = []
		heap_sum = 0
		for i in range(n):
			val = (-l[i][0] * (l[i][1] + heap_sum))# % M
			heapq.heappush(heap, l[i][1])
			heap_sum += l[i][1]
			if len(heap) > k - 1:
				heap_sum -= heapq.heappop(heap)
			res = max(res, val)
		return res % M
