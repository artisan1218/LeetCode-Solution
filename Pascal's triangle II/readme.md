# Pascal's Triangle II problem
<img width="633" alt="image" src="https://user-images.githubusercontent.com/25105806/148718901-611c0055-c70b-4d0b-952f-7f83f1d185d9.png">

Leetcode link: https://leetcode.com/problems/pascals-triangle-ii/

<br />

### Approach 1: getRow()
The idea is similar to [Pascal's Triangle](https://github.com/artisan1218/LeetCode-Solution/tree/main/Pascal's%20triangle). The only difference is that we only need to return the last row instead of all rows. Furthermore, since the current row of Pascal's triangle only depends on the previous row, it is reasonable to keep only two rows when looping through all rows until row `rowIndex`. This way, we use only `O(rowIndex)` extra space

```python3
def getRow(self, rowIndex: int) -> List[int]:
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1, 1]
    else:
        prevRow = [1, 1]
        for lvl_idx in range(2, rowIndex+1):
            curRow = [1]
            for j in range(1, lvl_idx):
                curRow.append(prevRow[j-1] + prevRow[j])
            curRow.append(1)
            prevRow = curRow
        return curRow
```

Time complexity is O(n):\
<img width="643" alt="image" src="https://user-images.githubusercontent.com/25105806/148719235-214fc4ab-92b6-4173-b815-7062956548ec.png">


