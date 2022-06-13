class Solution:

    def minOperations(self, nums: List[int], x: int) -> int:
        
        N = len(nums)
        total_sum = sum(nums)
        
        if total_sum == x: return N
        if total_sum < x: return -1
        
        max_subarray_size = -1
        target_sum = total_sum - x
        curr_sum = low = high = 0
        
        for high in range(N):
            curr_sum += nums[high]
            
            while curr_sum > target_sum:
                curr_sum -= nums[low]
                low += 1
            
            if curr_sum == target_sum:
                curr_subarray_size = high - low + 1
                max_subarray_size = max(max_subarray_size, curr_subarray_size)
        
        return N - max_subarray_size if max_subarray_size > -1 else -1
