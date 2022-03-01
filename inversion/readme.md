# Jump Game problem
* Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array.
* Each element in the array represents your maximum jump length at that position.
* Determine if you are able to reach the last index.

Leetcode link: https://leetcode.com/problems/jump-game/

<br />

### Approach 1: Greedy Algorithm, canJumpGreedy()
The idea is identical to [Jump Game II](https://github.com/artisan1218/LeetCode-Solution/tree/main/jumpGame2) except for the fact that we are now only interested in whether we can reach the end instead of how (the path)\
So we only need to calcualte the optimal jumping place at each index and move cursor `i` to there and check at the beginning of the loop for where current steps can bring `i` to the end.

```python3
def canJumpGreedy(self, nums: List[int]) -> bool:
    i = 0
    while i<len(nums):
        steps = nums[i]
        if i+steps >= len(nums)-1:
            # can jump
            return True
        best_choice = 0
        max_heuristic = 0
        for choice in range(1, steps+1):
            # choose the best jumping distance
            heuristic = choice+nums[i+choice]
            if heuristic >= max_heuristic:
                max_heuristic = heuristic
                best_choice = choice
        if max_heuristic==0:
            return False
        # jump to this index
        i = i + best_choice
```

Time complexity is O(n):\
![d3256e6f0a62871c9d234814175c93d](https://user-images.githubusercontent.com/25105806/127102899-e3555c77-a927-4e95-a9c7-e2d9976ab97a.png)

<br />

### Approach 2: Backtracking, canJumpBacktracking()
Backtracking can be applied here, which is similar to how we human solve this question: simply try all possible steps that we can take at each index and return the result. If all steps in current index do not bring us to the end, we should go back and iterate over next step.

```python3
def canJumpBacktracking(self, nums: List[int]) -> bool:
    return self.backtrack(0, nums)

def backtrack(self, i, nums):
    if i+nums[i]>=len(nums)-1:
        return True
    else:
        # go over all steps that we can jump at index i
        for step in range(1, nums[i]+1):
            if self.backtrack(i+step, nums):
                return True
        # if all steps at this index do not jump to the end, then try next step
        return False
```

Since this solution will traverse all possibilies until we've found a solution, this is very slow and lead to TLE :(
