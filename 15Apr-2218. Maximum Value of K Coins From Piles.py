class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # dp array to memorize the already calculated results
        self.dp = collections.defaultdict(lambda: None)
        
        # compute the prefix sum of each pile so that we can easily get the value from a pile selecting k coins
        self.piles = piles
        self.num_piles = len(piles)
        self.piles_pfval = []
        for i in range(self.num_piles):
            pfval = [0]
            rval = 0
            for val in piles[i]:
                rval += val
                pfval.append(rval)
            self.piles_pfval.append(pfval)
            self.dp[i, 0] = 0
        
        # initialize the dp array for the boundary condition
        for i in range(1, k + 1):
            if i <= len(piles[-1]):
                self.dp[self.num_piles - 1, i] = self.piles_pfval[self.num_piles - 1][i]
            else:
                self.dp[self.num_piles - 1, i] = 0
            
        return self.pickCoins(0, k)
    
    # the pickCoins returns the maximum value that we select k coins and start at pile pidx 
    def pickCoins(self, pidx, k):
        if self.dp[pidx, k] is None:
            mval = 0
            for j in range(k + 1):
                if j > len(self.piles[pidx]):
                    break
                tval = self.pickCoins(pidx + 1, k - j) + self.piles_pfval[pidx][j]
                mval = max(mval, tval)
            self.dp[pidx, k] = mval
        return self.dp[pidx, k]
