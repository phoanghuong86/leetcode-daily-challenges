class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cumulativeSum = 0
        cumulativeSumArr = []
        for num in nums:
            cumulativeSum += num
            cumulativeSumArr.append(cumulativeSum)
        return cumulativeSumArr
