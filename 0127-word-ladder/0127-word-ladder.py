class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                key = word[0:j] + "*" + word[j+1:]
                graph[key].append(word)

        seen = {beginWord}
        queue = deque([(beginWord,1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for j in range(len(word)):
                key = word[0:j] + "*" + word[j+1:]
                for neigh in graph[key]:
                    if neigh not in seen:
                        seen.add(neigh)
                        queue.append((neigh,steps+1))
        return 0
