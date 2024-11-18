class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        patharr = path.split("/")
        print(patharr)
        for char in patharr:
            if char == "..":
                if stack:
                    stack.pop()
            elif char == '' or char == '.':
                continue
            else:
                stack.append(char)
        return "/" + "/".join(stack)