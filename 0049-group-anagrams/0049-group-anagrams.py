class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            index = tuple(sorted(word))
            anagrams[index].append(word)
        return list(anagrams.values())