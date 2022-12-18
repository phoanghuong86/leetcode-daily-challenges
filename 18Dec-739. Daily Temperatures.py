class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        maxS = [] 
        i, j = 0 , 1
        answer = [0 for _ in range(len(temperatures))]
        while j < len(temperatures):
            if temperatures[j] > temperatures[i]:
                answer[i] = j - i
                while maxS and temperatures[maxS[-1]] < temperatures[j]:
                    answer[maxS[-1]] = j - maxS[-1]
                    maxS.pop()
                
            else:
                maxS.append(i)
            i += 1
            j += 1
                
        return answer
