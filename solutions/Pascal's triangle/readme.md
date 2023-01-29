# Pascal's Triangle problem
<img width="613" alt="Screen Shot 2022-01-09 at 8 09 54 PM" src="https://user-images.githubusercontent.com/25105806/148717575-1b1dbc72-a9d8-4e4b-ab46-1db7a385d5bb.png">

Leetcode link: https://leetcode.com/problems/pascals-triangle/

<br />

### Approach 1: Math, generate()
This solution is exactly how we compute the Pascal's triangle step by step. We only keep two variables, the current row and the previous row (in order to compute the element in current row) and compute row by row.

```python3
def generate(self, numRows: int) -> List[List[int]]:
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        res = [[1], [1, 1]]
        for lvl_idx in range(2, numRows):
            level = [1]
            for j in range(1, lvl_idx):
                level.append(res[-1][j-1] + res[-1][j])
            level.append(1)
            res.append(level)
        return res
```

Time complexity is O(n):\
<img width="643" alt="image" src="https://user-images.githubusercontent.com/25105806/148717694-f9d94051-2b87-454e-8afb-20ad7f1639fd.png">

