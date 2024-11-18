class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in hmap:
                stack.append(char)
            else:
                if not stack:
                    return False
                last_open = stack.pop()
                if hmap[last_open] != char:
                    return False
        return not stack
