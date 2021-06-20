# Combination Sum problem
* Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in **any order**.
* The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
* It is guaranteed that the number of unique combinations that sum up to `target` is less than 150 combinations for the given input.


### Approach 1: Backtracking, combinationSumBacktrack()
This approach uses the technique called backtracking, which we will exhaust **every single permutation of digits** in `candidates` to cover all the possibilities that can add up to `target`. First I iterate through the `candidates` and pick a number in order, if the number plus current result is smaller than target, then we can add it safely and add another number recursively. If adding a number will exceed the `target`, we should return and backtrack the previous adding simply by removing it from the result list. This way, we can cover all possible permutations of any length of the `candidates`. Then we will remove duplicates and return the result.

This is pretty similar to how we human find the combination sum: simply list all possible pairs

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/122658931-60a09b00-d127-11eb-8c3e-90c6f97d79b7.png)

<br />

### Approach 2: Dynamic Programming, combinationSumDP()
Credits to: https://www.youtube.com/watch?v=AUIfTelAGVc and https://leetcode.com/problems/combination-sum/discuss/16509/Iterative-Java-DP-solution

The DP idea is build a 2d array `dp` where each column represents the number from 1 up to `target` and each row represents the digits in `candidates`. Each slot in 2d array is a list combination of numbers that add up to the corresponding target number in that row. 

![combinationSumAnimation](https://user-images.githubusercontent.com/25105806/122659346-1e2d8d00-d12c-11eb-9fca-6d4bbb99cd31.gif)

**Note: Click [here](https://github.com/artisan1218/LeetCode-Solution/tree/main/combinationSum) to download the animation to play for yourself**

<br />

```
candidates=[1,2,3,6], target=3
so we list target from 1 up to 3 and all candidates

    1       2     3     6
1  [1]      []    []    []
2  [1,1]    [2]   []    []
3  [1,1,1,] [2,1] [3]   []

```

We will build up the `dp` array from `target=1` all the way up to `target=target` and the final result will be stored in `dp[dp.size()-1]`

Time complexity is O(n\*target\*m) where n is the size of `candidates`, target is the size of `target` and m is the size of combination array that adds up to each target from 1 to target.\
Actual running time:

![image](https://user-images.githubusercontent.com/25105806/122659149-8cbd1b80-d129-11eb-8d96-65b84bf0606b.png)


