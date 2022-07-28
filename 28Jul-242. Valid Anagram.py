from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Qucikly reject strings which are not of the same length
        if len(s) != len(t):
            return False
        
		# Construct the count dictionaries, but faster
        a = Counter(s)
        b = Counter(t)
		
		# Quickly reject cases where the counters have
		# different numbers of keys
        if len(a) != len(b):
            return False
        
		# Main rejection loop
        for key in a:
			# Reject if key is missing
            if key not in b:
                return False
			
			# Reject if the count at that key is not equal
            elif a[key] != b[key]:
                return False
            
        return True
