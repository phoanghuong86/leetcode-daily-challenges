class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        n=len(pattern)
        arr=[0]*n
        j=0
        dici={}
        for i in range(n):
            if pattern[i] in dici:
                arr[i]=dici[pattern[i]]
                
            else:
                arr[i]=j
                dici[pattern[i]]=j
                j+=1
                
        ans=[]
        for word in words:
                temp={}
                narr=[0]*n
                j=0
                for i in range(n):
                    if word[i] in temp:
                        narr[i]=temp[word[i]]
                    
                    else:
                        narr[i]=j
                        temp[word[i]]=j
                        j+=1
                if narr==arr:
                    ans.append(word)
                
        return ans
            
