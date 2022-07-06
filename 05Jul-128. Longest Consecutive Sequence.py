class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        else:    
            nums = list(set(nums))
            nums.sort()
            size= len(nums)
            max_count = 1
            count = 1
            for i in range(size-1):
                if nums[i+1]==nums[i]+1:
                    count +=1
                else:
                    count = 1
                    i += 1
                max_count = max(count, max_count)
            return max_count
