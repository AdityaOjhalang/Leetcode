class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                last_bracket = stack.pop()
                if brackets[last_bracket] != char:
                    return False
        return not stack
