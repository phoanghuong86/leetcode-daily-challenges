class Solution:
    def maxAncestorDiff(self, root):
        
        diff = 0
        def dfs(n):
            nonlocal diff
            vals = [n.val]
            if n.left  : vals.extend(dfs(n.left))
            if n.right : vals.extend(dfs(n.right))
            mn, mx = min(vals), max(vals)
            diff = max(diff, abs(n.val - mn), abs(n.val - mx))
            return (mn, mx)
        
        dfs(root)
        return diff
