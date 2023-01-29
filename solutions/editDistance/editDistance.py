#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # set up the dp matrix
        dp = [[0] * (len(word1)+1) for _ in range((len(word2)+1))]
        
        # change from '' to '' requires 0 edit
        dp[0][0] = 0
        
        # fill in first row
        for col in range(1, len(word1)+1):
            dp[0][col] = col
            
        # fill in first column
        for row in range(1, len(word2)+1):
            dp[row][0] = row
        
        # start dp
        for row in range(1, len(word2)+1):
            for col in range(1, len(word1)+1):
                if word1[col-1] == word2[row-1]:
                    # no need to edit if the current elements are same
                    dp[row][col] = dp[row-1][col-1]
                else:
                    # if current elements are not the same, the min edit distance will be the minimum edit distance
                    # from three neighbors plus 1
                    dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
        
        return dp[-1][-1]
        
if __name__ == "__main__":
    solver = Solution()
    word1 = "horse"
    word2 = "ros"
    print(solver.minDistance(word1, word2))


# In[ ]:




