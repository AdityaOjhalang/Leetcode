class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(a,b,opr):
            a = int(a)
            b = int(b)
            if opr == "+":
                return (a + b)
            if opr == "*":
                return (a * b)
            if opr == "-":
                return (b - a)
            if opr == "/":
                return (b / a)

        stack = []
        for t in tokens:
            if t in "+-*/":
                a = stack.pop()
                b = stack.pop()
                val = calculate(a,b,t)
                stack.append(val)
            else:
                stack.append(t)

        return int(stack.pop())