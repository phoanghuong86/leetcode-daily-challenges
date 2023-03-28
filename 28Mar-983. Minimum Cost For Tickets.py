class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        len_day = len(days)

        @cache
        def helper(idx: int = 0) -> int:

            if idx >= len_day:
                return 0

            dict_idx = {}

            for n in range(idx + 1, len_day):

                if days[n] - days[idx] >= 7 and not dict_idx.get('idx_week'):
                      dict_idx['idx_week'] = n

                if days[n] - days[idx] >= 30 and not dict_idx.get('idx_month'):
                      dict_idx['idx_month'] = n
                      break
            
            if not dict_idx.get('idx_week'):
                dict_idx['idx_week'] = len_day
            
            if not dict_idx.get('idx_month'):
                dict_idx['idx_month'] = len_day
                

            return min(
                costs[0] + helper(idx + 1),
                costs[1] + helper(dict_idx['idx_week']),
                costs[2] + helper(dict_idx['idx_month']), 
            )

        return helper()
            
