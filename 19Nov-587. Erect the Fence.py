class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def slope(x1,x2,y1,y2):
            return (y2-y1)/(x2-x1)
        trees.sort()
        X={}
        for x,y in trees:
            if x in X:
                X[x].append(y)
            else:
                X[x]=[y]
        q=deque()
        q.append(tuple(trees[0]))
        while True:
            p=None
            m=None
            for i in range(q[-1][0]+1,101):
                if i in X:
                    if not p:
                        p=[i,X[i][0]]
                        m=slope(q[-1][0],i,q[-1][1],X[i][0])
                        continue
                    if slope(q[-1][0],i,q[-1][1],X[i][0])<m:
                        m=slope(q[-1][0],i,q[-1][1],X[i][0])
                        p=[i,X[i][0]]
            if not p:
                x=q[-1][0]
                y=q[-1][1]
                for i in X[x]:
                    if i!=y:
                        q.append((x,i))
                break
            if tuple(p)==q[0]:
                break
            q.append(tuple(p))


        while q[-1][0]!=q[0][0] or q[-1][1]!=q[0][1]:
            p=None
            m=None
            for i in range(q[-1][0]-1,-1,-1):
                if i in X:
                    if not p:
                        p=[i,X[i][-1]]
                        m=slope(q[-1][0],i,q[-1][1],X[i][-1])
                        continue
                    if slope(q[-1][0],i,q[-1][1],X[i][-1])<m:
                        m=slope(q[-1][0],i,q[-1][1],X[i][-1])
                        p=[i,X[i][-1]]
            if not p:
                x=q[-1][0]
                y=q[0][1]
                for i in X[x]:
                    if i!=y:
                        q.append((x,i))
                break
            if tuple(p)==q[0]:
                break
            q.append(tuple(p))

        return set(q)
        
