# Subsets problem
* Given an integer array `nums` of unique elements, return all possible subsets (the power set).

Leetcode link: https://leetcode.com/problems/subsets/

<br />

### Approach 1: Backtracking, backtrack()
This idea is similar to [combinations](https://github.com/artisan1218/LeetCode-Solution/tree/main/combinations) problem. We just need a loop that loops through all different length and get all combinations for all lengths.

```python3
def subsets(self, nums: List[int]) -> List[List[int]]:
    result = []
    current = []
    for length in range(1, len(nums)+1):
        self.backtrack(nums, current, result, 0, length)
    return [[]] + result

def backtrack(self, nums, current, result, start, length):
    if len(current) == length:
        result.append(current.copy())
    else:
        for i in range(start, len(nums)):
            if len(current) + len(nums) - i + 1 >= length:
                current.append(nums[i])
                self.backtrack(nums, current, result, i+1, length)
                current.pop()
```


Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/132104051-670a7f93-10e1-4546-8b7c-aded3eb70bfb.png)


<br />

### Approach 2: Cascading, subsetsCascading()
The idea can bu summaried by the image below:\
![image](https://user-images.githubusercontent.com/25105806/132104075-2862fbcd-c983-49a1-9a69-10bcaa21911c.png)

```python3
def subsetsCascading(self, nums: List[int]) -> List[List[int]]:
    # start with empty list
    result = [[]]

    for new in nums:
        # use the previous length of the result, so assign the length of result to n
        n = len(result)
        for i in range(n):
            result.append(result[i]+[new])
    return result
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/132104095-5c4e3987-d82b-4227-821c-ecd713acded6.png)







