class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        @cache
        def hasApple(row, col, rowflag):
            if row>=m or col>=n:
                return False
            elif pizza[row][col]=='A':
                return True
            elif rowflag:
                return hasApple(row, col+1, rowflag)
            else:
                return hasApple(row+1, col, rowflag)
        
        @cache
        def count(top, left, k, cuttable, direction):
            if top==m or left==n:
                return 0
            elif k==1:
                return 1 if any(hasApple(row, left, True) for row in range(top, m)) else 0
            else:
                total = count(top, left, k-1, False, 0) if cuttable else 0
                if not direction or direction==1:
                    total+=count(top+1, left, k, cuttable or hasApple(top, left, True), 1)
                if not direction or direction==2:
                    total+=count(top, left+1, k, cuttable or hasApple(top, left, False), 2)
                return total%int(1e9+7)
        return count(0,0,k,False,0)
