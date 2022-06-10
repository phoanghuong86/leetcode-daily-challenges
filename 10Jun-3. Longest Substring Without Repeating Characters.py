class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = count = 0
        positions = {}
        for i, char in enumerate(s):
            if char in positions and positions[char] >= start:
                start = positions[char] + 1
            positions[char] = i
            count = max(count, i - start + 1) 
        return count             
