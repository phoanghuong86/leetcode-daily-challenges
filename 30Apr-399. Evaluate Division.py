class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # coefficient graph
        h=defaultdict(list)
        n = len(equations)
        # list of unique variables
        a = set()
        # create a graph of the values
        for i in range(n):
            upper = equations[i][0]
            lower = equations[i][1]
            val = values[i]
            h[upper].append((val,lower))
            h[lower].append((1/val,upper))
            a.add(upper)
            a.add(lower)
            
        # BFS traversal
        def BFS(up, low):
            q = deque([(1,up)])
            visited = {}
            while q:
                c,v = q.popleft()
                # check if we've reached the target variable
                if v==low:
                    return c
                visited[v] = True      
                # add any child variables that have not been visited to the queue
                for coeff, child in h[v]:
                    if child not in visited:
                        # because we are searching using the upper variable, we multiplicatively stack the coefficients
                        q.append((c*coeff,child))
            # this means a solution could not be found
            return -1
        
        result =[]
        for query in queries:
            qu =query[0]
            ql =query[1]
            # if a variable does not exist, then solution is not possible
            if qu not in a or ql not in a:
                result.append(-1)
            # if both variables are equal then solution is 1
            elif qu == ql:
                result.append(1)
            else:
                result.append(BFS(qu,ql))
        return result
