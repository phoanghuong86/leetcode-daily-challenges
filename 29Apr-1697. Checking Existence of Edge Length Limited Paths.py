class Solution:
    def distanceLimitedPathsExist(self, n: int, S: List[List[int]], Q: List[List[int]]) -> List[bool]:
        def Search(i):
            if i != root[i]:
                root[i] = Search(root[i])
            return root[i]

        def union(x, y):
            x, y = Search(x), Search(y)
            if x == y: return 0
            root[x] = y
            return 1

        root = list(range(n))
        ans = [False]*len(Q)
        i = 0
        S.sort(key=lambda x: x[2])
        q = [x[2] for x in Q]
        value= sorted(range(len(q)), key=q.__getitem__)
        for val in value:
            while i<len(S) and S[i][2]<Q[val][2]:
                x, y = S[i][0], S[i][1]
                i += 1
                union(x, y)
            if Search(Q[val][0]) == Search(Q[val][1]):
                ans[val] = True
        return ans  
