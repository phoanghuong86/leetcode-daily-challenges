# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        my_queue = []
        my_queue.append([original, cloned]) # Roots
        
        while len(my_queue) > 0:
            elem_o, elem_c = my_queue.pop(0)
            if elem_o == target:
                return elem_c
            
            if elem_o.left:
                my_queue.append([elem_o.left, elem_c.left])
            if elem_o.right:
                my_queue.append([elem_o.right, elem_c.right])
        
        return None
