'''
Python
Accepted
28 ms
13.6 mb
O(n2)
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        length = len(nums)           # length of the list
        return_list = []             # return list                
        found = False                # variable stores if we found the answer
                
        for i in range(len(nums)):
            
            if found == True:                           # Stop looping if the answer is found, since there must only have one answer
                break
            
            for j in range(len(nums)):                  # Could improve here by searching only part of numbers after i 
                
                if (i != j):                            # Could not add with itself
                    
                    if (nums[i] + nums[j]) == target:     # Check if the answer is met, if so add the value to the return list
                        
                        return_list.append(i)              
                        return_list.append(j)
                        found = True                      # set found to true
                        break                             # Stop searchinig if the answer is found
                        
                    
        return return_list
                        
