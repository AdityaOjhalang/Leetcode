class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        i,j =0,n-1
        s = list(s)
        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while j > i and s[j] not in vowels:
                j -= 1
            
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        
        return "".join(s)