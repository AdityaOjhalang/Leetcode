class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        graph = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            graph[key].append(word)
        return list(graph.values())