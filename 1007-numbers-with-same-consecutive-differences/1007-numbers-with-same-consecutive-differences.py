class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(path):
            if len(path) == n:  # Base case: If the number has n digits
                res.append(int("".join(map(str, path))))  # Convert path to number
                return
            
            last = path[-1]  # Get the last digit of the current path
            for i in range(10):  # Check all digits from 0 to 9
                if abs(i - last) == k:  # Only consider valid next digits
                    path.append(i)  # Add digit to path
                    backtrack(path)  # Recurse to build the next digit
                    path.pop()  # Backtrack by removing the last digit

        res = []
        for start in range(1, 10):  # Start with digits 1 to 9 (no leading zeros)
            backtrack([start])
        return res