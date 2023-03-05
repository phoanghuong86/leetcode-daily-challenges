class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        graph = defaultdict(list)
        for i in range(n):
            graph[arr[i]].append(i)
        print(graph)
        que = deque([0])
        result = 0
        visited = set()
        while que:
            q_len = len(que)
            for _ in range(q_len):
                cur = que.popleft()
                if cur == n - 1:
                    return result
                if cur in visited:
                    continue
                visited.add(cur)
                # case: arr[i] == arr[j]
                for child in graph[arr[cur]]:
                    que.append(child)                
                # clear the graph node, to avoid the redundent search. 
                graph[arr[cur]].clear()

                # case: i + 1
                if cur < n - 1:
                    que.append(cur + 1)
                # case: i - 1
                if cur > 0:
                    que.append(cur - 1)


            result += 1

        return result
