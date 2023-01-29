#!/usr/bin/env python
# coding: utf-8

# In[27]:


from typing import List

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        cols = len(targetPath)
        # construct graph
        adj = [[] for _ in range(n)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
        
        '''
        dp will be initialized to this, first element in tuple stands for edit distance, second element is the path
        dp[i][j] means the minimum edit distance w/ path ending at node i and targetPath ending at j
        [[(inf, []), (inf, []), (inf, []), (inf, [])], 
         [(inf, []), (inf, []), (inf, []), (inf, [])], 
         [(inf, []), (inf, []), (inf, []), (inf, [])], 
         [(inf, []), (inf, []), (inf, []), (inf, [])], 
         [(inf, []), (inf, []), (inf, []), (inf, [])]]
        '''
        dp = [[(float('inf'), []) for _ in range(cols)] for _ in range(n)]
 
        # update dp column by column from left to right
        for c in range(cols):
            for r in range(n):
                editDist = int(names[r] != targetPath[c])
                if c == 0: 
                    # for the first column, the edit distance will simply be 0 if first name
                    # matches with the first name in targetPath, otherwise 1
                    dp[r][c] = (editDist, [r])
                else:
                    # get all names connected with current name, then pick the smallest one
                    prevEditDistance, prePath = min(dp[k][c-1] for k in adj[r])
                    dp[r][c] = (prevEditDistance + editDist, prePath+[r])
        
        return min(dp[r][-1] for r in range(n))[1]
        
        
if __name__ == '__main__':
    solver = Solution()
    n = 5
    roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]]
    names = ["ATL","PEK","LAX","DXB","HND"]
    targetPath = ["ATL","DXB","HND","LAX"]
    result = solver.mostSimilar(n, roads, names, targetPath)
    print(result)


# In[ ]:




