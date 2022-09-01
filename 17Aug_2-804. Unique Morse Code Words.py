class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..'}
        code=[]
        complist=[]
        
        for word in words:
            list1=[i for i in word]
            
            for letter in word:
                if letter in morse:
                    code.append(morse[letter])
                    compcode = ''.join(code)
            complist.append(compcode)
            code.clear()
        res = [*set(complist)]
        return len(res)
