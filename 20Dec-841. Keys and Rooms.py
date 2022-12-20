class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keyset=set()
        keyset.add(0)
        visited=set()
        def func(keyset):
            for i in list(keyset): 
                if i not in visited:
                    visited.add(i)
                    for key in rooms[i]:
                        keyset.add(key)
                        for k in rooms[key]:
                            keyset.add(k)
                        visited.add(key)
            if visited!=keyset:
                func(keyset)
        func(keyset)
                    
        if len(visited)==len(rooms):
            return True
        return False
