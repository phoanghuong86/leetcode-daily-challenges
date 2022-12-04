class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n=len(nums)
        sums1=sum(nums) # right sum
        sums2=0 # left sum
        min1,k=float('inf'),0  # initial values
        for x,y in enumerate(nums[:n-1]):  # not including last value because n-x-1 will be equal 0 and we can't divide
            if min1==0:
                return k
            sums2 +=y  # adding values to left and abstracting from right
            sums1 -=y
            min2=abs((sums2//(x+1))-(sums1//(n-x-1)))   
            if min2<min1:
                min1,k=min2,x  # if min2 is lower ,index will be equal 0
        if sum(nums)//n<min1:      # if mean is lower return last index
            return n-1
        return k
