#!/usr/bin/env python
# coding: utf-8

# In[77]:


from typing import List

def fourSumBasedOnThreeSum(nums: List[int], target: int) -> List[List[int]]:
    result = []
    nums.sort()
    
    for idx in range(len(nums)-3):
        if idx==0 or nums[idx]!=nums[idx-1]:
            tmp_result = threeSum(nums[idx+1:], target - nums[idx])
            for threeSumList in tmp_result:
                threeSumList.append(nums[idx])
            result.extend(tmp_result)
               
    return result

def threeSum(nums, target):
    result = []
    for idx, num in enumerate(nums):
        left = idx+1
        right = len(nums)-1
        # if this is the first value, then no need to check duplicates
        if idx==0 or nums[idx]!=nums[idx-1]:
            while(left<right):
                if nums[left] + nums[right] + num == target:
                    result.append([num, nums[left], nums[right]])
                    while left<right and nums[left]==nums[left+1]: # skip duplicate elements
                        left+=1
                    while left<right and nums[right]==nums[right-1]: # skip duplicates
                        right-=1
                    left+=1 # move the left pointer to a new pos
                    right-=1 # move the right pointer to a new pos
                elif nums[left] + nums[right] + num < target:
                    left+=1
                else:
                    right-=1
    return result
        


# In[103]:


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        self.nSum(nums, target, 4, [], results)
        return results

    def nSum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: 
            return
        else:
            # solve 2-sum using two pointers
            if N == 2:
                left = 0
                right = len(nums)-1

                while left < right:
                    if nums[left] + nums[right] == target:
                        results.append(result + [nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
            else:
                # n sum requires at least n elements in the list
                for i in range(len(nums)-N+1):
                    # nums[i] is the smallest element and nums[-1] is the largest element
                    if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                        break
                    else:
                        if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                            self.nSum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
            return


# In[104]:


if __name__ == "__main__":
    nums = [2,2,2,2,2]
    target = 8
    solver = Solution()
    print(solver.fourSum(nums, target))


# In[ ]:




