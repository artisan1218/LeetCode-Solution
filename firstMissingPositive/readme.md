# First Missing Positive problem
* Given an unsorted integer array `nums`, find the smallest missing positive integer.

You must implement an algorithm that runs in `O(n)` time and uses `constant extra space`.

Leetcode link: https://leetcode.com/problems/first-missing-positive/

<br />

### Approach 1: Naive, HashSet, firstMissingPositiveHashSet()
This not a O(1) space complexity solution, but it is the most straight-forward solution. We first cache all numbers in `nums` in hash set and iteratively check for the first non-existing positive using a loop.

```java
public int firstMissingPositiveInplaceHashing(int[] nums) {
    int len = nums.length;

    // if a number is < 0 or > len, we can replace it with a special number len + 1
    // the number is impossible to be the answer. The answer must be within the
    // range 1 and len + 1
    for (int i = 0; i < len; i++) {
      if (nums[i] <= 0 || nums[i] > len) {
          nums[i] = len + 1;
      }
    }

    for (int i = 0; i < len; i++) {
      // take abs value of any number read to compare it with the len
      int num = Math.abs(nums[i]);
      // is a number is smaller or equal to len, it will be in the range of 1 to len +
      // 1
      if (num <= len) {
          // then convert it to zero index based array
          // e.g. 2 will be placed at index 1 if the array is continues
          num--;
          // if the 0-based index has a pos number, we convert it to neg number to mark it
          // as "exist"
          if (nums[num] > 0) { // prevents double negative operations
            // convert it to neg because it keeps the magnitude of the original number
            // we can simply restore its original value and compare it with len by taking
            // abs value of it
            nums[num] = -1 * nums[num];
          }
      }
    }

    // the first number whose positive will be the answer because we've replaced any
    // existing number in range 1 to len + 1 with neg value at it's corresponding
    // index as if the array is continues
    for (int i = 0; i < len; i++) {
      if (nums[i] >= 0) {
          return i + 1;
      }
    }

    // every number is within the range of 1 to len + 1, simply return len + 1,
    // which is the next number
    return len + 1;
}
```

Since the hashset provides constant lookup time, it only takes O(n) time to check all number in the `nums`:\
![image](https://user-images.githubusercontent.com/25105806/122690288-77a1c480-d1dd-11eb-81e8-f7804cba77d7.png)


<br />

### Approach 2: Change In-Place, firstMissingPositiveInplaceHashing()
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

```java
public int firstMissingPositiveHashSet(int[] nums) {
    // cache the nums using HashSet
    Set<Integer> existence = new HashSet<>();
    for (int num : nums) {
      existence.add(num);
    }
    // checking for non-existing least positive integer
    for (int i = 1; true; i++) {
      if (!existence.contains(i)) {
          return i;
      }
    }
}
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/122690803-65755580-d1e0-11eb-835e-0f815d509726.png)


