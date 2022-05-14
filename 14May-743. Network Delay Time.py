class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        
        for u,v,w in times:
            edges[u].append((v,w))
            
        m_heap = [(0,k)]
        
        visited = set()
        t = 0
        while m_heap:
            w1,n1 = heapq.heappop(m_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t,w1)
            
            for n2,w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(m_heap,(w1+w2,n2))
                    
        return t if len(visited) == n else -1
