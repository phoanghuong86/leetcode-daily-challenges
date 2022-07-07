class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def check(c1, c2, c3):
            # print(c1, c2, c3)
            n1 = len(c1)
            n2 = len(c2)
            n3 = len(c3)
            if n1 == n2 == n3 == 0:
                return True
            if n1+n2 != n3:
                return False
            if n1 == 0:
                if c2 == c3:
                    return True
                return False
            if n2 == 0:
                if c1 == c3:
                    return True
                return False
            if c1[0] == c2[0] == c3[0]:
                return check(c1[1:], c2, c3[1:]) or check(c1, c2[1:], c3[1:])
            if c1[0] == c3[0]:
                return check(c1[1:], c2, c3[1:])
            if c2[0] == c3[0]:
                return check(c1, c2[1:], c3[1:])
            return False
        return check(s1, s2, s3)
