class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        
        m, n = len(multipliers), len(nums)
        previous_layer = [0] * (m+1)
        new_layer = [0] * (m+1)
        
        for k in range(1, m+1):
            c = multipliers[k-1]
            new_layer[0] = previous_layer[0] + c*nums[-k]
            new_layer[k] = previous_layer[k-1] + c*nums[k-1]
            
            for left in range(1, k):
                right = k - left                
                new_layer[left] = max(previous_layer[left] + c*nums[-right],
                                      previous_layer[left-1] + c*nums[left-1])
            previous_layer = new_layer
            new_layer = [0] * (m+1)
            
        return max(previous_layer)
