#!/usr/bin/env python
# coding: utf-8

# In[132]:


from functools import lru_cache

class Solution:
    @lru_cache()
    def isInterleaveBacktrack(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)==0 and len(s2)==0 and len(s3)==0:
            return True
        elif len(s1)+len(s2)!=len(s3):
            return False
        else:
            res1 = False
            for i in range(1, len(s1)+1):
                if s1[:i]==s3[:i]:
                    res1 = self.isInterleave(s1[i:], s2, s3[i:])
                    if res1==True:
                        return True
                    else:
                        break
                else:
                    break
            
            res2 = False
            for i in range(1, len(s2)+1):
                if s2[:i]==s3[:i]:
                    res2 = self.isInterleave(s1, s2[i:], s3[i:])
                    if res2==True:
                        return True
                    else:
                        break
                else:
                    break

            return res1 or res2
        
    def isInterleaveDP1(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def dfs(i, j):
            if i==len(s1) and j==len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i<len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                return True
            if j<len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True
            
            dp[(i, j)] = False
            return False
        
        if len(s1)+len(s2)!=len(s3):
            return False
        else:
            return dfs(0, 0)
        
    def isInterleaveDP2(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1)+len(s2)!=len(s3):
            return False
        else:
            dp = [[False for _ in range(len(s1)+1)] for _ in range((len(s2)+1))]  
            dp[0][0] = True

            # initialize first row
            for i in range(len(s1)):
                if s1[i] == s3[i] and dp[0][i]==True:
                    dp[0][i+1] = True

            # initialize first column
            for i in range(len(s2)):
                if s2[i] == s3[i] and dp[i][0]==True:
                    dp[i+1][0] = True

            for row in range(1, len(s2)+1):
                for col in range(1, len(s1)+1):
                    if s1[col-1] == s3[row+col-1] and dp[row][col-1] == True:
                        dp[row][col] = True

                    if s2[row-1] == s3[row+col-1] and dp[row-1][col] == True:
                        dp[row][col] = True

            return dp[-1][-1]
        
            
if __name__ == '__main__':
    solver = Solution()
    s1 = "db"
    s2 = "b"
    s3 = "cbb"
    print(solver.isInterleaveDP2(s1, s2, s3))


# In[ ]:




