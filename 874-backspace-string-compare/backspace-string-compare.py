class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def build(s:str):
            stack = []
            for char in s:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack

        if build(s) == build(t):
            return True
        else:
            return False 