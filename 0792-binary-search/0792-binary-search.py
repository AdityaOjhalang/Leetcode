class Solution:
    def search(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right )//2 
            if arr[mid] == target:
                return mid 
            if arr[mid] > target:
                right = mid - 1
            if arr[mid] < target:
                left = mid + 1
        
        return -1
                