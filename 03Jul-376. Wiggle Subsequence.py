class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        on = [[nums[0]]] # longest subarray ends with nums[i] & positive
        off = [[nums[0]]] # longest subarray ends with nums[i] & negative
        
        res = 1 # record the subarray with the largest length
        
        for p in range(1, len(nums)):
            
            cur_on, cur_off = [nums[p]], [nums[p]]
            cur_on_len, cur_off_len = 1, 1
            
            q = p - 1
            while q > -1:
                
                if nums[q] < nums[p]:
                    # update cur_on
                    if 1 + len(off[q]) > cur_on_len:
                        cur_on = off[q] + [nums[p]]
                        cur_on_len = 1 + len(off[q])
                        
                elif nums[q] > nums[p]:
                    # update cur_off
                    if 1 + len(on[q]) > cur_off_len:
                        cur_off = on[q] + [nums[p]]
                        cur_off_len = 1 + len(on[q])             
                q -= 1
    
            on.append(cur_on)
            off.append(cur_off)
            res = max(res, len(cur_on), len(cur_off))
        
        return res
