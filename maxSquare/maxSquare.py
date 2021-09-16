#!/usr/bin/env python
# coding: utf-8

# In[25]:


from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxSide = 0
        
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        # init first row and first column
        for col in range(len(matrix[0])):
            if matrix[0][col]=='1':
                dp[0][col]=1
                maxSide = 1
        for row in range(len(matrix)):
            if matrix[row][0]=='1':
                dp[row][0]=1
                maxSide = 1
                
        # dp starts here. Each new cell in dp in dependent on the minimal value of the three neightbors around it.
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
                if matrix[row][col]=='1':
                    dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
                else:
                    dp[row][col] = 0
                maxSide = max(maxSide, dp[row][col])
        
        return maxSide**2
    
if __name__ == '__main__':
    solver = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(solver.maximalSquare(matrix))


# In[ ]:




