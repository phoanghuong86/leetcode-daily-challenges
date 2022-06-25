class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt=0;n=len(nums)
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                if i==1 or nums[i]>=nums[i-2]:
                    nums[i-1]=nums[i]
                else:
                    nums[i]=nums[i-1]
                cnt+=1
        #print(nums)
        return True if cnt<=1 else False
