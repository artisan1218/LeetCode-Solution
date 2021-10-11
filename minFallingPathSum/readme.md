# Minimum Falling Path Sum problem
![image](https://user-images.githubusercontent.com/25105806/136836197-22d4a379-3ac4-425a-8aec-f1949c501325.png)

Leetcode link: https://leetcode.com/problems/minimum-falling-path-sum/

<br />

### Approach 1: Dynamic Programming, minFallingPathSum()
The idea is to iterate through each element in the `matrix`, calculate the minimal path they can take from previous row, sum up the path values and go to next row. Since we only need to consider 3 elements in previous row each time, we can use `min(left, mid, right)` in O(1) time to get the min path for each node.

```python
def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])

    pre = matrix[0].copy()
    dp = matrix[0].copy()
    for r in range(1, rows):
        for c in range(cols):
            left = pre[max(0, c-1)] # max(0, c-1) is to bound the range when c=0
            mid = pre[c]
            right = pre[min(cols-1, c+1)] # min(cols-1, c+1) is to bound the range when c=cols
            dp[c] = matrix[r][c] + min(left, mid, right)
        pre = dp.copy()

    return min(dp)
```

Time complexity is O(m\*n) where m is the length of `matrix` and n is the length of each row in `matrix`:\
![image](https://user-images.githubusercontent.com/25105806/136836577-a23beb06-73c0-4468-9184-ad8fbe5031ff.png)


    

