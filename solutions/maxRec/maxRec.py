#!/usr/bin/env python
# coding: utf-8

# In[3]:


from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # converting max rec question to max rec in histogram by calculating the height of each column in matrix
        if len(matrix)==0:
            return 0
        else:
            ans = 0
            rowNum = len(matrix)
            colNum = len(matrix[0])

            # heights stands for the height of each 'column' of the matrix
            heights = [0 for _ in range(colNum)]

            # iterate over the matrix row by row
            for row in range(rowNum):
                # sum up the number of 1's in each column in that row in heights
                for col in range(colNum):
                    # if there is a 0, then the height of this column will be reset to 0
                    if matrix[row][col] == '0':
                        heights[col] = 0
                    else:
                        # if there is a 1, then the height of this column is increasing by 1
                        heights[col]+=1
                # calculate the current max area based on the heights up to this row
                curMax = self.largestRectangleArea(heights)
                ans = max(ans, curMax)

            return ans
    
    
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
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]]
    ans = solver.maximalRectangle(matrix)
    print(ans)


# In[ ]:




