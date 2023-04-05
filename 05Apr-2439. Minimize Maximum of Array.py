class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_avg_no, total = 0, 0
        for i in range(0,len(nums)):
            total+=nums[i]
            max_avg_no = max(max_avg_no,ceil(total/(i+1))) 
        return max_avg_no
