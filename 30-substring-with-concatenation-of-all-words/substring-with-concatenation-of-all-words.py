class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_length = len(words[0])
        num_words = len(words)
        substring_length = word_length * num_words
        word_count = Counter(words)
        results = []

        for i in range(len(s) - substring_length + 1):
            seen = {}
            for j in range(num_words):
                word_start = i + j * word_length
                word = s[word_start:word_start + word_length]
                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
            if seen == word_count:
                results.append(i)
        
        return results