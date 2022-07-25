class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=nums[::-1]
        if target not in nums:
            return [-1,-1]
        return [nums.index(target),len(nums)-a.index(target)-1]
