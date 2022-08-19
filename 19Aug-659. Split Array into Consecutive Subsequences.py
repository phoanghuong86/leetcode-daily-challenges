class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        c, ending = Counter(nums), defaultdict(int)
        for num in nums:
            if not c[num]:
                continue
            c[num]-=1
            if ending[num-1]>0:
                ending[num]+=1
                ending[num-1]-=1
            else:
                if not c[num+1] or not c[num+2]:
                    return False
                c[num+1]-=1
                c[num+2]-=1
                ending[num+2]+=1
        return True
