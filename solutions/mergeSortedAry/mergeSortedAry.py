#!/usr/bin/env python
# coding: utf-8

# In[4]:


from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mod = m+n-1
        cur1 = m-1
        cur2 = n-1
        
        # fill in nums1 from back
        while cur1>=0 and cur2>=0:
            if nums1[cur1] > nums2[cur2]:
                nums1[mod] = nums1[cur1]
                cur1-=1
            else:
                nums1[mod] = nums2[cur2]
                cur2-=1
            mod-=1
        
        # fill in with the rest elements in nums2
        if cur2>=0:
            nums1[0:cur2+1] = nums2[0:cur2+1]
        
if __name__ == '__main__':
    solver = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    
    solver.merge(nums1, m, nums2, n)
    print(nums1)


# In[ ]:




