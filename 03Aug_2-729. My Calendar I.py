class dll_node:
    def __init__(self,start,end,pre=None,nex=None):
        self.start = start
        self.end = end
        self.pre = None
        self.nex = None
class MyCalendar:
    def __init__(self):
        self.start = dll_node("start","start")
        self.end = dll_node("end","end")
        self.start.nex = self.end
        self.end.pre = self.start
	# debug print function
    # def print_dll(self,start,end):
    #     print(start,end)
    #     debug = self.start
    #     sqc = ""
    #     while debug.nex != None:
    #         sqc += str(debug.start)
    #         sqc += ","
    #         sqc += str(debug.end)
    #         sqc += ' | '
    #         debug = debug.nex
    #     print(sqc)
    def book(self, start: int, end: int) -> bool:
        event = dll_node(start,end)
        # insert to empty
        if self.start.nex == self.end:
            self.start.nex = event
            event.pre = self.start
            event.nex = self.end
            self.end.pre = event
            return True
        # insert head
        cur = self.start
        if cur.nex != self.end and event.end <= cur.nex.start:
            nex = cur.nex
            nex.pre = event
            event.nex = nex
            self.start.nex = event
            event.pre = self.start
            return True
        # insert tail
        if self.end.pre != self.start:
            tail = self.end.pre
            if event.start >= tail.end:
                tail.nex = event
                event.pre = tail
                event.nex = self.end
                self.end.pre = event
                return True
        # insert middle
        cur = self.start.nex
        while cur and cur != self.end and cur.nex != self.end:
            if cur.end <= event.start:
                if cur.nex == self.end:
                    cur.nex = event
                    event.pre = cur
                    event.nex = self.end
                    self.end.pre = event
                    return True
                elif cur.nex != self.end and cur.nex != None and cur.nex.start >= event.end:
                    nex = cur.nex
                    nex.pre = event
                    event.nex = nex
                    cur.nex = event
                    event.pre = cur
                    return True
            cur = cur.nex
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
