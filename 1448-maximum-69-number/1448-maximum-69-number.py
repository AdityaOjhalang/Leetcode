class Solution:
    def maximum69Number (self, num: int) -> int:
        charlist = list(str(num))
        for indx,char in enumerate(charlist):
            if char == "6":
                charlist[indx] = "9"
                break
        
        return int("".join(charlist))