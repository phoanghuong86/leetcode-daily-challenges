# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        if not root: return  0

        result = 0
        q = collections.deque()

        if root.left:         
            q.append((root.left, "left", 1))


        if root.right: 
            q.append((root.right, "right", 1))


        while q:
            current_node, left_right, value = q.popleft()

            if not current_node: continue

            result = max(result,value)

            if left_right == "left":
                    q.append((current_node.left, "left",  1)) 
                    q.append((current_node.right, "right", value + 1))  
            else: 
                q.append((current_node.right, "right", 1))
                q.append((current_node.left, "left", value + 1))

        return result
