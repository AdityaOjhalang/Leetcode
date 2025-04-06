class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        arr1 = []
        arr2 = []

        for n in set1:
            if n not in nums2:
                arr1.append(n)
            
        
        for n in set2:
            if n not in nums1:
                arr2.append(n)

        return [arr1,arr2]