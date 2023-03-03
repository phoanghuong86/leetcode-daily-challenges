class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        indexOut = None
        if needle is None:
            return 0
        if needle in haystack:
            # check index
            p1, p2 = 0, 0
            while p1 < len(haystack) and p2 <= len(needle) - 1:
                if haystack[p1] == needle[p2]:
                    if indexOut is None:
                        indexOut = p1
                    p2 += 1
                else:
                    p1 = indexOut if indexOut is not None else p1
                    p2 = 0
                    indexOut = None
                p1 += 1

            return indexOut

        return -1
