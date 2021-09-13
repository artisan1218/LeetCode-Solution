#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # monotonic stack
        
        for i, h in enumerate(heights):
            start = i
            # when we have a bar that is lower than the height of bar on top of stack
            # we pop the lower bar out of the stack and calculate the area of max rectangle
            while len(stack)!=0 and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            # we only push the index, height pair when the current bar is higher than
            # the height of bar on top of stack, this is why it's monotonic
            stack.append((start, h)) 
            
        # check the remaining the bar in the stack
        # since the remaining bar are guranteed to be in increasing order, the width is simply
        # the total length of the heights
        for idx, height in stack:
            maxArea = max(maxArea, height * (len(heights)-idx))
            
        return maxArea
        
        
if __name__ == '__main__':
    solver = Solution()
    heights = [2,1,5,6,2,3, 1]
    print(solver.largestRectangleArea(heights))


# In[ ]:




