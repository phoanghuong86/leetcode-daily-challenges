class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        return sum((l := len(list(g))) * (l + 1) // 2 for k, g in groupby(nums) if k == 0)
