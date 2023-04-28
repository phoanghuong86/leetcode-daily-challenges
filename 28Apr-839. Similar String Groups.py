class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def find(parent, node):
            if parent[node] != node:
                parent[node] = find(parent, parent[node])
            return parent[node]
        
        def union(parent, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x != root_y:
                parent[root_x] = root_y

        def are_similar(s1, s2):
            if s1==s2:
                return True
            diff_count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff_count += 1
                if diff_count > 2:
                    return False
            return diff_count == 2

        n = len(strs)
        parent = list(range(n))

        for i in range(n):
            for j in range(i + 1, n):
                if are_similar(strs[i], strs[j]):
                    union(parent, i, j)

        groups = set()
        for i in range(n):
            groups.add(find(parent, i))
        return (len(groups))
