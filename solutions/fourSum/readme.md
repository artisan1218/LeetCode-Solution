# 4Sum problem
* Given an array nums of n integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
```
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
```
You may return the answer in any order.

Leetcode link: https://leetcode.com/problems/4sum/

<br />

### Approach 1: Two Pointers, fourSumBasedOnThreeSum()
This approach is based on [3Sum](https://github.com/artisan1218/LeetCode-Solution/tree/main/threeSum) problem. The idea is to go through the list, fix one number at a time and find corresponding three sum and append them together. We just grab threeSum() and use it in a loop to achieve this. Time complexity is simply O(n\*threeSum Complexity), which is O(n^3).

```python3
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
```

Actual running time is indeed quite slow:\
![image](https://user-images.githubusercontent.com/25105806/119611564-b778b600-bdaf-11eb-833d-eaa0a89855ef.png)


<br />

### Approach 2: Two Pointers, Recursion, Solution.fourSum()
Credits to https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)


This approach considers a more generalized case of kSum. We can solve 2Sum problem really quick using two pointers, to solve 3Sum problem, simply fix a number and use 2Sum algorithm to find the rest two numbers. The idea can be extended to kSum by using recursion. 
1. Base case: 2Sum using two pointers
2. Recursive step: kSum = nSum(nums, k-1, k-1 result)

We use recursion to reduce k down to 2 and keep the k-1 result to append it to k result. So that we always fix a number and find k-1 sum.

```python3
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
```

Actual running time is quite fast:\
![image](https://user-images.githubusercontent.com/25105806/119612527-d9bf0380-bdb0-11eb-9bfa-f65f11284c64.png)


