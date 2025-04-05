class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        ans = count = l = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        ans = count
        for i in range(k,len(s)):
            if s[i] in vowels:
                count += 1
            if s[l] in vowels:
                count -= 1
            l += 1
            ans = max(ans,count)
        return ans 