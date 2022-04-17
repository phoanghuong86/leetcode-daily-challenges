# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.head = TreeNode(0, None, None)
        self.ans = self.head
        
        def inorder(root) : 
            if root : 
                inorder(root.left)
                lef = TreeNode(root.val, None, None)
                self.head.right = lef
                self.head = self.head.right
                inorder(root.right)
        inorder(root)
        return self.ans.right
