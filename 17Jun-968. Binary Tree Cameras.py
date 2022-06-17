# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cam = 0 # self.cam is used to keep track of cameras count
		
		
        #Postorder logic
        # function returns [boolean1, boolean2]
        # boolean1 indicates node is monitored or not
        # boolean2 indicates node is cam or not
        
        def dfs(root):
            
            if not root:
                #obviously there is no use of monitoring empty one.. so by default we think they r protected...
                #since it's empty.. It cannot be a cam
                
                return [True,False]
            
            if not root.left and not root.right:
                # since we need to monitor entire tree by less number of cams..
                # By common sense we can tell that leaf nodes are not act as cam
                # since leaf nodes dont have child.. for now they r not monitored..
                # so leaf nodes are conveying to its parent that it is not monitored by anything
                # also leaf node is conveying to its parent that it is not a cam..
                
                return [False,False]
            
            isProtectedLeft,isCamLeft = dfs(root.left)
            isProtectedRight, isCamRight = dfs(root.right)
            
            if not isProtectedLeft or not isProtectedRight:
                #If anyone of my child is not monitored..
                #then I need to become cam to monitor my children
                # so current node is a cam now
                self.cam += 1
                
                # since current node is a Cam, it can be monitored by itself..
                # So current node is conveying its ancestor that it is a cam and monitored by itself
                return [True,True]
            
            #since previously we checked current node's both children are monitored or not..
            #if both children are monitored then current node has to check itself that it is monitored or not...
            
            if isCamLeft or isCamRight:
                #If anyone of my child is Cam then I am monitored by them..
                #so current node will not be cam.. coz it is monitored by its children and its children also monitored by someone
                
                # so current node is conveying its ancestor that it is not a cam but monitored..
                return [True,False]
            
            
            # if both current node's children are monitored and neither of it's children are cam
            # then current node have to request its parent that I need u to monitor me
            
            # since current node's children are protected.. current node will not be an cam
            
            # so it is conveying to its parent that it is not a cam and not monitored
            return [False,False]
            
          
        isRootProtected, isRootCam = dfs(root)
        
        #if root is not monitored then it needs to become a cam
        #obviously it dont have any parent also to request for monitoring
        if not isRootProtected:
            self.cam += 1
        
        return self.cam
