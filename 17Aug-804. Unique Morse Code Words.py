class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        keys=["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        values=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dict_arr={}
        dict_arr=dict(zip(keys, values))
        
        for word in words:
            code=""
            for i in word:
                code = code + dict_arr[i]
            
            if code not in count_dict:
                count_dict[code]=1
            else:
                count_dict[code]=count_dict[code]+1
            
        return len(count_dict)
        
                
        
        
        
        
