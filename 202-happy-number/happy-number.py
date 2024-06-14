class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def nexnum(n:int) -> int:
            output = 0
            while n>0:
                digit = n%10
                output += digit ** 2
                n = n//10
            return output

        while n not in visited:

            visited.add(n)

            n = nexnum(n)
            if n == 1 :
                return True

        return False
        




