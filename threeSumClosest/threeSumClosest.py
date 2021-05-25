#!/usr/bin/env python
# coding: utf-8

# In[29]:


from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    result = list()
    nums.sort()
    
    closest = 0
    prev_diff = float('inf')
    # at least three elements in nums is needed, otherwise just return empty list
    for idx in range(len(nums)-2):
        # use two pointers to bound the range
        left = idx+1 # left pointer always start at current index + 1 so that it never visit seen elements
        right = len(nums)-1
        if idx==0 or nums[idx]!=nums[idx-1]: #will skip the same value
            while left < right:
                # update the best result so far
                curr_diff = abs(target - (nums[idx] + nums[left] + nums[right]))
                if curr_diff < prev_diff:
                    prev_diff = curr_diff
                    closest = nums[idx] + nums[left] + nums[right]
                    
                # update pointers
                if nums[idx] + nums[left] + nums[right] == target:
                    return target
                elif nums[idx] + nums[left] + nums[right] < target:
                    left+=1
                else:
                    right-=1
    return closest


# In[32]:


if __name__ == "__main__":
    nums = [0, 2,1,-3]
    target = 1

    print(threeSumClosest(nums, target))


# In[ ]:




