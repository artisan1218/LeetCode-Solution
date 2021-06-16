#!/usr/bin/env python
# coding: utf-8

# In[88]:


from typing import List

class Solution:
    def searchRangeExpandAroundMiddle(self, nums: List[int], target: int) -> List[int]:
        
        # regular binary search to find the index of a target
        left = 0
        right = len(nums)-1
        
        # 'middle' denotes the index of the target
        # middle is not necessarily the exact middle point of the range, but just a point in the range
        middle = -1
        while left<=right:
            midpoint = int((left+right)/2)
            if nums[midpoint] < target:
                left = midpoint+1
            elif nums[midpoint] > target:
                right = midpoint-1
            else:
                middle = midpoint
                break

        # if the target is not found
        if middle==-1:
            return [-1, -1]
        else:
            # middle is not necessarily the exact middle point of the range, but just a point in the range
            start = middle
            end = middle

            # This is not really an O(log n) code block but it works
            # expand the range at the 'middle' point to the left and right 
            while start>=0 and nums[start]==target or end<len(nums) and nums[end]==target:
                if start>=0 and nums[start]==target:
                    start -= 1
                if end<len(nums) and nums[end]==target:
                    end += 1

            return [start+1, end-1]

    def searchRangeTwoPassBinarySearch(self, nums: List[int], target: int) -> List[int]:
        
        # use binary search to find the start index of the range
        left = 0
        right = len(nums)-1
        start = -1
        while left<=right:
            midpoint = int((left+right)/2)
            if nums[midpoint] < target:
                left = midpoint+1
            else:
                if nums[midpoint] > target:
                    right = midpoint-1
                else:
                    # nums[midpoint] == target
                    # if midpoint is the beginning of the nums, or the previous value is not equal to target
                    # this means midpoint is now the starting index of the range, simply return it
                    if midpoint==0 or nums[midpoint-1]!=target:
                        start = midpoint
                        break
                    # otherwise we should move rigth pointer as if nums[midpoint] > target 
                    # because we want midpoint goes to left
                    # this is why this algorihtm still have O(log n) complexity
                    else:
                        right = midpoint-1
        
        if start==-1:
            return [-1, -1]
        else:
            # use binary search to find the end index of the range only when start is not -1
            # left can be start index because we've ruled out every element before start
            left = start
            right = len(nums)-1
            end = -1
            while left<=right:
                midpoint = int((left+right)/2)
                if nums[midpoint] <= target:
                    if nums[midpoint] < target:
                        left = midpoint+1
                    else:
                        # case where midpoint is equal to target
                        # if midpoint is the ending of the nums, or the next value is not equal to target
                        # this means midpoint is now the ending index of the range, simply return it
                        if midpoint==len(nums)-1 or nums[midpoint+1]!=target:
                            end = midpoint
                            break
                        # otherwise we should move the left pointer because we want
                        # the midpoint to goes to right
                        # this is why this algorihtm still have O(log n) complexity
                        else:
                            left = midpoint+1
                else:
                    # nums[midpoint] > target
                    right = midpoint-1
        
        return [start, end]

if __name__ == "__main__":
    solver = Solution()
    nums = [1,2,2,2,2,3,4,5]
    target = 2
    print(solver.searchRange(nums, target))


# In[ ]:




