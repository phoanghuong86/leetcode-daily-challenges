class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            x = -i
            bottom, to_mod = triangle[x], triangle[x-1]
            for i in range(len(to_mod)):
                to_mod[i] += min(bottom[i], bottom[i+1])
        return triangle[0][0]
