# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ans=[]
        tt=[0]
        def dfs(root):
            if root is None:return 0
            cursum=dfs(root.left)+dfs(root.right)+root.val
            ans.append(cursum)
            tt[0]+=root.val
            return cursum
        dfs(root)
        return max(i*(tt[0]-i) for i in ans)%(10**9+7)
