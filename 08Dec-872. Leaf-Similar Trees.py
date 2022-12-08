# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def leafs(node):  # generates sequence of leafs

            if node:

                if not (node.left or node.right):

                    yield node.val

                else:

                    yield from leafs(node.left)

                    yield from leafs(node.right)

        return all(

            l1 == l2 

            for l1, l2 in 

            zip_longest(leafs(root1), leafs(root2))

        )
