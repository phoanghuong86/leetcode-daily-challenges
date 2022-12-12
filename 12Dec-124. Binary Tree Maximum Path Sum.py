# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root, s = -inf) -> int:
        
        def dfs(n):                    # this recursive function 
            nonlocal s                 # computes best partial path
            if not n : return 0        # sum starting from node 'n':
            l = max(0, dfs(n.left))    # [1] compute left and right
            r = max(0, dfs(n.right))   #     partial path sums
            s = max(s, l + r + n.val)  # [2] compute full path sum
            return n.val + max(l, r)   # [3] choose best partial sum

        dfs(root)
        return s
