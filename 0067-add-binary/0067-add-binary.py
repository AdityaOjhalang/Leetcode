class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        a = a[::-1]
        b = b[::-1]
        carry = 0
        for i in range(max(len(a), len(b))):
            vala = int(a[i]) if i < len(a) else 0
            valb = int(b[i]) if i < len(b) else 0
            total = vala + valb +  carry
            char = str(total % 2)
            res = char + res
            carry = total // 2
        
        if carry:
            res = "1" + res
    
        return res
