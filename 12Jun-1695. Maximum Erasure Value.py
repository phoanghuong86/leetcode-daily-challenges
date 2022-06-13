class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = {nums[0]} # elem present in curent window
        total = nums[0]  # total of current window
        l = 0
        mx = 0
        for r in range(1, len(nums)):
            if nums[r] in seen:  # new window
                mx = max(mx, total)
                # Skip all elem before seen num in curr set
                while True:  
                    total -= nums[l]
                    seen.remove(nums[l])
                    if nums[l] == nums[r]:
                        l += 1
                        break
                    l += 1
            seen.add(nums[r])
            total += nums[r]
        
        mx = max(mx, total)
        
        return mx
                
