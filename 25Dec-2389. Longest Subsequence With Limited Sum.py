class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # sort and sum up, prepare for binary search
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        a = [0] * len(queries)
        for i in range(len(a)):
            q = queries[i]
            l = 0
            r = len(nums) - 1
            while l + 1 < r:
                m = (l + r) // 2
                if nums[m] >= q:
                    r = m
                else:
                    l = m
            # special case if the first element is already greater than the query
            a[i] = 0 if nums[l] > q else (r if nums[r] <= q else l) + 1

        return a
