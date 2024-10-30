class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(n)}

        for crs,pre in prerequisites:
            premap[crs].append(pre)
        
        seen = set()

        def dfs(crs):

            if premap[crs] == []:
                return True
            
            if crs in seen and premap[crs] != []:
                return False
            
            seen.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            
            premap[crs] = []
            return True
        
        for crs in range(n):
            if not dfs(crs):
                return False
        return True
            
