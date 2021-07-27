# Jump Game problem
* Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array.
* Each element in the array represents your maximum jump length at that position.
* Determine if you are able to reach the last index.

### Approach 1: Greedy Algorithm, canJumpGreedy()
The idea is identical to [Jump Game II](https://github.com/artisan1218/LeetCode-Solution/tree/main/jumpGame2) except for the fact that we are now only interested in whether we can reach the end instead of how (the path)\
So we only need to calcualte the optimal jumping place at each index and move cursor `i` to there and check at the beginning of the loop for where current steps can bring `i` to the end\

Time complexity is O(n):

![d3256e6f0a62871c9d234814175c93d](https://user-images.githubusercontent.com/25105806/127102899-e3555c77-a927-4e95-a9c7-e2d9976ab97a.png)

### Approach 2: Backtracking, canJumpBacktracking()
Backtracking can be applied here, which is similar to how we human solve this question: simply try all possible steps that we can take at each index and return the result. If all steps in current index do not bring us to the end, we should go back and iterate over next step.

Since this solution will traverse all possibilies until we've found a solution, this is very slow and lead to TLE :(
