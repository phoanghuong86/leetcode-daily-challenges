# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
		if root is None: 
			return False
		if root.left is None and root.right is None:
			if root.val == targetSum:
				return True
			elif root.val != targetSum:
				return False
		elif root.left is not None and root.right is None:
			return self.hasPathSum(root.left, targetSum-root.val)
		elif root.left is None and root.right is not None: 
			return self.hasPathSum(root.right, targetSum-root.val)
		elif root.left is not None and root.right is not None:
			return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val) 
