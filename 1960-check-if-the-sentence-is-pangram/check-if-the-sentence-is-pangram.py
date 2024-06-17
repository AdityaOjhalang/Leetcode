class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dic = "abcdefghijklmnopqrstuvwxyz"
        hmap = {}
        
        for i in range(len(dic)):
            hmap[dic[i]] = i
        
        count = 0 

        for i in range(len(sentence)):
            curr = sentence[i]
            if curr in hmap :
                del hmap[curr]

        if len(hmap) == 0 :
            return True
        else:
            return False
                
        