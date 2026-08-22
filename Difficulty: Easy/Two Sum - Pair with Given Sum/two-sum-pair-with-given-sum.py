class Solution:
	def twoSum(self, arr, target):
		# code here
		hashmap= set()
		
		for i in range (0,len(arr)):
		    
		    rem = target - arr[i]
		    
		    if rem in hashmap:
		        return True
		        
		    hashmap.add(arr[i])
		    
	    return False
		