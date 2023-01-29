#!/usr/bin/env python
# coding: utf-8

# In[5]:


from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        numRow = len(grid)
        numCol = len(grid[0])
        
        # sum up the first row
        for col in range(1, numCol):
            grid[0][col] += grid[0][col-1]
            
        # sum up first column
        for row in range(1, numRow):
            grid[row][0] += grid[row-1][0]
            
        # dp part
        for row in range(1, numRow):
            for col in range(1, numCol):
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        
        return grid[-1][-1]
    
if __name__ == "__main__":
    solver = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    minSum = solver.minPathSum(grid)
    print(minSum)


# In[ ]:




