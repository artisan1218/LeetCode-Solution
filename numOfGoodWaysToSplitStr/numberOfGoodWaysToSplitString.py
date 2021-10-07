#!/usr/bin/env python
# coding: utf-8

# In[39]:


class Solution:
    def numSplitsBruteForce(self, s: str) -> int:
        def isGoodWay(p, q):
            return len(set(p)) == len(set(q))
        
        count = 0
        for i in range(1, len(s)):
            print(s[0:i], s[i:])
            if isGoodWay(s[0:i], s[i:]):
                count+=1
        return count
    
    def numSplitsCache1(self, s: str) -> int:
        leftUnique = dict()    
        rightUnique = dict()    
        leftSeen = set()
        rightSeen = set()
        sLen = len(s)
        for i in range(0, len(s)):
            if s[i] not in leftSeen:
                leftSeen.add(s[i])
                leftUnique[i] = leftUnique.get(i-1, 0) + 1
            else:
                leftUnique[i] = leftUnique[i-1]
                
            if s[sLen-i-1] not in rightSeen:
                rightSeen.add(s[sLen-i-1])
                rightUnique[sLen-i-1] = rightUnique.get(sLen-i, 0) + 1
            else:
                rightUnique[sLen-i-1] = rightUnique[sLen-i]
        
        count = 0
        for i in range(0, len(s)-1):
            if leftUnique[i] == rightUnique[i+1]:
                count+=1
        
        return count
    
    def numSplitsCache2(self, s: str) -> int:
        leftUnique = list()    
        rightUnique = list()    
        leftSeen = set()
        rightSeen = set()
        sLen = len(s)
        for i in range(0, len(s)):
            leftSeen.add(s[i])
            rightSeen.add(s[sLen-i-1])
            leftUnique.append(len(leftSeen))
            rightUnique.append(len(rightSeen))
            
        count = 0
        for i in range(0, len(s)-1):
            if leftUnique[i] == rightUnique[sLen-i-2]:
                count+=1
        
        return count
        
if __name__ == '__main__':
    solver = Solution()
    s = "aacaba"
    ways = solver.numSplitsCache2(s)
    print(ways)

