#!/usr/bin/env python
# coding: utf-8

# In[4]:


from typing import List

class Solution:
    def twoSumTwoPointer(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        cur_sum = numbers[left]+numbers[right]
        while cur_sum != target:
            if cur_sum > target:
                right-=1
            else:
                left+=1
            
            cur_sum = numbers[left]+numbers[right]
        return [left+1, right+1] # +1 because it's 1-based
    
    
    def twoSumMap(self, numbers: List[int], target: int) -> List[int]:
        num_dict = dict()
        for i, n in enumerate(numbers):
            num_dict[n] = i
        
        for i, num in enumerate(numbers):
            target2 = target-num
            if target2 in num_dict:
                return [min(i+1, num_dict[target2]+1), max(i+1, num_dict[target2]+1)]

        
        
numbers = [2,7,11,15]
target = 9
solver = Solution()
print(solver.twoSum(numbers, target))

