#!/usr/bin/env python
# coding: utf-8

# In[54]:


def longestCommonPrefix(strs) -> str:
    result = ''
    minLen = min(strs, key=len)
    for i in range(len(minLen)):
        c = [word[i] for word in strs]
        if len(set(c)) == 1:
            result = strs[0][:i+1]
        else:
            break
    
    return result


# In[56]:


if __name__ == "__main__":
    strs = ['car', 'cir']
    print(longestCommonPrefix(strs))


# In[ ]:




