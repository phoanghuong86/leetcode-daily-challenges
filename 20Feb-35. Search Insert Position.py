class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for x,i in enumerate(nums):
            if i >= target:
                return x
        return len(nums)
