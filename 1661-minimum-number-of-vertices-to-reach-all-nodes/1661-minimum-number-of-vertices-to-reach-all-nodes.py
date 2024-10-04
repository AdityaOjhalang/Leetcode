class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inorder = [0]*n

        for _,y in edges:
            inorder[y] = 1
        
        print(inorder)
        res = []
        for i in range(len(inorder)):
            if inorder[i] == 0:
                res.append(i)
        return res 