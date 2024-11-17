class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hmap = Counter(magazine)
        for c in ransomNote:
            if hmap[c] <= 0:
                return False
            hmap[c] -= 1
        return True
