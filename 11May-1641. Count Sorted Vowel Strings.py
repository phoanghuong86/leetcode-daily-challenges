class Solution:
    def countVowelStrings(self, n: int) -> int:
        return ((n + 1)*(n + 1)*(n + 2)*(2*n + 3) // 6 +
                (n + 1)*(n + 1)*(n + 2) // 2 -
                (n + 1)*(n + 1)*(n + 2)*(n + 2) // 4 +
                (n + 1)*(n + 2) // 2) // 2
