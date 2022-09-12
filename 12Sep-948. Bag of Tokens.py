class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # two pointers & greedy
        # 1. sort tokens (ascending order)
        # 2. if power >= tokens[left], then face it up, score + 1
        # 3. if power < tokens[left], we can't earn point by face up tokens[left], then there are two situations:
             # (1) score > 0, we can face down tokens[right] to earn power
             # (2) score <= 0, just return the max_score
        # Note: we need to keep updating the max_score
        
        tokens.sort()
        left = 0
        right = len(tokens) -1
        score = 0
        max_score = 0
        
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                return max_score
        
        return max_score
