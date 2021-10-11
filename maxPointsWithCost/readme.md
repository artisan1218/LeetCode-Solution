# Maximum Number of Points with Cost problem
<img width="1134" alt="image" src="https://user-images.githubusercontent.com/25105806/136757389-78b3a1ca-0a6b-42a8-8a53-458e7203fcf7.png">

Leetcode link: https://leetcode.com/problems/maximum-number-of-points-with-cost/

<br />

### Approach 1: Brute Force, maxPointsBruteForce()
The idea is to iterate over each row of `points`, then each value of that row, then calculate the max value by going over all the values in previous row.

```python
def maxPointsBruteForce(self, points: List[List[int]]) -> int:
    rows = len(points)
    cols = len(points[0])

    pre = points[0].copy()
    dp = points[0].copy()
    for r in range(1, rows): # starting at the second row
        for c in range(0, cols): # for each of the element in this rwo
            for k in range(len(pre)): # go through each previous elements and update dp accordingly
                dp[c] = max(dp[c], points[r][c]+pre[k]-abs(k-c))
        pre = dp.copy()
    return max(dp)
```

Time complexity is O(m\*n^2) where m is the number of rows and n is the number of columns

<br />

### Approach 2: Dynamic Programming, maxPointsDP()
We can find that for each value in a certain row, we only need to consider three values in previous row: the max value on the left side of current value's index, the value right above current value, and the max value on the right side of current value's index.

Then we can write a dynamic solution to calculate the max value from left to right for each index in a row, and the max value from right to left for each index in a row. Then simply go over the current row, pick the larger one from either `left` or `rigth` and 
