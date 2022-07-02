class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 10**9 + 7
        verticalCuts.sort()
        horizontalCuts.sort()
        
        v_max = verticalCuts[0]
        for i in range(1, len(verticalCuts)):
            v_max = max(v_max, verticalCuts[i] - verticalCuts[i-1])
        v_max = max(v_max, w - verticalCuts[-1])

        
        h_max = horizontalCuts[0]
        for j in range(1, len(horizontalCuts)):
            h_max = max(h_max, horizontalCuts[j]-horizontalCuts[j-1])
        h_max = max(h_max, h - horizontalCuts[-1])

            
        return (h_max*v_max)%mod
