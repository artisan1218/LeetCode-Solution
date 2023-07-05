#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        def helper(dungeon, x, y, minHP, curHP):
            if x<len(dungeon) and y<len(dungeon[x]):
                # reached the bottom-right corner
                if x==len(dungeon)-1 and y==len(dungeon[x])-1:
                    curHP += dungeon[x][y]
                    minHP = min(minHP, curHP)
                    self.result = max(self.result, minHP)
                else:
                    curHP += dungeon[x][y]
                    minHP = min(minHP, curHP)
                    if curHP < self.result:
                        return
                    helper(dungeon, x, y+1, minHP, curHP) # rightward
                    helper(dungeon, x+1, y, minHP, curHP) # downward
                    
        self.result = float('-inf')
        helper(dungeon, 0, 0, 0, 0)
        return abs(self.result)+1
    
    def calculateMinimumHPDP(self, dungeon: List[List[int]]) -> int:
        # dp[x][y] = minimum HP needed at this cell to get to princess
        # we trace back from princess to starting point
        dp = [[0 for i in range(len(dungeon[0]))] for i in range(len(dungeon))]
        dp[-1][-1] = max(1 - dungeon[-1][-1], 1)
        
        # since we can only go rightward or downward, when tracing back, we can only go leftward or upward
        # fill in last row from right to left
        for y in range(len(dungeon[-1])-2, -1, -1):
            dp[-1][y] = max(dp[-1][y+1] - dungeon[-1][y], 1)
            
        # fill in last column from bottom to top
        for x in range(len(dungeon)-2, -1, -1):
            dp[x][-1] = max(dp[x+1][-1] - dungeon[x][-1], 1)
            
        # dp
        for x in range(len(dungeon)-2, -1, -1):
            for y in range(len(dungeon[x])-2, -1, -1):
                right = max(dp[x][y+1] - dungeon[x][y], 1)
                down = max(dp[x+1][y] - dungeon[x][y], 1)
                dp[x][y] = min(right, down)
            
        return dp[0][0]
        
        
solver = Solution()
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(solver.calculateMinimumHPDP(dungeon))


# In[ ]:




