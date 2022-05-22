class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = defaultdict(bool)
        def find(i,j):
            if i>j:
                return False
            
            if (i,j) not in dp:
                if j-i+1==1:
                    self.res += 1
                    dp[(i,j)] = True
                elif j-i+1==2:
                    if s[i] == s[j]:
                        self.res += 1
                        dp[(i,j)] = True
                    else:
                        dp[(i,j)] = False
            
                elif s[i] == s[j] and find(i+1,j-1):
                    dp[(i,j)] = True
                    self.res += 1
                else:
                    dp[(i,j)] = False
                find(i+1,j)
                find(i,j-1)
            return dp[(i,j)]
        
        self.res = 0
        find(0,len(s)-1)
        return self.res
