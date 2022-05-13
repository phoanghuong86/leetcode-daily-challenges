"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = [root, 'null']
        prev = None
        while queue:
            k = queue.pop(0)
            if k == 'null':
                if not queue: return root
                prev = None
                queue.append("null")
            else:
                k.next = prev
                prev = k
                if k.right: queue.append(k.right)
                if k.left: queue.append(k.left)
