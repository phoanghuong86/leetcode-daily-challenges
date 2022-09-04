# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols_hash_map = collections.defaultdict(lambda : collections.defaultdict(list))
        min_col = math.inf
        max_col = -math.inf
        max_row = -math.inf
        def traverse(root, row, col):
            nonlocal min_col, max_col, max_row
            if not root:
                return
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            max_row = max(max_row, row)
            bisect.insort(cols_hash_map[col][row], root.val)
            
            traverse(root.left, row + 1, col - 1)
            traverse(root.right, row + 1, col + 1)
            
        traverse(root, 0, 0)
        res = []
        for i in range(min_col, max_col + 1):
            tmp = []
            for j in range(max_row + 1):
                tmp.extend(cols_hash_map[i][j])
            res.append(tmp)
        return res
