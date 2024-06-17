class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        words = Counter(s)
        tocheck = words[s[0]]

        for w in words:
            if(words[w] != tocheck):
                return False
                break
        return True