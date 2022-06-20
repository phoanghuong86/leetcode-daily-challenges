class TrieNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else {}

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        
        words = ["app", "apple", "le"]
        
        ref strings = ["app#apple#le#", "apple#le#app#", "apple#app#"]
        
        The only way to reduce the ref string is to combine the words with similar postfixes as much as possible
        Prefixes do not matter
        
        The result will be len("#".merged_words + 1) # +1 for the last hash
        
        How do we optimize the merged_words?
        
        Example:
        ["apple", "ple", "le", "dle", "gle"]
        
        suffix_trie = {None: {e: {l:{
            p: {#: None, p: {}},
            #: None,
            d: {#: None},
            g: {#: None},
        }}}}
        """
        def add_reversed_word(root, word):
            cur = root
            for sym in word[::-1]:
                if sym not in cur.children:
                    cur.children[sym] = TrieNode(val=sym)
                cur = cur.children[sym]
                # absorb the word if a longer word is present
                if "#" in cur.children:
                    del cur.children["#"]
            
            # only add a word start if no longer words present
            if ("#" not in cur.children) and (not cur.children):
                cur.children["#"] = None
                
        def traverse(root):
            """traverses the suffix tree and returns all the words"""
            results = []
            for sym in root.children:
                if sym == "#":
                    results.append("")
                else:
                    results.extend([s + sym for s in traverse(root.children[sym])])
            return results
        
        # initialize suffix tree
        suffixes = TrieNode()
        [add_reversed_word(suffixes, word) for word in words]
        
        # traverse the suffix tree and grasp all the merged words
        merged_words = traverse(suffixes)
        
        # return length of all the merged words + "#" for each word ending
        return sum(len(w) for w in merged_words) + len(merged_words)
