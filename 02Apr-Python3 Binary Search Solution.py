class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # spells[i] * potions[j] >= success
        # spells[i] >= success/potions[j]
        # define list x as success/potions[j]
        # sort x and binary search x with each spell could work well

        x = sorted([success/potion for potion in potions])
        pairs = []
        for spell in spells:
            pos = bisect_right(x, spell)
            pairs.append(pos)
        return pairs
