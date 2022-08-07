class Solution:
    followers = {
        "a": ["e"],
        "e": ["a", "i"],
        "i": ["a", "e", "o", "u"],
        "o": ["i", "u"],
        "u": ["a"],
        "st": ["a", "e", "i", "o", "u"]
    }
    def countVowelPermutation(self, n: int) -> int:
        dp = {}  # for caching data of the dfs fuction
        mod = 10**9 + 7
        def dfs(currChar, n): 
            if n == 1: return len(self.followers[currChar]) #exit condition - 1 
            if (currChar, n) in dp: return dp[(currChar, n)] #exit condition - 2(already visited this node)
            ret = 0
            for x in self.followers[currChar]: 
                ret += dfs(x, n-1) #traverse througn the children and add to the answer
            #print(currChar, ret)
            ret%=mod
            dp[(currChar, n)] = ret
            return ret
        
        return dfs("st", n)
