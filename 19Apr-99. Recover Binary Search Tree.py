# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.node1, self.node2, self.prev_elem = TreeNode(), TreeNode(), TreeNode(float('-inf'))
        def dfs(node):
            if not node: return
            dfs(node.left)
            if self.node1.val == 0 and self.prev_elem.val >= node.val: self.node1 = self.prev_elem
            if self.node1.val != 0 and self.prev_elem.val >= node.val: self.node2 = node
            self.prev_elem = node
            dfs(node.right)
        dfs(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
