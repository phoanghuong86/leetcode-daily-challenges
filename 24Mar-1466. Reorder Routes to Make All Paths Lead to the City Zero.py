class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        maps = defaultdict(list)
        for a, b in connections:
            maps[a].append((b, 1))
            maps[b].append((a, 0))

        queue = [0]
        visited = set([0])
        res = 0
        while queue:
            nextQueue = []
            for node in queue:
                for neighbor, direction in maps[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        res += direction
                        nextQueue.append(neighbor)
            queue = nextQueue

        return res
