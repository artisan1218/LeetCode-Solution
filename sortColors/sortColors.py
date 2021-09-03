#!/usr/bin/env python
# coding: utf-8

# In[43]:


from typing import List

class Solution:
    def sortColorsNaive(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        moveCounter = 0
        i = 0
        while i<len(nums): # O(n)
            if nums[i] == 0:
                if i!=0:
                    moveCounter+=1
                    nums.insert(0, 0) # O(n)
                    nums.pop(i+1) # O(n) for arbitrary element and O(1) for last element
                # first element is 0, no need to exchange position, simply check the next one
                i+=1
            elif nums[i] == 2:
                moveCounter+=1
                nums.append(2) # O(1)
                nums.pop(i) # O(n)
            else:
                # 1's position does not need to be changed
                i+=1
            if moveCounter == len(nums):
                break
    
    def sortColorsOnePtrTwoPass(self, nums: List[int]) -> None:
        # move all 0's to the head
        head = 0
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i], nums[head] = nums[head], nums[i]
                head+=1
        
        # head is now the index of first non-0 number
        # move all 1's to the place after 0
        for i in range(head, len(nums)):
            if nums[i]==1:
                nums[i], nums[head] = nums[head], nums[i]
                head+=1
        
    def sortColorsTwoPtrsOnePass(self, nums: List[int]) -> None:
        head = 0
        tail = len(nums)-1
        for i in range(len(nums)):
            # i is not changed because we need to see if the exchanged value is still 2
            while i<=tail and nums[i]==2:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail-=1
            if nums[i] == 0:
                nums[i], nums[head] = nums[head], nums[i]
                head+=1
        
    def sortColorsTwoPtrsOnePass2(self, nums: List[int]) -> None:
        head = 0
        tail = len(nums)-1
        i = 0
        while i<=tail:
            if nums[i] == 0:
                nums[i], nums[head] = nums[head], nums[i]
                head+=1
                i = max(head, i)
            elif nums[i] == 2:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail-=1
            else:
                i+=1
                
    def sortColorsTwoPtrsOnePass3(self, nums: List[int]) -> None: 
        head = 0
        tail = len(nums)-1
        i = 0
        while i<=tail:
            if nums[i]==0:
                nums[i], nums[head] = nums[head], nums[i]
                head+=1
                i+=1
            elif nums[i]==2:
                # i is not changed because we need to see if the exchanged value is still 2
                nums[i], nums[tail] = nums[tail], nums[i]
                tail-=1
            else:
                i+=1
        
    def sortColorsValAssign(self, nums: List[int]) -> None: 
        # zero is the ending index of group 0
        # one is the ending index of group 1
        zero, one = 0, 0
        for i in range(len(nums)):
            num = nums[i]
            nums[i] = 2
            # if the original number is 0 or 1, we need to 'move' it to the front
            # by changing current number to 2, and changing the ending index of 1 to 1
            if num == 1:
                nums[one] = 1
                one += 1
            # if the original number is 0, we need to not only update ending index of 1 but also ending index of 0
            # because 1 is after 0, updating 0 also requires updating 1
            elif num == 0:
                # equivalent to shift 1 to the right by one and shift 0 to the right by 1
                nums[one] = 1
                nums[zero] = 0
                one += 1
                zero += 1
            #print(nums, i, zero, one)
             
if __name__ == '__main__':
    solver = Solution()
    nums = [2,0,2,1,1,0]
    solver.sortColorsValAssign(nums)
    print(nums)


# In[ ]:




