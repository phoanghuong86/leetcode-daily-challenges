class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #last test case
        if n==1 and trust==[]:
            return 1
        
        #all people who cant be the town judge
        #as they trust atleast one other person
        s = set()
        for t in trust:
            if t[0] not in s:
                s.add(t[0])
        
        
        #for all town judge candidates
        #create table entry
        table = {}
        for i in range(1,n+1):
            if i not in s:
                table[i] = 0
        
        #count number of people which trust the candidates
        #if n-1 people trust one candidate it is the town judge
        for t in trust:
            if t[1] in table:
                table[t[1]]+=1
                if table[t[1]] == n-1:
                    return t[1]
        return -1
