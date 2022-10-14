# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:

        # If there is a single node in the list, return None
        if not head.next:
            return None

        # Initialize three pointers: previous (point to a node before the slow pointer), slow, and fast
        prev, slow, fast = None, head, head

        # Iterate through all nodes
        while True:

            # Move all three pointers until the fast pointer reached the end of the list
            if fast.next and fast.next.next:
                prev, slow, fast = slow, slow.next, fast.next.next
                continue

            # Even case: Remove the next node after the slow pointer
            if fast.next:
                slow.next = slow.next.next

            # Odd case: Remove the node at the slow pointer
            else:
                prev.next = slow.next

            break

        return head
