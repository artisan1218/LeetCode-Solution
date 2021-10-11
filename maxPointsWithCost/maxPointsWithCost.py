#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List

class Solution:
    def maxPointsBruteForce(self, points: List[List[int]]) -> int:
        rows = len(points)
        cols = len(points[0])
        
        pre = points[0].copy()
        dp = points[0].copy()
        for r in range(1, rows): # starting at the second row
            for c in range(0, cols): # for each of the element in this rwo
                for k in range(len(pre)): # go through each previous elements and update dp accordingly
                    dp[c] = max(dp[c], points[r][c]+pre[k]-abs(k-c))
            pre = dp.copy()
        return max(dp)
                      
    def maxPointsDP(self, points: List[List[int]]) -> int:                  
        rows = len(points)
        cols = len(points[0])
        
        dp = points[0]
        left = [0] * cols
        right = [0] * cols
        
        for r in range(1, rows):
            for c in range(cols):
                if c==0:
                    left[c] = dp[c]
                else:
                    # the key is we decrement the left value by 1 each time and compare it with the value
                    # right above c to pick the larger one.
                    left[c] = max(left[c-1]-1, dp[c]) 
            for c in range(cols-1, -1, -1):
                if c==cols-1:
                    right[c] = dp[c]
                else:
                    right[c] = max(right[c+1]-1, dp[c])
            # for the current level dp, calculate the sum by adding current value and the larger value
            # from either left scan or right scan.
            for c in range(cols):
                dp[c] = points[r][c] + max(left[c], right[c])
        return max(dp)
                
        
if __name__ == '__main__':
    solver = Solution()
    points = [[1,2,3],[1,5,1],[3,1,1]]
    result = solver.maxPointsDP(points)
    print(result)


# In[ ]:




