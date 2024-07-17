class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calc(val1, val2, opr):
            if opr == "+":
                return (val1 + val2)
            elif opr == "-":
                return (val2 - val1)
            elif opr == "*":
                return (val1 * val2)
            else:
                return int(val2/val1)
        
        stack = []

        for t in tokens:
            if t in "+-*/":
                v1 = stack.pop()
                v2 = stack.pop()
                opr = t
                ans = calc(v1,v2,opr)
                stack.append(ans)
            else:
                stack.append(int(t))
        return stack.pop()