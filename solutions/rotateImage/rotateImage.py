#!/usr/bin/env python
# coding: utf-8

# In[47]:


from typing import List

class Solution:
    def rotateListComprehension(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # [::] will modify the matrix in-place
        matrix[::] = [[row[i] for row in reversed(matrix)] for i in range(len(matrix))]
        
    def rotateZip(self, matrix: List[List[int]]) -> None:
        matrix[::] = [list(num) for num in zip(*reversed(matrix))]
     
    
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        clockwise rotate
        first reverse up to down, then swap the symmetry 
        1 2 3     7 8 9     7 4 1
        4 5 6  => 4 5 6  => 8 5 2
        7 8 9     1 2 3     9 6 3
        '''
        #reverse matrix upside down
        matrix[::] = matrix[::-1]
        #swap the symmetry
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().rotate(matrix)
    print(matrix)


# In[ ]:




