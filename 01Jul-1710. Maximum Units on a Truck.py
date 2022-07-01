class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x : -x[1])
        profit = 0
        
        for box in boxTypes:
            if (box[0] <= truckSize):
                profit += box[1] * box[0]
                truckSize -= box[0]
            else:
                profit += box[1] * truckSize
                break
        
        return (profit)
