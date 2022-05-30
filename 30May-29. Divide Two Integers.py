class Solution:
    def divide(self, dividend: int, divisor: int):
        
        def base(dividend,divisor):
            i=1000000000
            while i*divisor>=dividend:
                i=i/10
            return i
        
        fin_cnt=0
        if divisor==1:
            if dividend>2147483647:
                return 2147483647
            elif dividend<-2147483648:
                return -2147483648
            else: return dividend
            
        elif divisor==-1:
            if dividend*-1>2147483647:
                return 2147483647
            elif dividend*-1<-2147483648:
                return -2147483648
            else: return dividend*-1
            
        neg=1
        if (dividend<0 and divisor>=0) or (divisor<0 and dividend>=0):
            neg=-1
        dividend=abs(dividend)
        divisor=abs(divisor)  
        
        while dividend>=divisor:
            bs=base(dividend,divisor)
            i=1
            val=0
            cnt=0
            while dividend>=val:
                val=bs*i*divisor
                if val<=dividend:
                    cnt=bs*i
                if val>dividend:
                    val=bs*(i-1)*divisor
                    break
                i+=1

            dividend=dividend-val
            fin_cnt=fin_cnt+cnt


        return int(fin_cnt)*neg
