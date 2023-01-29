#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List

class Solution:
    def setZeroesSpaceMN(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroLoc = list()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    zeroLoc.append((row, col))
        
        for loc in zeroLoc:
            row = loc[0]
            col = loc[1]
            
            # set row zero, go over each column
            for i in range(len(matrix[row])):
                matrix[row][i] = 0
            # set column zero, go over each row
            for j in range(len(matrix)):
                matrix[j][col] = 0
    
    def setZeroesSpaceMPlusN(self, matrix: List[List[int]]) -> None:
        # we do not need to store all the zeros in the matrix, but only 1 zero per row and per column
        zeroLoc = set()
        # per row
        row = 0
        while row < len(matrix):
            col = 0
            while col < len(matrix[row]):
                if matrix[row][col] == 0:
                    zeroLoc.add((row, col))
                    break
                col+=1
            row+=1
       
        # per column
        for colIdx, column in enumerate(zip(*matrix)):
            for rowIdx, val in enumerate(column):
                if val == 0:
                    zeroLoc.add((rowIdx, colIdx))
                    break
    
        for loc in zeroLoc:
            row = loc[0]
            col = loc[1]
            
            # set row zero, go over each column
            for i in range(len(matrix[row])):
                matrix[row][i] = 0
            # set column zero, go over each row
            for j in range(len(matrix)):
                matrix[j][col] = 0
    
    def setZeroesConstantSpace(self, matrix: List[List[int]]) -> None:
        # to see if there are zeros in the first col and row
        colZero = False
        rowZero = False
        
        numRows = len(matrix)
        numCols = len(matrix[0])
        # check if there are zeros in the first row
        for col in range(numCols):
            if matrix[0][col]==0:
                rowZero = True
                break
    
        # go over each cell
        for row in range(numRows):
            # check if there are zeros in the first column
            if matrix[row][0] == 0:
                colZero = True
            # if a cell is 0, change the first element in that row, that column to be 0
            for col in range(numCols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        # if there is only one line in matrix, start at row 0, otherwise row 1
        startRow = 0
        if len(matrix) > 1:
            startRow = 1
            
        # set to zeros
        for row in range(startRow, numRows):
            # iteration starting at row1, column 1 so we skip the first column and row  of the matrix
            for col in range(1, numCols):
                # if there is a zero either at the first element of the row or column
                if matrix[row][0]==0 or matrix[0][col]==0:
                    matrix[row][col] = 0
        
        
        # take care of the first column
        if colZero == True:
            # simply set all cells in the first column to be 0
            for row in range(numRows):
                matrix[row][0] = 0
            
        # set all cells in the first row to be 0 if there are 0's at the first row
        if rowZero == True:
            for col in range(numCols):
                matrix[0][col] = 0
        
        
    
if __name__ == '__main__':
    solver = Solution()
    matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
    solver.setZeroesConstantSpace(matrix)
    print(matrix)


# In[ ]:




