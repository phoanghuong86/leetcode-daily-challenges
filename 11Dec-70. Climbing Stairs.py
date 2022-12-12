class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1,2]
        if n < 2:
            return steps[n-1]
        for i in range(2,n):
            s = sum(steps)
            steps[0] = steps[1]
            steps[1] = s
        return steps[1]
