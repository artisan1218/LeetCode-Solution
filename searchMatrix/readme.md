# Search a 2D Matrix problem
* Write an efficient algorithm that searches for a value in an `m x n` matrix. This matrix has the following properties:
* Integers in each row are sorted from left to right.
* The first integer of each row is greater than the last integer of the previous row.
* Return `True` if `target` is found in the matrix, otherwise `False`

Leetcode link: https://leetcode.com/problems/search-a-2d-matrix/

<br />

### Approach 1: Column First, then Row, searchMatrixColRow()
Since the matrix is sorted, we can first search by the first element in each row, starting at row number 0 until we found a element that is bigger than the  `target`, then the row number will be the previous row index. Then simply search through that row to find the `target`.

```python3
def searchMatrixColRow(self, matrix: List[List[int]], target: int) -> bool:
    # since the matrix is sorted
    # first check column
    numRows = len(matrix)
    numCols = len(matrix[0]) # matrix has at least 1 row

    # found the row number of target
    targetRowIdx = 0
    for row in range(numRows):
        if matrix[row][0] <= target:
            targetRowIdx = row
        else:
            break

    # found the correct column number
    for col in range(numCols):
        if matrix[targetRowIdx][col] == target:
            return True

    # not found after searching all numbers in this row
    return False
```

Time complexity O(M+N) where M is the number of rows and N is the number of columns:\
![image](https://user-images.githubusercontent.com/25105806/131790088-e53057d3-6735-49e4-9606-0b9dc8ca0817.png)


<br />

### Approach 2: Binary Search, searchMatrixBinarySearch()
Credits to: https://leetcode.com/problems/search-a-2d-matrix/discuss/26220/Don't-treat-it-as-a-2D-matrix-just-treat-it-as-a-sorted-list

Turns out we can treat the sorted matrix as a sorted list in ascending order, each element is greater than the previous value. We only need to convert the index number in the sorted list to coordinates in terms of row index and column index in the matrix.\
`rowIndex = listIndex//rowLen` and `colIndex = listIndex%rowLen`.\
Then simply use binary search to find the `target`

```python3
def searchMatrixBinarySearch(self, matrix: List[List[int]], target: int) -> bool:
    # treat the sorted matrix as a list
    # apply binary search on the sorted list to find the target

    # length of the sorted list if consider matrix as a list
    totalLen = len(matrix) * len(matrix[0])
    rowLen = len(matrix[0])

    left = 0
    right = totalLen - 1
    while left <= right:
        middle = (left + right) // 2
        row, col = middle//rowLen, middle%rowLen
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            right = middle - 1
        else:
            left = middle + 1

    return False
```

Time complexity is O(logN) where N is the total number of elements in the matrix:\
![image](https://user-images.githubusercontent.com/25105806/131790577-2e9a10c7-79b3-4e76-923e-48f1bea8258d.png)

