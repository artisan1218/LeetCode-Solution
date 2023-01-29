#!/usr/bin/env python
# coding: utf-8

# In[128]:


from collections import Counter

class Solution:
    
    def validSubstr(self, substr, tCount):
            tCopy = tCount.copy()
            tLen = sum(tCount.values())
            for check in substr:
                if tCopy.get(check, 0)>0:
                    tLen-=1
                    tCopy[check]-=1
            return tLen==0
    
    def minWindowBruteForce(self, s: str, t: str) -> str:
        tCount = dict()
        for char in t:
            if char not in tCount.keys():
                tCount[char] = 1
            else:
                tCount[char] += 1
        
        minLen = float('inf')
        minLenWindow = ''
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                curSubstr = s[i:j]
                if len(curSubstr)>=len(t):
                    if self.validSubstr(curSubstr, tCount):
                        if len(curSubstr) < minLen:
                            minLen = len(curSubstr)
                            minLenWindow = curSubstr
        return minLenWindow      
        
    def minWindowTwoPointers(self, s: str, t: str) -> str:
        # current number elements
        window = dict()
        
        # count the number of occurence of char in t
        tCount = dict()
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
        
        # have is the number of char we have, need is the number of char we need to match t
        have = 0
        need = len(set(t))
        result = ''
        minLen = float('inf')
        left = 0
        for right in range(len(s)):
            curChar = s[right]
            window[curChar] = 1 + window.get(curChar, 0)

            if curChar in tCount.keys() and window[curChar] == tCount[curChar]:
                # we have found one element that we need
                have += 1
      
            # if we have found all elements we need, we can record the substring
            while have == need:
                # update min window and result
                curLen = right-left+1
                if curLen < minLen:
                    minLen = curLen
                    result = s[left:right+1]
            
                # shorten the current substring by shift left pointer to right because the current substring
                # may contain unnecessary elements on the left
                # left elements are all seen elements, so no need to check existence
                window[s[left]] -= 1
                
                # if the removed element is what we need, we can stop and continuing move right pointer to right
                # to discover more element
                # if the removed element is not in tCount, that means we can remove it since we do not need it
                if s[left] in tCount.keys() and window[s[left]] < tCount[s[left]]:
                    have -= 1
                
                # shift left pointer to right by one to shorten the substring
                left+=1
        
        return result
    
        
if __name__ == '__main__':
    solver = Solution()
    s = "aa"
    t = "aa"
    print('result:', solver.minWindowTwoPointers(s, t))


# In[ ]:




