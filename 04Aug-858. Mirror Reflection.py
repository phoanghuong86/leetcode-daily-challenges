class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p = p // 2
            q = q // 2

        if q % 2 == 0 and p % 2 == 1:
            return 0
        elif q % 2 == 1 and p % 2 == 1:
            return 1
        elif q % 2 == 1 and p % 2 == 0:
            return 2
        else:
            return -1
