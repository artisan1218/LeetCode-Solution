#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        sentinel = ListNode(-101, head)
        l = sentinel
        check = head
        rList = []
        
        # connect all nodes that are smaller than x
        # and store references of nodes that are greater than x
        while check!=None:
            if check.val < x:
                l.next = check
                l = l.next
                check = check.next
            else:
                rList.append(check)
                check = check.next
        
        # connect all nodes that are greater than x
        for node in rList:
            l.next = node
            l = l.next
            
        # disconnecting the last node to prevent circling
        l.next=None
        
        return sentinel.next
    
    def partitionTwoPointers(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        # beforeHead and afterHead are two pointers represent the nodes smaller than x and greater than x
        beforeHead = before = ListNode(0)
        afterHead = after = ListNode(0)
        
        while head!=None:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        
        # cut the circle
        after.next = None
        # connecting two parts
        before.next = afterHead.next
        
        return beforeHead.next
        
        
if __name__ == '__main__':
    solver = Solution()
    l = [1,4,3,2,5,2]
    x = 3
    
    head = ListNode()
    cursor = head
    for i in l:
        cursor.next = ListNode(i)
        cursor = cursor.next
        
    result = solver.partitionTwoPointers(head.next, x)
        
    while result!=None:
        print(result.val)
        result = result.next


# In[ ]:




