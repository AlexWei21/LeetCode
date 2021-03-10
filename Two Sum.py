'''
Python
Accepted
28 ms
13.6 mb
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        length = len(nums)
        return_list = []
        new_nums = []
        index = 0;
        found = False
        
        for i in nums:
            if i < target:
                new_nums.append(i)
                index += 1
                
        for i in range(len(nums)):
            
            if found == True:
                break
            
            for j in range(len(nums)):
                
                if (i != j):
                    
                    if (nums[i] + nums[j]) == target:
                        
                        return_list.append(i)
                        return_list.append(j)
                        found = True
                        break
                        
                    
        return return_list
                        
