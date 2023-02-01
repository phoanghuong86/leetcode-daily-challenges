class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        a = len(str1)
        b = len(str2)
        GCD = math.gcd(a,b)
        c = int(a/GCD)
        d = int(b/GCD)
        res = str1[:GCD]
        if res*c == str1 and res*d == str2: return res
        return ""
