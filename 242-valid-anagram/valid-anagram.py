class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = Counter(s)
        map2 = Counter(t)

        if map1 == map2 :
            return True 
        else:
            return False
