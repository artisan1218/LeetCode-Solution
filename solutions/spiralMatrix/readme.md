# Spiral Matrix problem
* Given an `m` x `n` matrix, return all elements of the `matrix` in spiral order.
  
  ![image](https://user-images.githubusercontent.com/25105806/127098278-7fdc9cb1-9465-4e16-9982-1f9732f2552e.png)

Leetcode link: https://leetcode.com/problems/spiral-matrix/

<br />

### Approach 1: List Traversal, spiralOrder()
The idea is very straight-forward, we will read in the `matrix` in spiral order. That is, read first line from left to right, then top to bottom, right to left, then bottom to top, then start another loop of reading in this order until we've read all elements in the matrix.

```python3
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    result = list()

    numRows = len(matrix)
    numCols = len(matrix[0])
    totalNums = numRows * numCols
    seenNums = 0

    left2right_row = 0
    offset = 0
    while seenNums < totalNums:
        # left to right
        for i in matrix[left2right_row][0+offset:numCols-offset]:
            result.append(i)
            seenNums+=1
        offset+=1
        left2right_row+=1
        if seenNums==totalNums:
            break

        # top to bottom
        top2bottom_row = left2right_row
        top2bottom_col = numCols-offset
        while top2bottom_row < numRows-offset:
            row = matrix[top2bottom_row]
            result.append(row[top2bottom_col])
            seenNums+=1
            top2bottom_row+=1
        if seenNums==totalNums:
            break   

        # right to left
        right2left_row = top2bottom_row
        for i in reversed(matrix[right2left_row][0+offset-1:numCols-offset+1]):
            result.append(i)
            seenNums+=1
        if seenNums==totalNums:
            break


        # bottom to top
        bottom2top_row = right2left_row-1
        bottom2top_col = 0+offset-1
        while bottom2top_row >= left2right_row:
            result.append(matrix[bottom2top_row][bottom2top_col])
            bottom2top_row-=1
            seenNums+=1
        if seenNums==totalNums:
            break


    return result
```

The time complexity is O(n) because we will reach each element in the matrix exactly once:\
![image](https://user-images.githubusercontent.com/25105806/127098523-a541c29c-cb91-4f77-8741-504a8f325374.png)
