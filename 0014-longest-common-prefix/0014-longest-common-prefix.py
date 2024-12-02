class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key = len)
        for i in range(len(smallest)):
            for s in strs:
                if s[i] != smallest[i]:
                    return smallest[:i]

        return smallest