#!/usr/bin/env python
# coding: utf-8

# In[9]:


from typing import List

class Solution:
    def uniquePathsWithObstaclesDFS(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) 
        n = len(obstacleGrid[0])
        result = self.dfs(m, n, 0, 0, obstacleGrid)
        return result
        
    def dfs(self, m, n, row, col, obstacleGrid):
        result = 0 
        if obstacleGrid[row][col] == 0:
            # reached the finish point
            if row == m - 1 and col == n - 1:
                result = 1
            else:
                if (col < n-1) and (obstacleGrid[row][col+1] == 0):
                    result += self.dfs(m, n, row, col+1, obstacleGrid)
                if (row < m-1) and (obstacleGrid[row+1][col] == 0):
                    result += self.dfs(m, n, row+1, col, obstacleGrid)
        return result
                    
    def uniquePathsWithObstaclesDP(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            numCol = len(obstacleGrid[0])
            numRow = len(obstacleGrid)
            
            # the path can only be taken from above or left
            # Number of ways of reaching the starting cell = 1
            obstacleGrid[0][0] = 1
            
            # first row, since there is no way above, we only need to check left cell
            # if there is a path from left cell, then there is also a path to current cell
            for col in range(1, numCol):
                # make sure this is not obstacle and there is a path from left
                if obstacleGrid[0][col] == 0:
                    if obstacleGrid[0][col-1] == 1:
                        # 1 here means number of path instead of obstacle
                        obstacleGrid[0][col] = 1
                else:
                    # this cell is a obstacle, change it to 0 which stands for 0 path
                    obstacleGrid[0][col] = 0
                    
            # first column, there is no way from left, only need to check above
            for row in range(1, numRow):
                if obstacleGrid[row][0] == 0:
                    if obstacleGrid[row-1][0] == 1:
                        # 1 here means number of path instead of obstacle
                        obstacleGrid[row][0] = 1
                else:
                    obstacleGrid[row][0] = 0
                    
            # start
            for row in range(1, numRow):
                for col in range(1, numCol):
                    if obstacleGrid[row][col] == 0:
                        # this is a free cell, number of paths reaching to this cell is equal to sum of number
                        # of paths from above and left of it
                        obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]
                    else:
                        # this is an obstacle, which means no path can be reached
                        obstacleGrid[row][col] = 0
        
        return obstacleGrid[-1][-1]
            
    
        
if __name__ == '__main__':
    obstacleGrid = [[0,0,1,0],[0,0,0,0], [1,1,1,0],[0,0,0,0]]
    solver = Solution()
    print(solver.uniquePathsWithObstaclesDP(obstacleGrid))


# In[ ]:




