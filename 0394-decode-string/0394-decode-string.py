class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currstr = ""
        currnum = 0
        for char in s:
            if char.isdigit():
                currnum = currnum * 10 + int(char)
            elif char == "[":
                stack.append((currnum,currstr))
                currnum = 0
                currstr = ""
            elif char == "]":
                repeatno,prevstr = stack.pop()
                currstr = prevstr + currstr * repeatno
            else:
                currstr += char
        return currstr