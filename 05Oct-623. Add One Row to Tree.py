# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        
        depth_map = {}
        # depth_map[1] = [root]
        self.get_depth_map(root, 1, depth_map)
        arr = depth_map[depth-1]
        print(len(arr))
        for node in arr:
            
            temp_left = node.left
            temp_right = node.right
            
            new_node_right = TreeNode(val)
            new_node_left = TreeNode(val)
            
            node.left = new_node_left
            node.right = new_node_right
            
            new_node_left.left = temp_left
            new_node_right.right = temp_right
        
        return root
            
