# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def check1(d):
            flag=0
            for x in d:
                if d[x]%2!=0:
                    flag+=1
            return flag<2
        self.c=0
        def check(root,d):
            if root.val in d:
                d[root.val]+=1
            else:
                d[root.val]=1
            if root.left==None and root.right==None:
                #print(d)
                if check1(d):
                    self.c+=1
                return
            
            if root.left:
                check(root.left,dict(d))
            if root.right:
                check(root.right,dict(d))
        d={}
        check(root,d)
        return self.c
