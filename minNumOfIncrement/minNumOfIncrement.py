#!/usr/bin/env python
# coding: utf-8

# In[29]:


from typing import List

class Solution:
    def minNumberOperationsBruteForce(self, target: List[int]) -> int:
        def countBlocks(nums, level):
            blocks = 0
            for i, num in enumerate(nums):
                if i==0 and num-level>0:
                    blocks = 1
                elif num-level > 0 and nums[i-1]-level <= 0:
                    blocks += 1
            return blocks
        
        height = max(target)
        level = 0
        minNum = 0
        for i in range(height):
            minNum += countBlocks(target, level)
            level+=1
        
        return minNum
    
    def minNumberOperations(self, target: List[int]) -> int:
        result = target[0]
        prev = target[0]
        for i in range(1, len(target)):
            if target[i] > prev:
                result = result + target[i] - prev
            prev = target[i]
        return result
        
if __name__ == '__main__':
    solver = Solution()
    target = [3,1,5,4,2]
    result = solver.minNumberOperations(target)
    print(result)


# In[ ]:




