#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.min = float('inf')
        self.next = None
        self.prev = None
        
class minStack:
    def __init__(self):
        self.topNode = ListNode()
        self.begin = self.topNode
        
    def push(self, val):
        newVal = ListNode(val)
        if val < self.topNode.min:
            newVal.min = val
        else:
            newVal.min = self.topNode.min
        self.topNode.next = newVal
        newVal.prev = self.topNode
        self.topNode = self.topNode.next
        
    def pop(self):
        result = self.topNode
        self.topNode = self.topNode.prev
        self.topNode.next = None
        result.prev = None
        return result.val
        
    def top(self):
        return self.topNode.val
        
    def getMin(self):
        return self.topNode.min
        


# In[ ]:




