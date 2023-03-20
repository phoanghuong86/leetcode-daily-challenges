class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        flower = 0
        for cur in flowerbed:
            if cur == 1:
                if prev == 1:
                    flower -= 1
                prev = 1
            else:
                if prev == 0:
                    flower += 1
                    prev = 1
                else:
                    prev = 0
        return flower >= n
                
