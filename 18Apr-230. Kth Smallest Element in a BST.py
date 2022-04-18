# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        temp=[]
        def travel(root,temp):
            if root==None:
                return
            else:
                travel(root.left,temp)
                temp.append(root.val)
                travel(root.right,temp)
            return temp
        x=travel(root,temp)
        heapq.heapify(x)
        temp=nsmallest(k,x)
        return temp[k-1]
