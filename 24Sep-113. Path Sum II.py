# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        
        def dfsBackTracking(node, sumPath):
            if not node: 
                return 
            
            sumPath.append(node.val)
                
            if not node.left and not node.right:
                if sum(sumPath) == targetSum:
                    output.append(sumPath[:])
            
            dfsBackTracking(node.left, sumPath)
            dfsBackTracking(node.right, sumPath)
                    
            sumPath.pop()  
            
        dfsBackTracking(root, [])
        
        return output
