# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA==None or headB==None:
            return None
        cur1=headA
        cur2=headB
        count1=count2=0
        while cur1!=None:
            count1+=1
            cur1=cur1.next
        while cur2!=None:
            count2+=1
            cur2=cur2.next
        cur1=headA
        cur2=headB
        if count1>count2:
            i=0
            while cur1!=None and i<count1-count2:
                cur1=cur1.next
                i+=1
        else:
            i=0
            while cur2!=None and i<count2-count1:
                cur2=cur2.next
                i+=1
        while cur1!=None and cur2!=None and cur1!=cur2:
            cur1=cur1.next
            cur2=cur2.next
        return cur1
