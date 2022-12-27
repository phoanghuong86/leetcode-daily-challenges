import itertools
import bisect

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diffs = sorted([capacity[i] - rocks[i] for i in range(len(rocks))])
        diffs = list(itertools.accumulate(diffs))
        return bisect.bisect_right(diffs, additionalRocks)
        
