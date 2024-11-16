class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == " ":
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == " ":
            right -= 1

        # intialize word arr and deque
        word , queue = [] , deque()

        # if space is found
        while left <= right:
            if s[left] == " " and word:
                queue.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        
        queue.appendleft("".join(word))
        return " ".join(queue)


        # no space is found

        # return
