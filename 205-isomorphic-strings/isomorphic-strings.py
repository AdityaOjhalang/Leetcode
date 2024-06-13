class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if (char_s in map1 and map1[char_s] != char_t) or (
                char_t in map2 and map2[char_t] != char_s
            ):
                return False
            map1[char_s] = char_t
            map2[char_t] = char_s
            
        return True
