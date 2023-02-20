# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        res=[]
        q=[]
        q.append(root)
        while(len(q)!=0):
            ans=[]
            n=len(q)
            for i in range(n):
                curr=q.pop(0)
                ans.append(curr.val)
                if curr.left!=None:
                    q.append(curr.left)
                if curr.right!=None:
                    q.append(curr.right)
            res.append(ans)
        for i in range(len(res)):
            if i%2!=0:
                res[i]=res[i][::-1]
        return res
