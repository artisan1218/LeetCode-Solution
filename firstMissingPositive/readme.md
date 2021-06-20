# First Missing Positive problem
* Given an unsorted integer array `nums`, find the smallest missing positive integer.

You must implement an algorithm that runs in `O(n)` time and uses `constant extra space`.

### Approach 1: Naive, HashSet, firstMissingPositiveHashSet()
This not a O(1) space complexity solution, but it is the most straight-forward solution. We first cache all numbers in `nums` in hash set and iteratively check for the first non-existing positive using a loop.

Since the hashset provides constant lookup time, it only takes O(n) time to check all number in the `nums`:\
![image](https://user-images.githubusercontent.com/25105806/122690288-77a1c480-d1dd-11eb-81e8-f7804cba77d7.png)


<br />

### Approach 2: Change In-Place, firstMissingPositive()
Credits to https://leetcode.com/problems/first-missing-positive/discuss/17214/Java-simple-solution-with-documentation

This approach takes advantage of two insights:
1. Numbers greater then length of `nums` can be ignored because the missing integer must be in the range `[1, length+1]`
2. If each cell in the array were to contain positive integers only, we can use the negative of the stored number as a flag to mark something (in this case the flag indicates this index was found in some cell of the array)


e.g. `nums=[2,1,7,8,9,11,12]`

We first traverse the nums and keep only number within range `[1, length+1]`. For the numbers that are not in this range, we change it to length+1
```
2 1 7 8 9 11 12
      ↓
2 1 7 8 8 8 8
```

Then we will change the value of a number to negtive if it is in range `[1, length+1]`, but we do not change them in same index but the index as if they were properly placed in an continuous and 0-based index array
```
2   1   7   8   8   8   8
            ↓
-2  -1  7   8   8   8   -8
```
Steps: 
1. first read 2, 2 is within the range and it is **supposed** to be placed at index 1(because 2-1) of a continuous array. So set number at index 1 to be negative
    ```
    2  -1  7   8   8   8   8
    ```
2. read -1, take absolute value 1, 1 is within the range and it is **supposed** to be placed at index 0(becasue 1-1) of a continuous array. So set number at index 0 to be negative. 
    ```
    -2  -1  7   8   8   8   8
    ```
3. read 7, 7 is within the range and it is **supposed** to be placed at index 6(because 7-1) of a continuous array. So set number at index 6 to be negative. 
    ```
    -2  -1  7   8   8   8   -8
    ```
4. read 8, 8 is not within the range, skip
5. read 8, 8 is not within the range, skip
6. read 8, 8 is not within the range, skip
7. read -8, take absolute value 8, 8 is not within the range, skip

Then simply check for the first number that is positive, the index of that number plus 1 will be the answer because we've replaced any existing number in range 1 to len + 1 with negative value at it's corresponding index **as if** the array is continuous.

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/122690803-65755580-d1e0-11eb-835e-0f815d509726.png)


