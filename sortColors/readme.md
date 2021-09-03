# Sort Colors problem
* Given an array nums with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
* We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.
* You must solve this problem without using the library's sort function.


### Approach 1: Naive, sortColorsNaive()
The naive solution is to iterate through the list, move all 0's to the front and move all 2's to the end. There are many ways to implement this and some are quicker due to the implementation of `move` operation. In this solution, even though I only iterate through the list once, the time complexity is still O(n^2) since the `nums.insert()` will take O(n) time. \
![image](https://user-images.githubusercontent.com/25105806/131936278-0243a949-ffc2-40f8-894b-29f371d4e5fc.png)

### Approach 2: One Pointer Two Pass, sortColorsOnePtrTwoPass()
The idea is to move all 0's to the front by swaping, which is O(1), in a first pass and move all 1's to the end of last 0 in the second pass. Since we will only go through the list twice and each swaping operation is O(1). Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/131936510-2e373a1c-72fe-42a9-a197-550c82a9e891.png)

### Approach 3: Two Pointers One Pass, sortColorsTwoPtrsOnePass()
We can use two pointers, one for moving 0's to the front and the other one for moving 2's to the end in one pass. Notice that when moving 2 to the end, we do not change the current cursor index `i` because we need to see if the exchanged value is still 2.\
Time complexity is still O(n):\
![image](https://user-images.githubusercontent.com/25105806/131936683-83fb60c5-0c6f-4e81-b478-a1cf5748f869.png)

### Approach 4: Two Pointers One Pass 2, sortColorsTwoPtrsOnePass2()
Same idea, different implementation than approach 3.\
![image](https://user-images.githubusercontent.com/25105806/131936772-21bba409-becf-49aa-8058-242b09f24c52.png)

### Approach 5: Two Pointers One Pass 3, sortColorsTwoPtrsOnePass3()
Same idea, different implementation than approach 3.\
![image](https://user-images.githubusercontent.com/25105806/131936875-b266183d-9e0a-4b6e-a291-646c646554c6.png)


### Approach 6: Value Assignment, sortColorsValAssign()
Instead of sorting the list by swapping, we can directly modify the value. Just use two variables to store the ending index of 0's and 1's.\
Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/131937003-13aa7f06-cf71-4c0b-8e0e-b54b9533ebc9.png)
