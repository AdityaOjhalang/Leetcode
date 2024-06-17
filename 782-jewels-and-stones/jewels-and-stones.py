class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jset = set(jewels)
        stone_map = Counter(stones)
        res = 0 
        for stone in jset:
            if stone in stone_map:
                res += stone_map[stone]
        return res
