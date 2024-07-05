class Solution:
    def calculate(self, s: str) -> int:

        output,curr,sign,stack = 0,0,1,[]
        for c in s :
            if c.isdigit():
                curr = curr * 10 + int(c)
            elif c in "+-":
                output += curr * sign
                curr = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(output)
                stack.append(sign)
                sign = 1
                output = 0 #curr will not be 0 always a sign beofre opening
            elif c == ")":
                output += sign*curr
                output *= stack.pop()
                output += stack.pop()
                curr=0
        return output + ( curr * sign)
