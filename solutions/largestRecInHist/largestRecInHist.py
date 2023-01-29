#!/usr/bin/env python
# coding: utf-8

# In[39]:


from typing import List

class Solution:
    def largestRectangleArea1(self, heights: List[int]) -> int:
        if len(heights)==0:
            return 0
        else:
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
        
    def largestRectangleArea2(self, heights: List[int]) -> int:
        if len(heights)==0:
            return 0
        else:
            maxArea = 0
            stack = [] # monotonic stack
            # instead of storing both index and height, we only store index
            for i in range(len(heights)):
                while len(stack)!=0 and heights[stack[-1]]>heights[i]:
                    idx = stack.pop()
                    width = i if len(stack)==0 else (i-stack[-1]-1)
                    maxArea = max(maxArea, heights[idx] * width)
                stack.append(i)
            
            while len(stack)!=0:
                idx = stack.pop()
                width = len(heights) if len(stack)==0 else (len(heights)-stack[-1]-1)
                maxArea = max(maxArea, heights[idx] * width)

            return maxArea
        
        
if __name__ == '__main__':
    solver = Solution()
    heights = [4,2,0,3,2,5]
    print(solver.largestRectangleArea2(heights))


# In[ ]:




