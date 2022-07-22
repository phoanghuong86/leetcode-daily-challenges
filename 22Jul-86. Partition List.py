# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        temp=[]                             # to store the values in temp
        curr = head
        while curr:
            temp.append(curr.val)
            curr = curr.next
        
        # check and replace the values which are < x and mark used values as -1e9
        curr = head
        for i in range(len(temp)):
            if temp[i] < x:
                curr.val = temp[i]
                curr = curr.next
                temp[i] = -1e9
        
        
        # remaining unused values can be replaced in list
        for e in temp:
            if e != -1e9:
                curr.val = e
                curr = curr.next
        
        return head
