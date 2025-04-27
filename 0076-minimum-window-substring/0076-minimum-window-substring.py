class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = {}

        have_count = 0
        need_count = len(need)

        res = [-1,-1]
        res_len = float("inf")

        left = 0 
        for right in range(len(s)):
            char = s[right]

            have[char] = have.get(char,0) + 1
            if char in need and have[char] == need[char]:
                have_count += 1

            while have_count == need_count :
                if (right- left + 1) < res_len:
                    res = [left,right]
                    res_len = right - left + 1
                remove = s[left]
                have[remove] -= 1
                if remove in need and have[remove] < need[remove]:
                    have_count -= 1
                left += 1
            l,r = res

        if res_len != float("inf"):
            return s[l:r+1]
        else:
            return ""