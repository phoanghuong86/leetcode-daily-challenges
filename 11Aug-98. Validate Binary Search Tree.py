# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def rightMostNode(rmn,curr):
            while rmn.right!=None and rmn.right!=curr:
                rmn = rmn.right
            return rmn

        prev,curr = None,root
        while curr:
            left = curr.left
            if not left:
                if prev and prev.val>=curr.val:
                    return False
                prev = curr
                curr = curr.right
            else:
                rmn = rightMostNode(left,curr)
                if rmn.right == None:
                    rmn.right = curr
                    curr = curr.left
                else:
                    if prev.val>=curr.val:
                        return False
                    rmn.right = None
                    prev = curr
                    curr = curr.right

        return True
