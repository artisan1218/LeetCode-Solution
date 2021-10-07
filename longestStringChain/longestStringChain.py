#!/usr/bin/env python
# coding: utf-8

# In[31]:


from typing import List

class Solution:
    def longestStrChainDP(self, words: List[str]) -> int:
        dp = {}
        result = 1

        for word in sorted(words, key=len):
            dp[word] = 1
            # go through each possible predecessor word
            for i in range(len(word)):
                pred = word[:i] + word[i + 1:] 
                if pred in dp:
                    dp[word] = dp[pred] + 1
                    result = max(result, dp[word])

        return result
    
    def longestStrChainDFS(self, words: List[str]) -> int:
        
        def dfs(word):
            if word in dp: 
                return dp[word]
            else:
                ans = 1
                # go through each predecessor
                for i in range(len(word)):
                    pred = word[:i] + word[i + 1:]
                    if pred in words_set:
                        ans = max(1 + dfs(pred), ans)
                dp[word] = ans
                return ans
        
        ans = 0
        words_set =set(words)
        dp = {}    
        # go through each word and compute word chain separately
        for word in words:
            ans = max(ans, dfs(word))
        return ans
    
if __name__ == '__main__':
    solver = Solution()
    words = ["a","b","ba","bca","bda","bdca"]
    result = solver.longestStrChainDFS(words)
    print(result)


# In[ ]:




