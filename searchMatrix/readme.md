# Search a 2D Matrix problem
* Write an efficient algorithm that searches for a value in an `m x n` matrix. This matrix has the following properties:
* Integers in each row are sorted from left to right.
* The first integer of each row is greater than the last integer of the previous row.
* Return `True` if `target` is found in the matrix, otherwise `False`

### Approach 1: Column First, then Row, searchMatrixColRow()
Since the matrix is sorted, we can first search by the first element in each row, starting at row number 0 until we found a element that is bigger than the  `target`, then the row number will be the previous row index. Then simply search through that row to find the `target`.

Time complexity O(M+N) where M is the number of rows and N is the number of columns:\
![image](https://user-images.githubusercontent.com/25105806/131790088-e53057d3-6735-49e4-9606-0b9dc8ca0817.png)


<br />

### Approach 2: Binary Search, searchMatrixBinarySearch()
Credits to: https://leetcode.com/problems/search-a-2d-matrix/discuss/26220/Don't-treat-it-as-a-2D-matrix-just-treat-it-as-a-sorted-list

Turns out we can treat the sorted matrix as a sorted list in ascending order, each element is greater than the previous value. We only need to convert the index number in the sorted list to coordinates in terms of row index and column index in the matrix.\
`rowIndex = listIndex//rowLen` and `colIndex = listIndex%rowLen`.\
Then simply use binary search to find the `target`

Time complexity is O(logN) where N is the total number of elements in the matrix:\
![image](https://user-images.githubusercontent.com/25105806/131790577-2e9a10c7-79b3-4e76-923e-48f1bea8258d.png)

