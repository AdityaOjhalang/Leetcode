class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay = len(haystack)
        ned = len(needle)

        if hay < ned:
            return - 1
        for i in range(len(haystack)):
            if haystack[i:i+ned] == needle:
                return i
        return -1