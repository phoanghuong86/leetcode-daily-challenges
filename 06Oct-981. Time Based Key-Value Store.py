class TimeMap(object):

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key, value, timestamp):
        self.d[key].append((timestamp, value))

        
    def get(self, key, timestamp):
        if key not in self.d:
            return ''
        ans = -1
        temp = self.d[key]
        l, r = 0, len(temp)-1
        while l <= r:
            m = (l+r)/2
            if temp[m][0]<=timestamp:
                l = m+1
                ans = m
            else:
                r = m-1
        if ans == -1:
            return ''
        return temp[ans][1]
