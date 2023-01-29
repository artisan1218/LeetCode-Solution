#!/usr/bin/env python
# coding: utf-8

# In[42]:


from typing import List

class Solution:
    def searchMatrixColRow(self, matrix: List[List[int]], target: int) -> bool:
        # since the matrix is sorted
        # first check column
        numRows = len(matrix)
        numCols = len(matrix[0]) # matrix has at least 1 row
        
        # found the row number of target
        targetRowIdx = 0
        for row in range(numRows):
            if matrix[row][0] <= target:
                targetRowIdx = row
            else:
                break
        
        # found the correct column number
        for col in range(numCols):
            if matrix[targetRowIdx][col] == target:
                return True
        
        # not found after searching all numbers in this row
        return False
    
    def searchMatrixBinarySearch(self, matrix: List[List[int]], target: int) -> bool:
        # treat the sorted matrix as a list
        # apply binary search on the sorted list to find the target
        
        # length of the sorted list if consider matrix as a list
        totalLen = len(matrix) * len(matrix[0])
        rowLen = len(matrix[0])
        
        left = 0
        right = totalLen - 1
        while left <= right:
            middle = (left + right) // 2
            row, col = middle//rowLen, middle%rowLen
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                right = middle - 1
            else:
                left = middle + 1
        
        return False


# In[43]:


if __name__ == '__main__':
    solver = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(solver.searchMatrixBinarySearch(matrix, target))

