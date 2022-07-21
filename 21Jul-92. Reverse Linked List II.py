# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import deque
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        root = head 
        point = head
        left -= 1
        right -= 1
        cache = deque()
        pointers = deque()
        for i in range(right+1) : 
            if i>=left : 
                if point is not None : 
                    cache.appendleft(point.val)
                    pointers.append(point)
            point = point.next

        for v,p in zip(list(cache),list(pointers)) :
            p.val = v
        
        return root
