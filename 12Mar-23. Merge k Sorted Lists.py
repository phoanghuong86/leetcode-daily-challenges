# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next# Definition for singly-linked list.

# class ListNode:

#     def __init__(self, val=0, next=None):

#         self.val = val

#         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        nums = []

        for head in lists:

            while head:

                nums.append(head)

                temp = head

                head = head.next

                temp.next = None

        nums.sort(key = lambda x: x.val)

        head = ListNode()

        temp = head

        for i in nums:

            temp.next = i

            temp = temp.next

        return head.next

            


 

