# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        def traverse(node, depth):
            if not node:
                return
            if not ret or depth > len(ret) - 1:
                ret.append([])
            ret[depth].append(node.val)
            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)
        traverse(root, 0)
        return ret
        
