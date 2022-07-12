class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        count = sum(matchsticks)
        if count % 4 != 0:
            return 0
        matchsticks.sort(reverse=True)
        sub_sum = count//4
        seen = {}
        return self.backtrack(matchsticks, 0, [0,0,0,0], sub_sum, seen)
    
    def backtrack(self, matchsticks, i, curr, sub_sum, seen):
        if i == len(matchsticks):
            return len(set(curr)) == 1
        tp = tuple(curr)
        if tp not in seen:
            length = matchsticks[i]
            for g in range(4):
                if curr[g] + length <= sub_sum:
                    curr[g] += length
                    if self.backtrack(matchsticks, i+1, curr, sub_sum, seen):
                        seen[tp] = True
                        return True
                    curr[g] -= length
            seen[tp] = False
        return seen[tp]
            
