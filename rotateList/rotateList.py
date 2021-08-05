#!/usr/bin/env python
# coding: utf-8

# In[84]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:        
        if head==None:
            return head
        else:
            # get the length of the linked list using O(n)
            length = 0
            len_cursor = head
            while len_cursor:
                length+=1
                len_cursor = len_cursor.next
            
            # length is at least 1 because we've ruled out case where there is no node in the linked list
            # if k is longer than the length of the linked list, we can simply get the mod because rotating
            # 7 times of a length 6 linked list is no difference than rotating once
            k = k%length

            # find tail using O(n)
            tail = head
            while tail.next:
                tail = tail.next

            # connect tail and head
            tail.next = head

            # move current head to correct index
            for i in range(length - k):
                head = head.next

            # cut the circle we've created by connecting tail to head
            while tail.next != head:
                tail = tail.next
            tail.next = None

            return head
    
if __name__ == '__main__':
    head = ListNode(1)
    cursor = head
    for i in range(4):
        cursor.next = ListNode(i+2)
        cursor = cursor.next
    
    solver = Solution()
    result = solver.rotateRight(head, k=2)
    
    while result:
        print(result.val, end=' ')
        result = result.next


# In[ ]:




