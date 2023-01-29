#!/usr/bin/env python
# coding: utf-8

# In[32]:


def solution(S):
    cost = 0
    firstIdx = S.find('b') 
    lastIdx = S.rfind('b') # rfind to get last index of b
    lenS = len(S)
    if firstIdx==-1 and lastIdx==-1:
        return 0
    else:
        optionOne = S[:firstIdx] + S[firstIdx+1:] # pop from center
        optionTwo = S[firstIdx+1:] # pop left from side
        optionThree = S[:lastIdx] # pop right from side
        cost += min(solution(optionOne)+2, solution(optionTwo)+firstIdx+1, solution(optionThree)+lenS-lastIdx)
        return cost


# In[35]:


S = "aaabaaa"

print(solution(S))

