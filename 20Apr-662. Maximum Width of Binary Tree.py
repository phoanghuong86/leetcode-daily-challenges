# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def bfs(node):
            q = deque([(node, 0)])
            self.ans = 1
            while q:
                self.ans = max(self.ans, q[-1][1] - q[0][1] + 1)
                l = len(q)
                for _ in range(l):
                    c, b = q.popleft()
                    if c.left:
                        q.append((c.left, b << 1))
                    if c.right:
                        q.append((c.right, b << 1 | 1))
        bfs(root)
        return self.ans
