# Spiral Matrix II problem
* Given a positive integer `n`, generate an `n x n` matrix filled with elements from 1 to n2 in spiral order.
  
  ![image](https://user-images.githubusercontent.com/25105806/127755454-d44304f7-e53b-4d01-9384-826a74235b1b.png)

Leetcode link: https://leetcode.com/problems/spiral-matrix-ii/

<br />

### Approach 1: Walk in Spiral Order 1, generateMatrix()
The idea is same as spiralMatrix problem solved [here](https://github.com/artisan1218/LeetCode-Solution/tree/main/spiralMatrix). The only difference is now we access each digit in matrix and modify it to an increasing number instead of storing it to another list. 

We will read in the `matrix` in spiral order. That is, read first line from left to right, then top to bottom, right to left, then bottom to top, then start another loop of reading in this order until we've read all elements in the matrix.

We will use four separate for loop to control the right turn of the reader and use `offset` to control the amount of elements we should modify in each direction.

```python3
def generateMatrix(self, n: int) -> List[List[int]]:
    matrix = [[1 for i in range(n)] for i in range(n)]
    numRows = len(matrix)
    numCols = len(matrix[0])
    totalNums = n**2
    seenNums = 0

    left2right_row = 0
    offset = 0
    while seenNums < totalNums:
        # left to right
        for i in range(offset, len(matrix[left2right_row])-offset):
            matrix[left2right_row][i] = seenNums+1
            seenNums+=1
        offset+=1
        left2right_row+=1
        if seenNums==totalNums:
            break

        # top to bottom
        top2bottom_row = left2right_row
        top2bottom_col = numCols-offset
        while top2bottom_row < numRows-offset:
            matrix[top2bottom_row][top2bottom_col] = seenNums+1
            seenNums+=1
            top2bottom_row+=1
        if seenNums==totalNums:
            break   

        # right to left
        right2left_row = top2bottom_row
        for i in reversed(range(0+offset-1, numCols-offset+1)):
            matrix[right2left_row][i] = seenNums+1    
            seenNums+=1
        if seenNums==totalNums:
            break


        # bottom to top
        bottom2top_row = right2left_row-1
        bottom2top_col = 0+offset-1
        while bottom2top_row >= left2right_row:
            matrix[bottom2top_row][bottom2top_col] = seenNums+1
            bottom2top_row-=1
            seenNums+=1
        if seenNums==totalNums:
            break

    return matrix
```


The time complexity is O(n) because we will reach each element in the matrix exactly once
![image](https://user-images.githubusercontent.com/25105806/127755521-36e59f55-eb87-483d-b97b-763382c58afb.png)


<br />

### Approach 2: Walk in Spiral Order 2, generateMatrixWalkSpiral()
Credits to https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions

The idea is same as approach 1, but use a much more consise code logic to control the right turn: 

`matrix[(row+di)%n][(col+dj)%n]` checks if the next element is already added, the next element means the next element that we will meet in matrix if keep straight. 

If the element has value greater than 0, then we should make a right turn by exchaning the row and col direction(`row_direction, col_direction = col_direction, -row_direction`)

This is a very clever way to control the right turn but it also reduce the readability by a lot.


```python3
def generateMatrixWalkSpiral(self, n: int) -> List[List[int]]:
    matrix = [[0] * n for _ in range(n)]
    row, col, row_direction, col_direction = 0, 0, 0, 1
    for num in range(n**2):
        matrix[row][col] = num + 1
        # matrix[(row+di)%n][(col+dj)%n] checks if the next element is already added
        # the next element means the next element that we will meet in matrix if keep straight
        # if the element has value greater than 0, then we should make a right turn
        # by exchaning the row and col direction
        if matrix[(row+row_direction)%n][(col+col_direction)%n] >0:
            row_direction, col_direction = col_direction, -row_direction
        row += row_direction
        col += col_direction
    return matrix
```

Time complexity is still O(n):

![image](https://user-images.githubusercontent.com/25105806/127755570-6edd1ebe-a11f-499a-bac6-92d6a1c66ee3.png)
