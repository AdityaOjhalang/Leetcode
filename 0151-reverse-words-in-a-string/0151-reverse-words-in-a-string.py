class Solution:
    def reverseWords(self, s: str) -> str:
        i,j = 0 , len(s) - 1
        while i <= j and s[i] == " ":
            i+= 1
        while i <= j and s[j] == " ":
            j -= 1

        word = []
        queue = deque()
        while i <= j:
            if word and s[i] == " ":
                queue.appendleft("".join(word))
                word = []
            elif s[i] != " ":
                word.append(s[i])
            i += 1
        queue.appendleft("".join(word))
        return " ".join(queue)

 