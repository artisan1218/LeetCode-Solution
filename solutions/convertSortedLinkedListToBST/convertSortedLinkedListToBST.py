#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head!=None:
            nums.append(head.val)
            head = head.next
        
        def convert(nums):
            if len(nums)==0:
                return None
            else:
                # find a middle point
                mid = len(nums)//2
                # make middle point at the root 
                root = TreeNode(nums[mid])
                root.left = convert(nums[0:mid])
                root.right = convert(nums[mid+1:])
                return root
            return root
        return convert(nums)
    
    def sortedListToBST2(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        # find the length of the linked list
        def findSize(head):
            ptr = head
            size = 0
            while ptr!=None:
                ptr = ptr.next
                size += 1
            return size
        
        def convert(l, r):
            nonlocal head
            
            if l>r:
                return None
            else:
                mid = (l+r)//2
                
                leftBranch = convert(l, mid-1) # left subtree
                root = TreeNode(head.val) # root is not the element at mid, but head, we will build the leftsubtree first
                root.left = leftBranch # connect root and left subtree
                
                head = head.next # move the head to right, build the right subtree
                rightBranch = convert(mid+1, r) # right subtree
                root.right = rightBranch # connect
                
                return root
        
        size = findSize(head)
        return convert(0, size-1)
            
        
if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    solver = Solution()
    tree = solver.sortedArrayToBST2(nums)

