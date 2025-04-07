class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        stack.append(asteroids[0])
        for i in range (1,len(asteroids)):
            curr = asteroids[i]
            while stack and (stack[-1]  > 0 and curr < 0 )  :
                if abs(stack[-1] == abs(curr)):
                    stack.pop()
                    break
                elif stack and abs(stack[-1]) > abs(curr):
                    break
                else:
                    stack.pop()
            else:   #else belogs to while loop
                stack.append(curr)

        return stack
