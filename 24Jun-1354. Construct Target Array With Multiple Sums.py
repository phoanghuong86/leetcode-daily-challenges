class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-i for i in target]
        heapify(target)
        while True:
            num = -heappop(target)
            if num == 1:
                # largest number is now 1, so we've found the solution, return True
                return True
            elif total - num == 1:
                # handle scenarios such as [1, 10000], where num % (total - num) is always 0
                return True
            elif total == num:
                # handles scenarios [2,2], [2]
                return False
            
            diff = num % (total - num)
            if diff == 0 or diff == num:
                # if the resultant difference = 0, we cannot form [1,1,1...]
                # if diff == num, that means we cannot reduce it further into 1
                return False
            
            heappush(target, -diff)
            total = diff + (total - num)
