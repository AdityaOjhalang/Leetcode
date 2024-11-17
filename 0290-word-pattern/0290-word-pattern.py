class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        map1 = {}
        map2 = {}
        if len(pattern) != len(words):
            return False
        for i in range(len(words)):
            char1 = pattern[i]
            char2 = words[i]
            if (char1 in map1 and map1[char1] != char2) or (char2 in map2 and map2[char2] != char1):
                return False
            map1[char1] = char2
            map2[char2] = char1
        return True