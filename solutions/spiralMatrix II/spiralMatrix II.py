#!/usr/bin/env python
# coding: utf-8

# In[43]:


from typing import List
import math

class Solution:
    
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[1 for i in range(n)] for i in range(n)]
        numRows = len(matrix)
        numCols = len(matrix[0])
        totalNums = n**2
        seenNums = 0
        
        left2right_row = 0
        offset = 0
        while seenNums < totalNums:
            # left to right
            for i in range(offset, len(matrix[left2right_row])-offset):
                matrix[left2right_row][i] = seenNums+1
                seenNums+=1
            offset+=1
            left2right_row+=1
            if seenNums==totalNums:
                break

            # top to bottom
            top2bottom_row = left2right_row
            top2bottom_col = numCols-offset
            while top2bottom_row < numRows-offset:
                matrix[top2bottom_row][top2bottom_col] = seenNums+1
                seenNums+=1
                top2bottom_row+=1
            if seenNums==totalNums:
                break   
                
            # right to left
            right2left_row = top2bottom_row
            for i in reversed(range(0+offset-1, numCols-offset+1)):
                matrix[right2left_row][i] = seenNums+1    
                seenNums+=1
            if seenNums==totalNums:
                break
        
            
            # bottom to top
            bottom2top_row = right2left_row-1
            bottom2top_col = 0+offset-1
            while bottom2top_row >= left2right_row:
                matrix[bottom2top_row][bottom2top_col] = seenNums+1
                bottom2top_row-=1
                seenNums+=1
            if seenNums==totalNums:
                break
                
        return matrix
    
    def generateMatrixWalkSpiral(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        row, col, row_direction, col_direction = 0, 0, 0, 1
        for num in range(n**2):
            matrix[row][col] = num + 1
            # matrix[(row+di)%n][(col+dj)%n] checks if the next element is already added
            # the next element means the next element that we will meet in matrix if keep straight
            # if the element has value greater than 0, then we should make a right turn
            # by exchaning the row and col direction
            if matrix[(row+row_direction)%n][(col+col_direction)%n] >0:
                row_direction, col_direction = col_direction, -row_direction
            row += row_direction
            col += col_direction
        return matrix
        
    
if __name__ == '__main__':
    n = 5
    solver = Solution()
    result = solver.generateMatrixWalkSpiral(n)
    print(result)


# In[ ]:




