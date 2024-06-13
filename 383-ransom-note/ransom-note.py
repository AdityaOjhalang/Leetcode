class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n = len(ransomNote)
        tobuild = Counter(magazine)
        for i in range(len(ransomNote)):
            if(tobuild[ransomNote[i]] > 0 ):
                tobuild[ransomNote[i]] -= 1
            else:
                return False
        return True
