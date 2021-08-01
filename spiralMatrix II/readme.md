# Spiral Matrix II problem
* Given a positive integer `n`, generate an `n x n` matrix filled with elements from 1 to n2 in spiral order.
  
  ![image](https://user-images.githubusercontent.com/25105806/127755454-d44304f7-e53b-4d01-9384-826a74235b1b.png)


### Approach 1: Walk in Spiral Order 1, generateMatrix()
The idea is same as spiralMatrix problem solved [here](https://github.com/artisan1218/LeetCode-Solution/tree/main/spiralMatrix). The only difference is now we access each digit in matrix and modify it to an increasing number instead of storing it to another list. 

We will read in the `matrix` in spiral order. That is, read first line from left to right, then top to bottom, right to left, then bottom to top, then start another loop of reading in this order until we've read all elements in the matrix.

We will use four separate for loop to control the right turn of the reader and use `offset` to control the amount of elements we should modify in each direction.

The time complexity is O(n) because we will reach each element in the matrix exactly once
![image](https://user-images.githubusercontent.com/25105806/127755521-36e59f55-eb87-483d-b97b-763382c58afb.png)

### Approach 2: Walk in Spiral Order 2, generateMatrixWalkSpiral()
Credits to https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions

The idea is same as approach 1, but use a much more consise code logic to control the right turn: 

`matrix[(row+di)%n][(col+dj)%n]` checks if the next element is already added, the next element means the next element that we will meet in matrix if keep straight. 

If the element has value greater than 0, then we should make a right turn by exchaning the row and col direction(`row_direction, col_direction = col_direction, -row_direction`)

This is a very clever way to control the right turn but it also reduce the readability by a lot.

Time complexity is still O(n):

![image](https://user-images.githubusercontent.com/25105806/127755570-6edd1ebe-a11f-499a-bac6-92d6a1c66ee3.png)
