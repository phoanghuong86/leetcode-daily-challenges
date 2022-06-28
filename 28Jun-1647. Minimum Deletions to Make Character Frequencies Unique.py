from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int: 
        freq = Counter(s)
        lst=set()
        for val in freq.values():
            if val not in lst:
                lst.add(val)
            else:
                while val in lst and val>0:
                    val-=1
                lst.add(val)
        return sum(freq.values())-sum(lst)
