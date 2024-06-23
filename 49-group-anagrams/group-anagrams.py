class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = collections.defaultdict(list)

        for s in strs:
            index = tuple(sorted(s))
            anagrams[index].append(s)

        return list(anagrams.values())