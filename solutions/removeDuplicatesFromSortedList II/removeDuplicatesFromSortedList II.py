#!/usr/bin/env python
# coding: utf-8

# In[19]:


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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        pred = sentinel # predecessor
        
        while head!=None:
            if head.next!=None and head.val==head.next.val:
                # we have duplicates, should skip this sublist
                while head.next!=None and head.val==head.next.val:
                    # repeatedly skip duplicates value
                    head = head.next
                # we have skiped this duplicates sublist, we can temporarily move 'next' pointer of pred here
                # but since we don't know if there are more duplicates upfront, don't move pointer of pred itself here
                # 3 3 4 4, we have skiped 3 3, but don't know how many 4's are there
                pred.next = head.next                
            else:
                # next two values are not the same, we can safely move pred
                pred = pred.next
                
            # move head to next
            head = head.next
            
        return sentinel.next
        
if __name__ == '__main__':
    solver = Solution()
    
    l = [1,1,2,3,4]
    head = ListNode()
    cursor = head
    for i in l:
        cursor.next = ListNode(i)
        cursor = cursor.next

    result = solver.deleteDuplicates(head.next)
        
    while result!=None:
        print(result.val)
        result = result.next


# In[ ]:




