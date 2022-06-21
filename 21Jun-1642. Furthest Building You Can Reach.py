from heapq import heapify, heappushpop
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Complexity:
        # - Time: O(N) if L >= N, else O(N*log(L))
        #   where N is the number of buildings, L is the number of ladders
        # - Space: O(1) if L == 0, else O(min(N,L))

        heightIter = iter(heights)
        furthestBuildingIdx = 0
        height = next(heightIter)

        # Simpler logic if we have no ladders
        if ladders == 0:
            # Complexity:
            # - Time: O(N)
            # - Space: O(1)
            for nextHeight in heightIter:
                if nextHeight > height:
                    heightIncrease = nextHeight - height
                    if bricks < heightIncrease:
                        break
                    bricks -= heightIncrease
                furthestBuildingIdx += 1
                height = nextHeight
            return furthestBuildingIdx

        # We have some ladders

        # - Advance until all ladders get used and keep track of the height increases we used them for
        #   Complexity:
        #   - Time: O(N)
        #   - Space: O(min(N, L))
        ladderHeightIncreaseHeap = []
        previousHeight = height
        for height in heightIter:
            furthestBuildingIdx += 1
            if height > previousHeight:
                ladderHeightIncreaseHeap.append(height - previousHeight)
                ladders -= 1
                if ladders == 0:
                    break
            previousHeight = height
        else:
            # We reached the last building
            return furthestBuildingIdx

        # - Make a heap from the ladder use tracking data, in order to get quick access to the min value
        #   Complexity:
        #   - Time: O(log(L))
        #   - Space: O(1)
        heapify(ladderHeightIncreaseHeap)

        # - Continue to advance, and, when a there's a height increase, determine whether to swap
        #   the use of bricks here with the smallest height increase where a ladder is currently
        #   used; then, make sure we have enough bricks for that height increase
        #   Complexity:
        #   - Time: O(N*log(L))
        #   - Space: O(1)
        for nextHeight in heightIter:
            if nextHeight > height:
                heightIncrease = heappushpop(ladderHeightIncreaseHeap, nextHeight - height)
                if bricks < heightIncrease:
                    break
                bricks -= heightIncrease
            furthestBuildingIdx += 1
            height = nextHeight

        return furthestBuildingIdx
