class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs = 0
        complement = {}

        for n in nums:
            if n > k:
                continue
            com = k-n
            if complement.get(com, 0) > 0:
                complement[com] -= 1
                pairs +=1
            else:
                complement[n] = complement.get(n, 0) + 1

        return pairs
