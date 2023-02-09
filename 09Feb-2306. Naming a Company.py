class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ls = [set() for _ in range(26)]
        for idea in ideas: 
            init = idea[0]
            rest = idea[1:]
            ls[ord(init) - 97].add(rest)
        res = 0
        for i in range(25): 
            st1 = ls[i]
            len1 = len(st1)
            if not len1: 
                continue
            for j in range(i + 1, 26): 
                st2 = ls[j]
                len2 = len(st2)
                if not len2: 
                    continue
                len_int = len(st1.intersection(st2))
                res += 2 * (len1 - len_int) * (len2 - len_int)
        return res

