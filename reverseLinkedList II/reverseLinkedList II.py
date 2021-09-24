#!/usr/bin/env python
# coding: utf-8

# In[48]:


# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        
        # find linkedlist on the left-side(pre) and right-side(suf) of left and right
        count = 1
        pre = sentinel
        while count!=left:
            pre = pre.next
            count+=1
        
        count = 0
        suf = head
        while count!=right:
            suf = suf.next
            count+=1
        
        # reverse left to right
        revHead = suf
        cursor = pre.next
        while cursor!=suf:
            nextNode = cursor.next
            cursor.next = revHead
            revHead = cursor
            cursor = nextNode

        # connect pre
        pre.next = revHead

        return sentinel.next

            
        
if __name__ == '__main__':
    solver = Solution()
    
    l = [1,2,3,4,5]
    left = 2
    right = 4
    head = ListNode()
    cursor = head
    for i in l:
        cursor.next = ListNode(i)
        cursor = cursor.next

    result = solver.reverseBetween(head.next, left, right)
        
    while result!=None:
        print(result.val)
        result = result.next


# In[ ]:




