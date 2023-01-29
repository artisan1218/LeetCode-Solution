#!/usr/bin/env python
# coding: utf-8

# In[23]:


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
    def deleteDuplicates1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-101, head)
        pred = sentinel # predecessor
        
        while head!=None:
            if head.val!=pred.val:
                pred.next = head
                pred = pred.next
                head = head.next
                pred.next = None
            else:
                head = head.next
            
        return sentinel.next
    
    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur!=None:
            while cur.next!=None and cur.val==cur.next.val:
                cur.next = cur.next.next # skip one duplicate a time, skip all duplicates after the loop
            cur = cur.next # move the pointer to a new pos
        
        return head
    
    def deleteDuplicates3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        else:
            head.next = self.deleteDuplicates3(head.next)
            if head.val == head.next.val:
                return head.next
            else:
                return head
        
if __name__ == '__main__':
    solver = Solution()
    
    l = [1,2, 3, 3,3, 4,4,4,4]
    head = ListNode()
    cursor = head
    for i in l:
        cursor.next = ListNode(i)
        cursor = cursor.next

    result = solver.deleteDuplicates3(head.next)
        
    while result!=None:
        print(result.val)
        result = result.next


# In[ ]:




