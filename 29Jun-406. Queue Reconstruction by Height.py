class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x : (-x[0], x[1]))  
        result = []

        while people:
            curr = people.pop(0)        
            if curr[1] == len(result):  # after sort at beginning, curr[i] >= len(result), it will not be smaller
                result.append(curr)     
            else: 
                result.insert(curr[1], curr)

        return result
