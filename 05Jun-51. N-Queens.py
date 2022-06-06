class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.col = set()
        self.posdiag = set() #r-c
        self.negdiag = set() #r+c
        self.res = []
        self.board = [["."]*n for _ in range(n)]
        
        def backtrack(r):
            if r == n:
                self.res.append(["".join(row) for row in self.board])
                return
            
            for c in range(n):
                if c in self.col or r-c in self.posdiag or r+c in self.negdiag:
                    continue
                
                self.col.add(c)
                self.posdiag.add(r-c)
                self.negdiag.add(r+c)
                self.board[r][c] = "Q"
                
                backtrack(r+1)
                
                self.col.remove(c)
                self.posdiag.remove(r-c)
                self.negdiag.remove(r+c)
                self.board[r][c] = "."
        
        backtrack(0)
        return self.res
