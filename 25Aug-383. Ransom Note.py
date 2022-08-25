class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ran={}
        mag={}
        for i in ransomNote:
            if i in ran:
                ran[i]+=1
            else:
                ran[i]=1
        for i in magazine:
            if i in mag:
                mag[i]+=1
            else:
                mag[i]=1
        print(ran,mag)
        for i in ran:
            #print(ran[i],mag[i])
            if i in mag:
                if ran[i]<=mag[i]:
                    continue
            return False
        return True    ```
