class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hmap = Counter(s)

        for char in t:
            if char not in hmap or hmap[char] <= 0:
                return char
            else:
                hmap[char] -= 1
        