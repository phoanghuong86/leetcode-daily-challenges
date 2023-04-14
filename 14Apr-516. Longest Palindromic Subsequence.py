class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self._longestPalindromeSubseq(s, 0, len(s) - 1, {})
    
    def _longestPalindromeSubseq(self, s, start, end, memo):
        key = (start, end)
        if key in memo:
            return memo[key]
        if start == end:
            return 1
        if start > end:
            return 0
        
        if s[start] == s[end]:
            memo[key] = self._longestPalindromeSubseq(s, start + 1, end - 1, memo) + 2
        else:
            memo[key] = max(
                self._longestPalindromeSubseq(s, start + 1, end, memo),
                self._longestPalindromeSubseq(s, start, end - 1, memo)
            )
        return memo[key]
