class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        map1 = {}
        map2 = {}

        word = s.split()
        if (len(word)) != len(pattern):
            return False
        
        for i in range(len(word)):
            curr_p = pattern[i]
            curr_w = word[i]

            if (curr_w in map1 and map1[curr_w] != curr_p) or (curr_p in map2 and map2[curr_p] != curr_w):
                return False
            
            map1[curr_w] = curr_p
            map2[curr_p] = curr_w
        
        return True
