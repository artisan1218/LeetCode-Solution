# Minimum Number of Increments on Subarrays to Form a Target Array problem
![image](https://user-images.githubusercontent.com/25105806/136676629-e1a1af26-1d03-42b6-b86f-021a0d010b23.png)

Leetcode link: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

<br />

### Approach 1: Brute Force, minNumberOperationsBruteForce()
The idea is to scan the array `target` level by level, count the number of consecutive subsequence `blocks` and sum them up. \
This leads to TLE

```python
def minNumberOperationsBruteForce(self, target: List[int]) -> int:
    def countBlocks(nums, level):
        blocks = 0
        for i, num in enumerate(nums):
            if i==0 and num-level>0:
                blocks = 1
            elif num-level > 0 and nums[i-1]-level <= 0:
                blocks += 1
        return blocks

    height = max(target)
    level = 0
    minNum = 0
    for i in range(height):
        minNum += countBlocks(target, level)
        level+=1

    return minNum
```

Time complexity is O(h*\n) where h is the value of largest element in `target` and n is the length of `target`


<br />

### Approach 2: Dynamic Programming, minNumberOperationsDP()
This solution will only go over the array `target` once. We maintain a variable `result` that keeps track of the answer. `result` is initialized to the first element of the `target`, if the current value in `target` is smaller than the previous, we should not update `result`, however if its greater than previous value, we should update the `result` to `result = result + currentVal - prev` because the height of previous value `prev` is the number of increment we can share with current value, but since current value is greater than previous value, we also have to take account in the height difference between current value and previous value: `currentVal - prev`.

![image](https://user-images.githubusercontent.com/25105806/136676773-39592db1-b845-4551-82d0-2ec4daf5d964.png)


```python
def minNumberOperations(self, target: List[int]) -> int:
    result = target[0]
    prev = target[0]
    for i in range(1, len(target)):
        if target[i] > prev:
            result = result + target[i] - prev
        prev = target[i]
    return result
```

Time complexity is O(n) where n is the length of `target`:\
![image](https://user-images.githubusercontent.com/25105806/136676748-92c8f8f3-4211-4e5c-9756-4856fbabeca5.png)



    

