# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self,root):
        res=[]
        hashmap = {}
        def dfs(node, depth = 0):
            if node:
                if depth not in hashmap:
                    hashmap[depth] = [node.val]
                else:
                    hashmap[depth].append(node.val)

                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)
        for k,v in hashmap.items():
            res.append(sum(v)/float(len(v)))
        return res
