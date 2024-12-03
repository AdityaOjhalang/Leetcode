class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in hmap:
                stack.append(char)
            
            else:
                if stack:
                    lastopen = stack.pop()
                    if hmap[lastopen] != char:
                        return False
                else:
                    return False 
        
        return True if len(stack) == 0 else False
