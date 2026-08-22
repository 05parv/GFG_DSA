class Solution:
    def fibonacciNumbers(self,n):
        # code here
        ans = []
        i=0
        j=1
        
        ans.append(i)
        
        for nums in range (n-1):
            ans.append(j)
            next = i+j
            i=j
            j=next
        return ans
            