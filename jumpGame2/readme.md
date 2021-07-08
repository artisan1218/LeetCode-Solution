# Jump Game II problem
* Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array.
* Each element in the array represents your maximum jump length at that position.
* Your goal is to reach the last index in the minimum number of jumps.
* You can assume that you can always reach the last index.

### Approach 1: Greedy Algorithm, jumpGreedy(), jumpGreedy2()
The idea is to choose the optimal index of jumping for the next jump at each jump and achieve the overall optimal solution.

For example:
```
2, 3, 1, 2, 4, 2, 3
```

We start at index 0 with value 2, we can jump to 3 or 1. Since `3+1` is greater than `1+2`, we choose 3 to be the next jumping index.
Note here the try to optimize `i+nums[i]` instead of just `nums[i]`, this is similar to heuristic search, where we take both length of path that takes us to current spot and the length of next path into account.\
At index 1 with value 3, we can jump to 1, 2, or 4. Since 4 has the greatest value of `i+nums[i]`, we choose 4.\
Then at 4 we can jump to the end.

If we only consider `nums[i]`, think about this example: `5, 4, 3, 2, 1, 1, 0`

Since 4 is the greatest one that we can jump from 5, we choose 4,\
Since 3 is the greatest one that we can jump from 4, we choose 3,\
Since 2 is the greatest one that we can jump from 3, we choose 2,\
...\
This will take more steps than the optimal solution


<br />
Time complexity is O(n):

![image](https://user-images.githubusercontent.com/25105806/124996915-a520a780-dffe-11eb-8335-b67b7fa2a3ed.png)

