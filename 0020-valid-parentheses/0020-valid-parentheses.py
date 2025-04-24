class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in hmap:
                stack.append(char)
            else:
                if stack:
                    last = stack.pop()
                    if hmap[last] != char:
                        return False
                else:
                    return False
        return not stack