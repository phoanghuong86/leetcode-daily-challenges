class Solution:
    def partitionString(self, s: str) -> int:
        count, i = 1, 0
        char_set = set()
        while i < len(s):
            if s[i] in char_set:
                count += 1
                char_set = {s[i],}
            else:
                char_set.add(s[i])
            i += 1
        return count
