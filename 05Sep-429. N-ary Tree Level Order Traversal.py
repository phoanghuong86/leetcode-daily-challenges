class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        dq = deque()
        
        if not root:
            return res
        
        dq.append(root)
        while dq:
            size = len(dq)
            level_nodes = []
            while size > 0:
                size -= 1
                node = dq.popleft()
                child_nums = len(node.children)
                for i in range(child_nums):
                    dq.append(node.children[i])
                    
                level_nodes.append(node.val)
                
            res.append(level_nodes)
            
        return res
