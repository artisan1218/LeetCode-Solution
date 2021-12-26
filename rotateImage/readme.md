# Rotate Image problem
* You are given an `n x n` 2D `matrix` representing an image, rotate the image by 90 degrees (clockwise).
* You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

  ![image](https://user-images.githubusercontent.com/25105806/125137755-2ee57900-e0c2-11eb-83b2-ac03ffc25329.png)

Leetcode link: https://leetcode.com/problems/rotate-image/

<br />

### Approach 1: List Comprehension, rotateListComprehension()
Use list compresion to do the conversion: `[[1,2,3],[4,5,6],[7,8,9]]` will be rotated to `[[7,4,1],[8,5,2],[9,6,3]]`. That is, the first element in each row in the original `matrix` in reverse order, then second element, then third element.

```python3
def rotateListComprehension(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # [::] will modify the matrix in-place
    matrix[::] = [[row[i] for row in reversed(matrix)] for i in range(len(matrix))]
```

Running time:\
![image](https://user-images.githubusercontent.com/25105806/125138371-643e9680-e0c3-11eb-8620-33fa35c67aca.png)



<br />


### Approach 2: Zip, rotateZip()
This approach is similar to approach 1, but use the built-in `zip` function of python to obtain the vertical row of the matrix.

```python3
def rotateZip(self, matrix: List[List[int]]) -> None:
    matrix[::] = [list(num) for num in zip(*reversed(matrix))]
```

Running time:\
![image](https://user-images.githubusercontent.com/25105806/125138405-6dc7fe80-e0c3-11eb-9710-1b3722c1c11d.png)

<br />

### Approach 3: Common Method for Rotating, rotate()
Credits to: https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image

Turns out we can first flip the matrix upside down and swap the elements along the diagonal
```
first reverse up to down, then swap the symmetry 
1 2 3     7 8 9     7 4 1
4 5 6  => 4 5 6  => 8 5 2
7 8 9     1 2 3     9 6 3
```

```python3
def rotate(self, matrix: List[List[int]]) -> None:
    '''
    clockwise rotate
    first reverse up to down, then swap the symmetry 
    1 2 3     7 8 9     7 4 1
    4 5 6  => 4 5 6  => 8 5 2
    7 8 9     1 2 3     9 6 3
    '''
    #reverse matrix upside down
    matrix[::] = matrix[::-1]
    #swap the symmetry
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]        
```

Time complexity is O(m) where m is the number of digits in the matrix, running time:\
![image](https://user-images.githubusercontent.com/25105806/125138419-74567600-e0c3-11eb-8aeb-d18b0e47a180.png)



