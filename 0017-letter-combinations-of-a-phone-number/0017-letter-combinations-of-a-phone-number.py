class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if len(digits) == 0:
            return []
        res = []
        def backtrack(i,path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            possiblechars = letters[digits[i]]
            for char in possiblechars:
                path.append(char)
                backtrack(i+1,path)
                path.pop()

        backtrack(0,[])
        return res 