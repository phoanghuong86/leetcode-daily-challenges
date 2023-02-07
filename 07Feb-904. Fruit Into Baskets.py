from collections import Counter

MAX_BASKETS = 2


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        cnt = Counter()
        output, w_start = 0, 0

        for t in fruits:
            if cnt[t] == 0 and len(cnt) == MAX_BASKETS:
                while len(cnt) >= MAX_BASKETS:
                    cnt[x := fruits[w_start]] -= 1

                    if cnt[x] == 0:
                        cnt.pop(x)

                    w_start += 1

            cnt[t] += 1
            output = max(output, cnt.total())

        return output
