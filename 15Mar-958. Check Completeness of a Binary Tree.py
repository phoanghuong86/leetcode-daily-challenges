# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
                        

        queue = deque([root])                       #   <-- initialize the queue

        while queue[0]:                             #   <-- if and while top queue node is not null, pop   
            node = queue.popleft()                  #       it and then push its left child and right  
            queue.extend([node.left, node.right])   #       child onto the queue.

        while queue and not queue[0]:               #   <-- if and while top queue node is null, pop it. 
            queue.popleft()                         #        

        if queue: return False                      #   <-- If the queue is not empty, it must be non-null, so 
        return True                                 #       return False; if the queue is empty, return True.
