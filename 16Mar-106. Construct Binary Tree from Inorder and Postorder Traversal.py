# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.formBinaryTree(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)

    def formBinaryTree(self, inOrder: List[int], postOrder: List[int], start: int, end: int, start2: int, end2: int) -> TreeNode:
        if start > end:
            return None
        middle = TreeNode(postOrder[end2])
        mid = 0
        for i in range(start, end + 1):
            if inOrder[i] == middle.val:
                mid = i
                break
        noOfElements = mid - 1 - start
        x = noOfElements + start2  # i.e the end of postOrderTraversal of left subtree
        middle.left = self.formBinaryTree(inOrder, postOrder, start, mid - 1, start2, x)
        middle.right = self.formBinaryTree(inOrder, postOrder, mid + 1, end, x + 1, end2 - 1)
        return middle
