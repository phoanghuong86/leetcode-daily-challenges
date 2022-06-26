class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = len(cardPoints)
        window_size = l - k
        all_sum = cur_win_sum = win_sum = sum(cardPoints[:window_size])``
        for idx in range(window_size, l):
            cur_win_sum += - cardPoints[idx - window_size] + cardPoints[idx]
            all_sum += cardPoints[idx]
            win_sum = min(cur_win_sum, win_sum)
        return all_sum - win_sum
