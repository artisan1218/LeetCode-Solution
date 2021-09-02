# Set Matrix Zeroes problem
* Given an `m x n` integer matrix matrix, if an element is `0`, set its entire row and column to `0`'s, and return the matrix.
* You must do it in place.


### Approach 1: Naive, Space(M\*N), setZeroesSpaceMN()
The challenge of this problem is that changing one row and column to zero's without remembering all the places of zero will affect the remaining numbers. The simplest way to do this is to store all the positions of zeros and set the corresponding row and column to 0's one by one.
This therefore requires O(m\*n) space complexity

![image](https://user-images.githubusercontent.com/25105806/131763395-59175464-e258-4bb3-83df-d99dfdef1ede.png)


<br />

### Approach 2: Space(M+N), setZeroesSpaceMPlusN()
Turns out it only requires one 0 in each row, each column to set all numbers of that row and column to 0. So we can only store the number of rows and columns that contains 0 and change them one by one because storing more than one 0 in each row or column does not change the result, so only store one 0 to save space. The worst case is we store M+N 0's. So the space complexity is O(M+N)
![image](https://user-images.githubusercontent.com/25105806/131763633-0155c1ae-c037-4af1-a7ae-6b168919f8c1.png)

<br />

### Approach 3: Constant Space, setZeroesConstantSpace()
The most space efficient way to do this is to first determine whether there are 0's in the first row and first column by using two boolean variables.\
Consider the matrix below, there is a 0 in the first column and there is no 0 at the first row:\
<img src="https://user-images.githubusercontent.com/25105806/131764345-b1d9a74e-077f-4a05-b9d8-eaddb4ec7b62.jpg" width="50%" height="50%">

Go over the entire matirx, if the current value is 0, then that means we need to change the entire row and column to be 0, but in order to mantain the matrix so that the remaining numbers will not be confused by the 0's set by us and 0's come with the matrix, we only set the first element in that row and column to be 0. Since we've already remembered whether there are 0's in the first row and column, this will not affect the first row and column.\
Note that the blue 0's are all in the first row or column corresponed to the 0's in the matrix.\
<img src="https://user-images.githubusercontent.com/25105806/131764673-27ed6218-e8a8-4474-8114-97dd760df46c.jpg" width="50%" height="50%">

Then at starting at position `[1,1]` of the `matrix` (skipping first row and column and we will deal with them later), go over the entire matirx, if the first element of the corresponding row and column is 0, change this value to be 0.\
The green 0's are set because there is a 0 either at the first element of that row or first element of that column.\
<img src="https://user-images.githubusercontent.com/25105806/131764843-a8ea04a6-cd11-4ad0-8ca8-3c90fcc7618f.jpg" width="50%" height="50%">

Finally, check if there are zero's in the first column or row by looking at the boolean value of the two variables. If true, then set the entire row or column to be zero's as well.\
Yellow 0's are set because there is at least one 0 at the first column, this is known by checking the boolean variable `colZero`.\
<img src="https://user-images.githubusercontent.com/25105806/131764939-55888fc6-2012-4b7c-91fc-bb552cde90bb.jpg" width="50%" height="50%">


Since we do not store any positional information about the 0's, we use only constant space:\
![image](https://user-images.githubusercontent.com/25105806/131764106-ff5ebfc5-4e31-4af7-bd19-925e5908326f.png)

