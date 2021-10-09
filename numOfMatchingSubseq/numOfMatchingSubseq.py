#!/usr/bin/env python
# coding: utf-8

# In[22]:


from typing import List
from collections import defaultdict
 
class Solution:
    def numMatchingSubseqBruteForce(self, s: str, words: List[str]) -> int:
        def match(subsq, s):
            j = 0
            for i in range(len(s)):
                if s[i] == subseq[j]:
                    j+=1
                if j==len(subseq):
                    return True
            return False
        
        count = dict()
        for subseq in words:
            count[subseq] = count.get(subseq, 0) + 1
        
        result = 0
        for subseq in count:
            if match(subseq, s):
                result+=count[subseq]
        return result
    
    def numMatchingSubseqBinarySearch(self, s: str, words: List[str]) -> int:
        def binarySearch(lst, tgt):
            l = 0
            r = len(lst)
            while l<r:
                mid = (l+r)//2
                if lst[mid] > tgt:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        lookup = defaultdict(list)
        for idx, char in enumerate(s):
            lookup[char].append(idx)
        
        result = 0
        for word in words:
            start = -1
            found = True
            for char in word:
                tgtIdx = binarySearch(lookup[char], start)
                if tgtIdx == len(lookup[char]):
                    found = False
                    break
                else:
                    start = lookup[char][tgtIdx]
            if found:
                result+=1
        return result
        
    
    def numMatchingSubseqNextPointer(self, s: str, words: List[str]) -> int:
        pointerDict = defaultdict(list)
        for word in words:
            pointerDict[word[0]].append(word[1:])
            
        result = 0    
        for char in s:
            waitingList = pointerDict[char]
            pointerDict[char] = []
            for suffix in waitingList:
                if len(suffix)==0: # we have reached the end of current word
                    result += 1
                else:
                    # update the dict with new char and its suffix
                    pointerDict[suffix[0]].append(suffix[1:])
        return result
        
        
if __name__ == '__main__':
    solver = Solution()
    s = "abcde"
    words = ["a","bb","acd","ace"]
    result = solver.numMatchingSubseqBinarySearch(s, words)
    print(result)


# In[ ]:




