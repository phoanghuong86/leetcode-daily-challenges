class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for w in words:
            p = trie
            for c in w:
                if c not in p:
                    p[c] = {}
                p = p[c]
            p["#"] = w
        
        ret = list()
        def dfs(p, i, j, visited):
            if "#" in p:
                ret.append(p["#"])
                del p["#"]
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            
            for dx, dy in directions:
                new_x = i + dx
                new_y = j + dy
                
                if  (new_x, new_y) not in visited and 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] in p:
                    if len(p[board[new_x][new_y]]) == 0:
                        del p[board[new_x][new_y]]
                        continue
                    visited.add((new_x, new_y))
                    dfs(p[board[new_x][new_y]], new_x, new_y, visited)
                    visited.remove((new_x, new_y))
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    dfs(trie[board[i][j]], i, j, {(i,j)})
                    
        return list(ret)
