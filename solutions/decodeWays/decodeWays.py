#!/usr/bin/env python
# coding: utf-8

# In[45]:


class Solution:
    def numDecodings(self, s: str) -> int:
        return self.dfs(s, 0, dict())
    
    def dfs(self, s, i, cache):
        # we have reached the end of s, this is a valid solution
        if i==len(s):
            return 1
        else:
            result=0
            if s[i]!='0': # single digit
                # memorization
                if s[i+1:] not in cache:
                    cache[s[i+1:]] = self.dfs(s, i+1, cache)
                result += cache[s[i+1:]]
                
            # two digits, either start with 1 or start with 2 and second digit is smaller or equal than 6
            if i+1<len(s) and (s[i]=='1' or (s[i]=='2' and ord(s[i+1]) <= ord('6'))):
                # memorization
                if s[i+2:] not in cache:
                    cache[s[i+2:]] = self.dfs(s, i+2, cache)
                result += cache[s[i+2:]]
                    
            return result
        
    def numDecodingsDP1(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        
        if s[0]!='0':
            dp[0] = 1
        
        for i in range(1, len(s)):
            if s[i]!='0':
                dp[i] += dp[i-1]
            
            if s[i-1]=='1' or (s[i-1]=='2' and ord(s[i])<=ord('6')):
                if i-2>=0:
                    dp[i] += dp[i-2]
                else:
                    dp[i] += 1
        
        return dp[-1]
        
    def numDecodingsDP2(self, s: str) -> int:
        left = 1 
        right = 1 if s[0]!='0' else 0
        
        for i in range(1, len(s)):
            newRight = 0
            if s[i]!='0':
                newRight = right
            
            if s[i-1]=='1' or (s[i-1]=='2' and ord(s[i])<=ord('6')):
                newRight += left
            left, right = right, newRight
        
        return right
        
if __name__ == '__main__':
    solver = Solution()
    s = "112"
    result = solver.numDecodingsDP2(s)
    print(result)


# In[ ]:




