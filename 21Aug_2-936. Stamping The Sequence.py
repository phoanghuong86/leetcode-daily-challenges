class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        tLen = len(target)
        sLen = len(stamp)
        
        T = '?'*tLen
        res = []
        
        turns = 10*tLen
        prevTarget = 'A'
        
        while prevTarget != target and target != T and turns > 0:
            turns -= 1
            prevTarget = target
            
            i = 0
            while i < tLen:
                
                j = 0
                qCount = 0
                while i+j < tLen and j < sLen and (target[i+j] == '?' or target[i+j] == stamp[j]):
                    qCount = qCount + (1 if target[i+j] == '?' else 0)
                    j += 1
                
                if j == sLen and qCount != sLen:
                    target = target[:i] + '?'*sLen + target[i+sLen:]
                    res.append(i)
                    break
                else:
                    i += 1
        
        return res[::-1] if prevTarget != target and turns > 0 else []
