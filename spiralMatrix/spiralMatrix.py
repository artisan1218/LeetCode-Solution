#!/usr/bin/env python
# coding: utf-8

# In[105]:


from typing import List
import math

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = list()
        
        numRows = len(matrix)
        numCols = len(matrix[0])
        totalNums = numRows * numCols
        seenNums = 0
        
        left2right_row = 0
        offset = 0
        while seenNums < totalNums:
            # left to right
            for i in matrix[left2right_row][0+offset:numCols-offset]:
                result.append(i)
                seenNums+=1
            offset+=1
            left2right_row+=1
            if seenNums==totalNums:
                break
            
            # top to bottom
            top2bottom_row = left2right_row
            top2bottom_col = numCols-offset
            while top2bottom_row < numRows-offset:
                row = matrix[top2bottom_row]
                result.append(row[top2bottom_col])
                seenNums+=1
                top2bottom_row+=1
            if seenNums==totalNums:
                break   
                
            # right to left
            right2left_row = top2bottom_row
            for i in reversed(matrix[right2left_row][0+offset-1:numCols-offset+1]):
                result.append(i)
                seenNums+=1
            if seenNums==totalNums:
                break
            
            
            # bottom to top
            bottom2top_row = right2left_row-1
            bottom2top_col = 0+offset-1
            while bottom2top_row >= left2right_row:
                result.append(matrix[bottom2top_row][bottom2top_col])
                bottom2top_row-=1
                seenNums+=1
            if seenNums==totalNums:
                break
            
        
        return result
    
if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    solver = Solution()
    result = solver.spiralOrder(matrix)
    print(result)


# In[ ]:




