# Combination Sum II problem
* Given a collection of candidate numbers (`andidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.
* Each number in `candidates` may only be used **once** in the combination.

Note: The solution set must not contain duplicate combinations.

Leetcode link: https://leetcode.com/problems/combination-sum-ii/

<br />

### Approach 1: Backtracking, combinationSum2Backtrack()
This approach is identical to the probelm combinationSum solved [here](https://github.com/artisan1218/LeetCode-Solution/tree/main/combinationSum) except for the fact that this time we are only allowed using each digit not more than once. So the change here is to add a `start` index that tells the loop where should it start getting numbers from `candidates`, we simply add to `start` by 1 each time we enter a new stack using recursion, which will avoid using a digit multiple times.

```java
public List<List<Integer>> combinationSum2Backtrack(int[] candidates, int target) {
    List<List<Integer>> result = new ArrayList<>();
    List<Integer> combination = new ArrayList<>();
    int sum = 0;

    backtrack(candidates, target, result, combination, sum, 0);
    // this is to remove duplicates combinations
    Set<List<Integer>> unique = new HashSet<>();
    for (List<Integer> comb : result) {
      Collections.sort(comb);
      unique.add(comb);
    }
    return new ArrayList<>(unique);
}

public boolean backtrack(int[] candidates, int target, List<List<Integer>> result, List<Integer> combination,
  int sum, int start) {

    // go over each digit starting at index 'start' in the list so that we will not
    // double counting same digit
    for (int i = start; i < candidates.length; i++) {
      int digit = candidates[i];
      if ((sum + digit) < target) {
          // if adding the current digit does not exceed the target, we can add it safely
          combination.add(digit);
          sum += digit;
          // keeping checking the rest of the digit until an adding exceeds the target
          // or all digits are seen
          if (!backtrack(candidates, target, result, combination, sum, i + 1)) {
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
![image](https://user-images.githubusercontent.com/25105806/122664169-82fcdd80-d154-11eb-9c26-ad77151a7ecf.png)


<br />

### Approach 2: Dynamic Programming, combinationSum2DP()
Again, the solution is highly similar to the DP solution in [combinationSum](https://github.com/artisan1218/LeetCode-Solution/tree/main/combinationSum)

The difference is that we now use a hashmap called `count` to count the occurrence of each digit in `candidates` and use it to avoid adding digits multiple times. Besides that, instead of going over the entire original `candidates`, we now only going through the unique digits set of the `candidates` to avoid duplicate combination.

To put another word, a digit can still be used multiple times when building the combination array but we will only add those valid combination arrays to result, which are the combination array whose occurrence of each digits does not exceed the occurrence of corresponding digits in original array

We will build up the `dp` array from `target=1` all the way up to `target=target` and the final result will be stored in `dp[dp.size()-1]`


```java
public List < List < Integer >> combinationSum2DP(int[] candidates, int target) {
    // count candidates
    Map < Integer, Integer > freq = new HashMap < > ();
    for (int digit: candidates) {
        if (freq.containsKey(digit)) {
            freq.put(digit, freq.get(digit) + 1);
        } else {
            freq.put(digit, 1);
        }
    }

    List < List < List < Integer >>> dp = new ArrayList < > ();
    // currTarget begins at 1 because the condition 1 <= target <= 500
    for (int currTarget = 1; currTarget <= target; currTarget++) {
        List < List < Integer >> row = new ArrayList < > ();
        // go over the unique candidates that we can choose digit from
        // use the candidates set that consist of only unique digits
        // a digit can still be used multiple times when building the combination array
        // but we will only add those valid combination arrays to result, which are the
        // combination array whose occurrence of each digits does not exceed the
        // occurrence of corresponding digits in original array
        for (int digit: freq.keySet()) {
            // if a digit is smaller than the current target, we can add it to current
            // combination and looking back for the remaining numbers by checking dp
            if (digit < currTarget) {
                for (List < Integer > prevAns: dp.get(currTarget - digit - 1)) {
                    // to avoid duplicates
                    if (digit <= prevAns.get(0)) {
                        Map < Integer, Integer > count = new HashMap < > ();
                        boolean valid = true;
                        List < Integer > combination = new ArrayList < > ();
                        combination.add(digit);
                        combination.addAll(prevAns);
                        // checking for digits that are used for multiple times
                        for (int check: combination) {
                            if (count.containsKey(check)) {
                                count.put(check, count.get(check) + 1);
                            } else {
                                count.put(check, 1);
                            }
                            // checking if number of uses of a digit exceeds its occurrence
                            if (count.get(check) > freq.get(check)) {
                                valid = false;
                                break;
                            }
                        }
                        if (valid) {
                            row.add(new ArrayList < > (combination));
                        }
                    }
                }
            } else if (digit == currTarget) {
                // case when a single digit is equal to target
                List < Integer > combination = new ArrayList < > ();
                combination.add(digit);
                // add a new copy of the combination so that it will not be changed
                row.add(new ArrayList < > (combination));
            }
        }
        dp.add(new ArrayList < > (row));
    }

    return dp.get(target - 1);
}
```


Time complexity is O(n\*target\*m) where n is the size of `candidates`, target is the size of `target` and m is the size of combination array that adds up to each target from 1 to target.\
Actual running time:

![image](https://user-images.githubusercontent.com/25105806/122664230-01f21600-d155-11eb-82b4-f743fdb6e73d.png)


