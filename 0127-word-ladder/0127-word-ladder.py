class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                key = word[0:i] + "*" + word[i+1:]
                graph[key].append(word)
        
        queue = deque([(beginWord,1)])
        seen = {beginWord}

        while queue:
            word,steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                key = word[0:i] + "*" + word[i+1:]
                for neigh in graph[key]:
                    if neigh not in seen:
                        seen.add(neigh)
                        queue.append((neigh,steps+1))
        return 0
