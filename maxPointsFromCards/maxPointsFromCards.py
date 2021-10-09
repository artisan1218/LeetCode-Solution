#!/usr/bin/env python
# coding: utf-8

# In[46]:


from typing import List

class Solution:
    def maxScoreDFS(self, cardPoints: List[int], k: int) -> int:
        def dfs(cardPoints, k, l, r):
            if k==0:
                return 0
            else:
                left = cardPoints[l] + dfs(cardPoints, k-1, l+1, r) # take from left
                right = cardPoints[r] + dfs(cardPoints, k-1, l, r-1) # take from right
                return max(left, right)
        
        return dfs(cardPoints, k, 0, len(cardPoints)-1)
    
    def maxScoreIteration(self, cardPoints: List[int], k: int) -> int:
        result = 0
        for leftNum in range(k+1):
            rightNum = k-leftNum
            result = max(result, sum(cardPoints[:leftNum])+sum(cardPoints[len(cardPoints)-rightNum:]))
            
        return result
    
    def maxScoreIteration2(self, cardPoints: List[int], k: int) -> int:
        l2r = [0]
        r2l = [sum(cardPoints)]
        for idx, point in enumerate(cardPoints):
            l2r.append(l2r[-1] + point)
            r2l.append(r2l[-1] - point)
        
        result = 0
        for leftNum in range(k+1):
            rightNum = k-leftNum
            result = max(result, l2r[leftNum]+r2l[len(cardPoints)-rightNum])
            
        return result
    
    def maxScoreSlidingWindow(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints)-k
        result = sum(cardPoints[right:])
        curSum = sum(cardPoints[right:])

        for _ in range(right, len(cardPoints)):
            # move the sliding window to right by one pos
            curSum = curSum - cardPoints[right] + cardPoints[left]
            result = max(result, curSum)
            left+=1
            right+=1
        return result
            
        
if __name__ == '__main__':
    solver = Solution()
    cardPoints = [1,79,80,1,1,1,200,1]
    k = 3
    print(solver.maxScoreSlidingWindow(cardPoints, k))
    


# In[ ]:




