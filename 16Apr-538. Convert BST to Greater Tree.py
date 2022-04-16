# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum_val = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return
            dfs(node.right)
            self.sum_val += node.val
            node.val = self.sum_val
            dfs(node.left)
        
        dfs(root)
        return root
