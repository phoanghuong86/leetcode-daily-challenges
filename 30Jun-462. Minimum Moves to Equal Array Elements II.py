#bruteforce soluiton
#O(n^2) passed 27/30 test cases
#we find ans for all possibilities and take min of them.
def minMoves2(self, nums: List[int]) -> int:
    n=len(nums)
    ans=float("inf")
    for i in range(n):
        moves=0
        for num in nums:
            moves+=abs(num-nums[i])     #gives TLE
        ans=min(ans,moves)
    return ans
    
#optimized soln
#we sort nums and find the median
#O(nlogn)
def minMoves2(self, nums: List[int]) -> int:
    nums.sort()
    ans=0
    median=nums[len(nums)//2]
    for num in nums:
        ans+=abs(median-num)
    return ans
