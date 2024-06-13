class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = Counter(s)
        n = len(t)
        if len(s) != len(t):
            return False
        for i in range(n):
            if t[i] in map1 and map1[t[i]] > 0 :
                map1[t[i]] -= 1
            else:
                return False
        return True