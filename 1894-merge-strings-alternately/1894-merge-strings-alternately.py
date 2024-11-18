class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        res = []
        while i < m and j < n:
            res += word1[i]
            i+=1
            res += word2[j]
            j+=1
        while i < m:
            res += word1[i]
            i+=1
        while j < n:
            res += word2[j]
            j+=1
        return "".join(res)

