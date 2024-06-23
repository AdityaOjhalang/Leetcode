class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charTable = [0]*26

        for char in s:
            ind = ord(char) - ord("a")
            charTable[ind] +=1
        
        for char in t:
            ind = ord(char) - ord("a")
            charTable[ind] -=1

            if charTable[ind] < 0 :
                return False

        for count in charTable:
            if count != 0:
                return False

        return True