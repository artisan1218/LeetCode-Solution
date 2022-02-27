# Combination Sum II problem
* Given a collection of candidate numbers (`andidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.
* Each number in `candidates` may only be used **once** in the combination.

Note: The solution set must not contain duplicate combinations.


### Approach 1: Backtracking, combinationSum2Backtrack()
This approach is identical to the probelm combinationSum solved [here](https://github.com/artisan1218/LeetCode-Solution/tree/main/combinationSum) except for the fact that this time we are only allowed using each digit not more than once. So the change here is to add a `start` index that tells the loop where should it start getting numbers from `candidates`, we simply add to `start` by 1 each time we enter a new stack using recursion, which will avoid using a digit multiple times.

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/122664169-82fcdd80-d154-11eb-9c26-ad77151a7ecf.png)


<br />

### Approach 2: Dynamic Programming, combinationSum2DP()
Again, the solution is highly similar to the DP solution in [combinationSum](https://github.com/artisan1218/LeetCode-Solution/tree/main/combinationSum)

The difference is that we now use a hashmap called `count` to count the occurrence of each digit in `candidates` and use it to avoid adding digits multiple times. Besides that, instead of going over the entire original `candidates`, we now only going through the unique digits set of the `candidates` to avoid duplicate combination.

To put another word, a digit can still be used multiple times when building the combination array but we will only add those valid combination arrays to result, which are the combination array whose occurrence of each digits does not exceed the occurrence of corresponding digits in original array

We will build up the `dp` array from `target=1` all the way up to `target=target` and the final result will be stored in `dp[dp.size()-1]`

Time complexity is O(n\*target\*m) where n is the size of `candidates`, target is the size of `target` and m is the size of combination array that adds up to each target from 1 to target.\
Actual running time:

![image](https://user-images.githubusercontent.com/25105806/122664230-01f21600-d155-11eb-82b4-f743fdb6e73d.png)


