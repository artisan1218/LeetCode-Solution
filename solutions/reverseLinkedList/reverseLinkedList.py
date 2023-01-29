#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseListNaive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = head
        cacheList = []
        
        # store all ListNode in a list so that we can retrieve it later
        while cursor!=None:
            cacheList.append(cursor)
            cursor = cursor.next
        
        # create new linked list
        resultHead= ListNode()
        resultCursor = resultHead
        for node in reversed(cacheList):
            resultCursor.next = node
            resultCursor = resultCursor.next
        # disconnect original head to prevent loop
        resultCursor.next=None
        
        return resultHead.next
    
    def reverseListIteration(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        
        while head!=None:
            # first use a new pointer to hold the remaining linked list
            nextNode = head.next
            # reverse current node, newHead start with null, so last node in reversed linked list points to null
            head.next = newHead
            # point newHead to current head
            newHead = head
            # move head to nextNode, cannot use head = head.next because head is not disconnected from nextNode
            head = nextNode
        return newHead
    
    def reverseListRecursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def recursion(head, prevHead):
            # enter recursion stack until we've reached the end of linked list
            if head==None:
                return prevHead
            
            nextNode = head.next
            head.next = prevHead
            # head becomes predHead in the next recursive stack
            return recursion(nextNode, head)
        
        return recursion(head, None)
            
        
if __name__ == '__main__':
    solver = Solution()
    
    l = [1,2,3,4,5]
    head = ListNode()
    cursor = head
    for i in l:
        cursor.next = ListNode(i)
        cursor = cursor.next

    result = solver.reverseListRecursion(head.next)
        
    while result!=None:
        print(result.val)
        result = result.next


# In[ ]:




