class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        for i in path.split('/'):
            if i == '..':
                if result:
                    result.pop()
            elif i not in ('', '.'):
                result.append(t)
        
        return "/" + "/".join(result)
