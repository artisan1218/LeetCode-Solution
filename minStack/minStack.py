#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.min = float('inf')
        self.next = None
        self.prev = None
        
class minStackDoublyLinkedList:
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
        
        
        
class minStackTwoStack:
    def __init__(self):
        self.stack = list()
        self.min = list()
        
    def push(self, val):
        self.stack.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        else:
            self.min.append(min(self.min[-1], val))
        
    def pop(self):
        self.min.pop()
        return self.stack.pop()
        
    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.min[-1]
        

