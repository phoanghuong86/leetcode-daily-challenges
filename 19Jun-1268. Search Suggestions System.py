# Dictionary Solution
# Time:     O(nlogn + n+k),     Sorts prodcuts once, iterates through products once and searchWord length once (k = length of search word).
# Space:    O(n),               Dictionary storing list of products.
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()                                     # Sort products lexigraphically.
        prefixToProducts = defaultdict(list)                # Maps prefix to products.
        
        prefix = ''
        for word in products:                               # Iterates through each word in products list.
            for character in word:                          # Iterates through each character in product word.
                prefix += character                         # Appends character to the current prefix.
                prefixToProducts[prefix].append(word)       # Appends prefix -> word maping to dictionary.
                
            prefix = ''                                     # Resets prefix for next word.
            
        results = []                                        # List to hold the search results.
        for character in searchWord:                        # Iterates through each character in searchWord.
            prefix += character                             # Appends character to current prefix.
            results.append(prefixToProducts[prefix][:3])    # Appends at most 3 words to list using current prefix.
            
        return results                                      # Returns results list containing products found with searchWord.
