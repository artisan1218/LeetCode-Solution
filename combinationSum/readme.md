# Combination Sum problem
* Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in **any order**.
* The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
* It is guaranteed that the number of unique combinations that sum up to `target` is less than 150 combinations for the given input.

![image](https://user-images.githubusercontent.com/25105806/145903163-72c1df11-4dea-4923-8a4a-970f7db8604b.png)

Leetcode link: https://leetcode.com/problems/combination-sum/

<br/>

### Approach 1: Backtracking, combinationSumBacktrack()
This approach uses the technique called backtracking, which we will exhaust **every single permutation of digits** in `candidates` to cover all the possibilities that can add up to `target`. First I iterate through the `candidates` and pick a number in order, if the number plus current result is smaller than target, then we can add it safely and add another number recursively. If adding a number will exceed the `target`, we should return and backtrack the previous adding simply by removing it from the result list. This way, we can cover all possible permutations of any length of the `candidates`. Then we will remove duplicates and return the result.

This is pretty similar to how we human find the combination sum: simply list all possible pairs

```java
public List<List<Integer>> combinationSumBacktrack(int[] candidates, int target) {
    List<List<Integer>> result = new ArrayList<>();
    List<Integer> combination = new ArrayList<>();
    int sum = 0;

    backtrack(candidates, target, result, combination, sum);
    // this is to remove duplicates combinations
    Set<List<Integer>> unique = new HashSet<>();
    for (List<Integer> comb : result) {
    Collections.sort(comb);
    unique.add(comb);
    }
    return new ArrayList<>(unique);
}

public boolean backtrack(int[] candidates, int target, List<List<Integer>> result, List<Integer> combination,
    int sum) {

    // go over each digit in the list
    for (int digit : candidates) {
    if ((sum + digit) < target) {
        // if adding the current digit does not exceed the target, we can add it safely
        combination.add(digit);
        sum += digit;
        // keeping checking the rest of the digit until an adding exceeds the target
        // or all digits are seen
        if (!backtrack(candidates, target, result, combination, sum)) {
        // an adding is not successful, start backtracking by removing the current digit
        sum -= digit;
        combination.remove(combination.size() - 1);
        }
    } else if ((sum + digit) == target) {
        // we've found a combination, add the combination to result and check the next
        // digit
        combination.add(digit);
        result.add(new ArrayList<>(combination));
        combination.remove(combination.size() - 1);
    }
    }
    return false;
}
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/122658931-60a09b00-d127-11eb-8c3e-90c6f97d79b7.png)

<br />

### Approach 2: Dynamic Programming, combinationSumDP()
Credits to: https://www.youtube.com/watch?v=AUIfTelAGVc and https://leetcode.com/problems/combination-sum/discuss/16509/Iterative-Java-DP-solution

The DP idea is build a 2d array `dp` where each column represents the number from 1 up to `target` and each row represents the digits in `candidates`. Each slot in 2d array is a list combination of numbers that add up to the corresponding target number in that row. 
```
candidates=[1,2,3,6], target=3
so we list target from 1 up to 3 and all candidates

    1       2     3     6
1  [1]      []    []    []
2  [1,1]    [2]   []    []
3  [1,1,1,] [2,1] [3]   []

```


![combinationSumAnimation](https://user-images.githubusercontent.com/25105806/122659346-1e2d8d00-d12c-11eb-9fca-6d4bbb99cd31.gif)

**Note: Click [here](https://github.com/artisan1218/LeetCode-Solution/tree/main/combinationSum) to download the animation to play for yourself**

<br />

```java
public List<List<Integer>> combinationSumDP(int[] candidates, int target) {
    List<List<List<Integer>>> dp = new ArrayList<>();

    // currTarget begins at 1 because the condition 1 <= target <= 500
    for (int currTarget = 1; currTarget <= target; currTarget++) {
    List<List<Integer>> row = new ArrayList<>();
    // go over the candidates that we can choose digit from
    for (int digit : candidates) {
        // if a digit is smaller than the current target, we can add it to current
        // combination and looking back for the remaining numbers by checking dp
        if (digit < currTarget) {
        for (List<Integer> prevAns : dp.get(currTarget - digit - 1)) {
            // to avoid duplicates
            if (digit <= prevAns.get(0)) {
            List<Integer> combination = new ArrayList<>();
            combination.add(digit);
            combination.addAll(prevAns);
            row.add(new ArrayList<>(combination));
            }
        }
        } else if (digit == currTarget) {
        // case when a single digit is equal to target
        List<Integer> combination = new ArrayList<>();
        combination.add(digit);
        // add a new copy of the combination so that it will not be changed
        row.add(new ArrayList<>(combination));
        }
    }
    dp.add(new ArrayList<>(row));
    }

    return dp.get(target - 1);
}
```

We will build up the `dp` array from `target=1` all the way up to `target=target` and the final result will be stored in `dp[dp.size()-1]`

Time complexity is O(n\*target\*m) where n is the size of `candidates`, target is the size of `target` and m is the size of combination array that adds up to each target from 1 to target.\
Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/122659149-8cbd1b80-d129-11eb-8d96-65b84bf0606b.png)


