class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False

        hmap1 = Counter(word1)
        hmap2 = Counter(word2)

        return sorted(hmap1.values()) == sorted(hmap2.values())
