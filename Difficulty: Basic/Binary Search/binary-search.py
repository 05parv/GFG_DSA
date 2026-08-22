class Solution:
    def binarySearch(self, arr, k):
        # code here
        low = 0
        high = len(arr)-1
        
        
        while high >= low:
            
            num = high + low
            
            mid = num//2
            
            
            if arr[mid] == k:
                return True
                
                
            if arr[mid] < k:
                low = mid + 1
                
            if arr[mid] > k:
                high = mid -1
                
                
        return False