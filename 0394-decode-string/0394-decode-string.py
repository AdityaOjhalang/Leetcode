class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currstring = ""
        currnum = 0

        for char in s:
            if char.isdigit():
                currnum = currnum * 10 + int(char)

            elif char == "[":
                stack.append((currstring, currnum))
                currnum = 0
                currstring = ""

            elif char == "]":
                laststr, repeat = stack.pop()
                currstring = laststr + currstring * repeat
            else:
                currstring += char
            
        return currstring 
