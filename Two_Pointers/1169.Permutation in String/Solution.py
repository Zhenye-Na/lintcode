from collections import Counter, defaultdict

class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    def checkInclusion(self, s1, s2):
        # write your code here
        target = s1 
        source = s2 

        if len(target) > len(source):
            return False 

        target_hash = {} 
        source_hash = {}

        for i in range(len(target)):
            target_hash[target[i]] = target_hash.get(target[i], 0) + 1 
            source_hash[source[i]] = source_hash.get(source[i], 0) + 1 
            
        if target_hash == source_hash:
            return True 
            
        for window_start in range(1, len(source) - len(target) + 1):
            window_end = window_start + len(target) - 1 
            
            source_hash[source[window_end]] = source_hash.get(source[window_end], 0) + 1 
            source_hash[source[window_start - 1]] -= 1 

            if source_hash[source[window_start - 1]] == 0:
                del source_hash[source[window_start - 1]]

            if source_hash == target_hash:
                return True 

        return False
