class Solution:
 #two pass solution
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)
        for i in range(len(candies)-1):
            if ratings[i] < ratings[i+1]:
                candies[i+1] = candies[i]+1
        for i in range(len(candies)-1,0,-1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i-1],candies[i]+1)
        return sum(candies)
