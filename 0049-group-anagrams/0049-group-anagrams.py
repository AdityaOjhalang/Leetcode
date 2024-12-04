class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            i = tuple(sorted(s))
            anagrams[i].append(s)
        return list(anagrams.values())