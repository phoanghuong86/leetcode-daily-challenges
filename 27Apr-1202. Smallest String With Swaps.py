from collections import defaultdict
from typing import List


class UnionFind:

    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x) -> int:
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1


# Runtime: 721 ms, faster than 87.74% of Python3 online submissions for Smallest String With Swaps.
# Memory Usage: 50.4 MB, less than 69.64% of Python3 online submissions for Smallest String With Swaps.
class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        for x, y in pairs:
            uf.union(x, y)
        groups = defaultdict(lambda: [])
        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)
        res = [" "] * n
        for key in groups:
            indices = groups[key]
            temp = []
            for i in indices:
                temp.append(s[i])
            temp.sort()
            ni = len(indices)
            # key exchange step: exchange the temp group chars in the original index with sorted chars
            for i in range(ni):
                res[indices[i]] = temp[i]
        return "".join(res)
