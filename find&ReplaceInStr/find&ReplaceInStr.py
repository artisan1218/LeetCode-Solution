#!/usr/bin/env python
# coding: utf-8

# In[42]:


from typing import List

class Solution:
    def findReplaceStringLeftToRight(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        pre = 0
        # sort the three tuple in acsending order 
        # so that pre is always the difference between source and target
        for idx, source, target in sorted(zip(indices, sources, targets)):
            # check if source exists at index idx
            if source == s[idx+pre:idx+len(source)+pre]:
                s = s[0:idx+pre] + target + s[idx+pre+len(source):]
                pre += len(target)-len(source)
        return s
    
    def findReplaceStringRightToLeft(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # going from right to left does not require maintaining the delta length between source and target
        for idx, src, tgt in sorted(zip(indices, sources, targets), reverse=True):
            if s[idx:idx+len(src)] == src: # if s[idx:].startswith(src):
                s = s[0:idx] + tgt + s[idx+len(src):]
        return s
        
    def findReplaceStringPieceTable(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        table = dict()
        for i in range(len(indices)):
            if s[indices[i]:].startswith(sources[i]):
                table[indices[i]] = i
        
        result = list()
        i = 0
        while i<len(s):
            if i in table:
                result.append(targets[table[i]])
                i += len(sources[table[i]])
            else:
                result.append(s[i])
                i += 1
        return ''.join(result)
        
if __name__ == '__main__':
    solver = Solution()
    s = "vmokgggqzp"
    indices = [3,5,1]
    sources = ["kg","ggq","mo"]
    targets = ["s","so","bfr"]
    result = solver.findReplaceStringPieceTable(s, indices, sources, targets)
    print(result)


# In[ ]:




