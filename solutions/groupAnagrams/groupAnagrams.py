#!/usr/bin/env python
# coding: utf-8

# In[42]:


from typing import List

class Solution:
    def groupAnagramsSort(self, strs: List[str]) -> List[List[str]]:
        
        result = {}
        for word in strs:
            # all anagrams will have same value of sortedWord, so we can put them in a dict
            sortedWord = tuple(sorted(word))
            result[sortedWord] = result.get(sortedWord, []) + [word]
            
        return list(result.values())
    
    def groupAnagramsCount(self, strs: List[str]) -> List[List[str]]:
        
        result = {}
        for word in strs:
            count = [0] * 26
            # count the occurence of each letter instead of sorting
            for char in word:
                count[ord(char)-ord('a')] += 1
            # convert type list to tuple to hash in dict
            result[tuple(count)] = result.get(tuple(count), []) + [word]
        
        return list(result.values())
    
if __name__ == "__main__":
    solver = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(solver.groupAnagramsCount(strs))


# In[ ]:




