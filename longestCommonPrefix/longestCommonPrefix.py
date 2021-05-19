#!/usr/bin/env python
# coding: utf-8

# In[69]:


def longestCommonPrefixVertical(strs) -> str:
    result = ''
    minLen = min(strs, key=len)
    for i in range(len(minLen)):
        c = [word[i] for word in strs]
        if len(set(c)) == 1:
            result = strs[0][:i+1]
        else:
            break
    
    return result

def longestCommonPrefixZip(strs) -> str:
    result = ''
    for idx, columnTuple in enumerate(zip(*strs)):
        if len(set(columnTuple)) == 1:
            result = strs[0][:idx+1]
        else:
            break
    
    return result

def longestCommonPrefixZip2(strs) -> str:
    result = ''
    for idx, columnTuple in enumerate(zip(*strs)):
        if len(set(columnTuple)) > 1:
            return strs[0][:idx]

    return min(strs, key=len)


# In[70]:


if __name__ == "__main__":
    strs = ['ca', 'cire']
    print(longestCommonPrefixZip2(strs))


# In[ ]:




