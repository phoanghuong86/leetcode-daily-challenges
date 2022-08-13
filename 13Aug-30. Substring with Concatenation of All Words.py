class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_word  = len(words[0])
        count_words = len(words)
        len_internal_str = count_words * len_word
        a = 0
        lst = []
        while a <= (len(s) - len_internal_str):
            sub_string = s[a:(a + len_internal_str)]
            if len(sub_string) < len_internal_str : break
            w = self.allword(sub_string, words)
            if w : 
                lst = lst + [a]
            a = a + 1
        return lst
    
    def allword(self, s: str, words: List[str]) -> bool:
        len_word = len(words[0])
        no_words = [s[i:(i + len_word)] for i in range(0, len(s), len_word) ]
        for w in words:
            if w in no_words:
                no_words.remove(w)
            else: return False
        return True
