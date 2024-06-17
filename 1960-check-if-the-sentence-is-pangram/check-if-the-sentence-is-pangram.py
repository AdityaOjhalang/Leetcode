class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

            hset = set(sentence)
            if len(hset) != 26:
                return False
            else:
                return True
                
        