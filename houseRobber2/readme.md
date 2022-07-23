# House Robber problem
<img width="928" alt="image" src="https://user-images.githubusercontent.com/25105806/138203292-2c30b823-a6e6-40d8-b8e7-a76b059e7dd2.png">

Leetcode link: https://leetcode.com/problems/house-robber/

<br />

### Approach 1: DFS with Memorization, robRecursion()
The idea is to use DFS to explore all possible ways of robbing, then use memorization to avoid counting duplicate cases. At each house, we have two choices: either rob the current one and the one before previous one, or rob the previous one. Then just return the max value of these two cases at each recursion.

```python
def robRecursion(self, nums: List[int]) -> int:
    mem = dict()
    def dfs(nums, i, mem):
        if i in mem:
            return mem[i]
        else:
            if i>=len(nums):
                return 0
            else:
                option1 = nums[i] + dfs(nums, i+2, mem) # rob current house and rob i+2
                option2 = dfs(nums, i+1, mem) # skip this one and rob i+1

                mem[i] = max(option1, option2)
                return mem[i] 
    return dfs(nums, 0, mem)
```

Time complexity is O(n):\
<img width="666" alt="image" src="https://user-images.githubusercontent.com/25105806/138203580-c2d906ac-b5ab-4dd3-8f55-80c97c06e75e.png">


<br />

### Approach 2: Dynamic Programming, robDP1()
The idea is to use a `dp` array to hold the max amount of robbing at each house. We have same two choices at each house as approach 1 stated, but this time we use dp array to memorize the previous amount.

```python
def robDP1(self, nums: List[int]) -> int:
    if len(nums)==1:
        return nums[0]
    else:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            # for each num at i, we found the max value of i-1 or i-2 + nums[i]
            # dp[i-1] means rob the previous one, so that we cannot rob the current
            # dp[i-2] + num means rob the current one and the one before previous one
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[-1]
```

Time complexity is O(n):\
<img width="668" alt="image" src="https://user-images.githubusercontent.com/25105806/138203857-07f858b6-b32d-4039-93fb-ac025f6bf1ab.png">

<br />

### Approach 3: Dynamic Programming, robDP2()
Same as approach 2, but since the result at each house only depends on the previous two houses, we can then only use two variable `pre` and `cur` to calculate the result.

```python
def robDP2(self, nums: List[int]) -> int:
    pre = 0
    cur = 0
    for num in nums:
        # pre + num means rob the current one and the one before the previous one
        # cur means rob the previous one, so we cannot rob current one(num) or the one before previous one(pre)
        pre, cur = cur, max(pre+num, cur)

    return cur
```

Time complexity is O(n):\
<img width="665" alt="image" src="https://user-images.githubusercontent.com/25105806/138204093-1712ef40-7d12-40a6-bb34-030afda97e54.png">


