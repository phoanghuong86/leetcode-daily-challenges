class WordFilter:
    def __init__(self, words: List[str]):
        self.root = {}
        for i, word in self.u(words):
            for j in range(len(word)):
                wrap = word[~j:] + '#' + word
                cur = self.root
                for c in wrap:
                    if c not in cur:
                        cur[c] = {}
                    cur = cur[c]
                    cur['idx'] = i
                
    def u(self, words):
        seen = set()
        unique_words = []
        for i in range(len(words) - 1, -1, -1):
            word = words[i]
            if word not in seen:
                seen.add(word)
                unique_words.append((i, word))
        return reversed(unique_words)
                
    def f(self, prefix: str, suffix: str) -> int:
        target = suffix + '#' + prefix
        cur = self.root
        for c in target:
            if c not in cur:
                return -1
            cur = cur[c]
        return cur['idx']
