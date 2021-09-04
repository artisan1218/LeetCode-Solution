#!/usr/bin/env python
# coding: utf-8

# In[4]:


from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        for length in range(1, len(nums)+1):
            self.backtrack(nums, current, result, 0, length)
        return result
        
    def backtrack(self, nums, current, result, start, length):
        if len(current) == length:
            result.append(current.copy())
        else:
            for i in range(start, len(nums)):
                if len(current) + len(nums) - i + 1 >= length:
                    current.append(nums[i])
                    self.backtrack(nums, current, result, i+1, length)
                    current.pop()
                    
    def subsetsCascading(self, nums: List[int]) -> List[List[int]]:
        # start with empty list
        result = [[]]
        
        for new in nums:
            # use the previous length of the result, so assign the length of result to n
            n = len(result)
            for i in range(n):
                result.append(result[i]+[new])
        return result

    
if __name__ == '__main__':
    solver = Solution()
    nums = [1,2,3]
    result = solver.subsetsCascading(nums)
    print(result)


# In[ ]:




