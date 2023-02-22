class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def CalculateCapacity(capacity): 
            count = 1
            max = capacity
            for weight in weights:
                if weight > max:
                    max = capacity
                    count += 1
                max -= weight
            return True if count <= days else False

        start, end = max(weights), sum(weights)
        while start < end:
            mid = start + (end - start) // 2
            if CalculateCapacity(mid):
                end = mid
            else:
                start = mid + 1
        return start
