class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(None)
        def dp(index,remainDays):
            if remainDays==0:
                if index==n:
                    return 0
                else:
                    return sys.maxsize
                
            if index==n:
                if remainDays==0:
                    return 0
                else:
                    return sys.maxsize
                
            ans=sys.maxsize
            curMax=0
            for i in range(index,n):
                curMax=max(curMax,jobDifficulty[i])
                ans=min(ans,curMax+dp(i+1,remainDays-1))
                
            return ans
        n=len(jobDifficulty)
        if n<d:
            return -1
        return dp(0,d)
