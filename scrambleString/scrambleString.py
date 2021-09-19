#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return self.helper(s1, s2, {})
        
    def helper(self, s1, s2, cache):
        if (s1, s2) in cache:
            return cache[(s1, s2)]
        else:
            if len(s1) != len(s2) or sorted(s1)!=sorted(s2):
                cache[(s1, s2)] = False
                return False
            if s1 == s2:
                cache[(s1, s2)] = True
                return True
            for i in range(1, len(s1)):
                cut = (self.helper(s1[:i], s2[:i], cache) and self.helper(s1[i:], s2[i:], cache))
                rotation = (self.helper(s1[:i], s2[-i:], cache) and self.helper(s1[i:], s2[:-i], cache))
                if cut or rotation:
                    return True
            cache[(s1, s2)] = False
            return False
        
if __name__ == '__main__':
    s1 = "abcd"
    s2 = "acbd"
    solver = Solution()
    print(solver.isScramble(s1, s2))


# In[ ]:




