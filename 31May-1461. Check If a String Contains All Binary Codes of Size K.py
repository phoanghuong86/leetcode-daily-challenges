class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()
        n = len(s)
        for i in range(n-k+1):
            st.add(s[i:i+k]) # Add every substring into set
            if len(st) == 2**k: return True
        return False
