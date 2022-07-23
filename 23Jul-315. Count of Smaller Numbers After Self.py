from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        counts = []
        for n in reversed(nums):
            index = sl.bisect_left(n)
            counts.append(index)
            sl.add(n)
        counts.reverse()
        return counts
