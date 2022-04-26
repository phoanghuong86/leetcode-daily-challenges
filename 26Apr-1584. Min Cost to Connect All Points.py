class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = list(map(lambda l: tuple(l), points))
        unexplored = set(points)
        min_dist = 0
        pq = [(0, points[0])]
        while unexplored:
            dist, u = heapq.heappop(pq)
            if u not in unexplored:
                continue
            unexplored.remove(u)
            min_dist += dist
            for v in unexplored:
                heapq.heappush(pq, (abs(v[0] - u[0]) + abs(v[1] - u[1]), v))
        return min_dist
