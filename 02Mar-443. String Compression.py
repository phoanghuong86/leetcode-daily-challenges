class Solution:
    def compress(self, chars: List[str]) -> int:
        if(len(chars)==1):
            return 1
        ans=[]
        c=None
        ct=0
        i=0
        for a in chars:
            if(a!=c):
                if(ct>1):
                    x=str(ct)
                    for m in x:
                        chars[i]=m
                        i+=1
                chars[i]=a
                i+=1
                ct=1
                c=a
            else:
                ct+=1
        if(ct==1):
            return i
        x=str(ct)
        for m in x:
            chars[i]=m
            i+=1
        return i
            
