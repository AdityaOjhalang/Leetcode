class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        #removing spaces
        while left <= right and s[left] == " ":              
            left +=1
        while left <= right and s[right] == " ":
            right -= 1
        
        word = []
        queue = deque()
        while left <= right:
            if word and s[left] == " ":
                queue.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        queue.appendleft("".join(word))
        return " ".join(queue)
                