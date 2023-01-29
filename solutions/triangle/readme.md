# Triangle problem
![image](https://user-images.githubusercontent.com/25105806/150445459-cd838afd-f817-4bad-bf89-b3c59e358b0f.png)

Leetcode link: https://leetcode.com/problems/triangle/

<br/>

### Approach 1: Dynamic Programming, Bottom-up approach, minimumTotalDPbottomUp()
Credit to: https://www.youtube.com/watch?v=OM1MTokvxs4

The idea of this approach is to calculate the minimum sum of path that contains each element in the `triangle`. We can treat the `triangle` array as a tree. We then scan from bottom to top, at each level, we calculate and store the minimum sum of the element at current level with corresponding element at upper level. When we work our way up, the sum at the first level will be the answer.

Demo:\
<img src="https://user-images.githubusercontent.com/25105806/150448124-dbe3c8aa-1836-46b5-9c62-c76b106389b7.jpg" width="60%" height="60%">

```python3
def minimumTotalDPbottomUp(self, triangle: List[List[int]]) -> int:
    dp = [0] * (len(triangle) + 1)
    for row in reversed(triangle):
        for i in range(len(row)):
            dp[i] = row[i] + min(dp[i], dp[i+1])
    return dp[0]
```

We only need to store one level of size `n` where `n` is the size of array at the bottom of the `triangle`. So space complexity is O(n). Time complexity is O(n^2):\
![image](https://user-images.githubusercontent.com/25105806/150446224-c1d3e1fb-a45e-4be0-bd93-218e534a5cf5.png)

<br />

### Approach 2: Dynamic Programming, Top-down approach, minimumTotalDPtopDown()
Similarily, we can also scan from top to bottom. The idea is, again, to sum up and store the minimum sum of element at current level and the stored sum at previous levels. When we work our way down, the answer will be the minimum among the last row.

Demo:\
<img src="https://user-images.githubusercontent.com/25105806/150447750-847f78fe-02b8-4815-8448-203924ad14d1.jpg" width="60%" height="60%">

```python3
def minimumTotalDPtopDown(self, triangle: List[List[int]]) -> int:
    curr_dp = [triangle[0][0]]
    for row in triangle[1:]:
        next_dp = [float('inf')] * len(row)
        for i in range(len(curr_dp)):
            next_dp[i] = min(curr_dp[i]+row[i], next_dp[i])
            next_dp[i+1] = min(curr_dp[i]+row[i+1], next_dp[i+1])
        curr_dp = next_dp
    return min(curr_dp)
```

Time complexity is O(n^2) and space complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/150447916-c063ff59-4dd7-4fa4-8694-8f6302c65777.png)
