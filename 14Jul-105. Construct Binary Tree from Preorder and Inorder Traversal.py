# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder == []:
            return None
        root = TreeNode()
        # print(inorder, preorder)
        root.val = preorder[0]
        i = inorder.index(root.val)
        ino = inorder[:i]
        root.left = self.buildTree(preorder[1:], ino)
        root.right = self.buildTree(preorder[len(ino)+1:], inorder[i+1:])
        return root
