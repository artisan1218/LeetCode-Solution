#!/usr/bin/env python
# coding: utf-8

# In[28]:


class Solution:
    def numDistinctBacktrack(self, s: str, t: str) -> int:
        def helper(s, t, si, ti):
            result = 0
            if ti==len(t):
                return 1
            else:
                for i in range(si, len(s)):
                    if s[i] == t[ti]:
                        result += helper(s, t, i+1, ti+1)
                return result
        
        return helper(s, t, 0, 0)
                                 
    def numDistinctDFS(self, s: str, t: str) -> int:
        mem = dict()
        
        def dfs(si, ti):
            if (si, ti) in mem:
                return mem[(si, ti)]
            else:
                if ti==len(t):
                    return 1
                elif si==len(s):
                    return 0
                else:
                    if s[si]==t[ti]:
                        mem[(si, ti)] = dfs(si+1, ti+1) + dfs(si+1, ti)
                    else:
                        mem[(si, ti)] = dfs(si+1, ti)
                    return mem[(si, ti)]
        
        return dfs(0, 0)
    
    def numDistinctDP(self, s: str, t: str) -> int:
        dp = [[0] * (len(s)+1) for _ in range(len(t) + 1)]
        
        for i in range(len(s)+1):
            dp[0][i] = 1
        
        for row in range(1, len(t)+1):
            for col in range(1, len(s)+1):
                if t[row-1]==s[col-1]:
                    dp[row][col] = dp[row][col-1] + dp[row-1][col-1]
                else:
                    dp[row][col] = dp[row][col-1]
        return dp[-1][-1]
    

if __name__ == '__main__':
    solver = Solution()
    s = "babgbag"
    t = "bag"
    result = solver.numDistinctDP(s, t)
    print(result)


# In[ ]:




