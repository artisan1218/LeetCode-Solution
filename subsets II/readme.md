# Subsets II problem
* Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).
* The solution set must not contain duplicate subsets. Return the solution in any order.


### Approach 1: Generate All and Remove Dup, subsetsWithDupRemoveDupSubsets()
This solution is a brute force solution, we first generate all subsets like what we did in [subset](https://github.com/artisan1218/LeetCode-Solution/tree/main/subsets), then use `set` to remove any duplicate results.

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/134554504-7d213786-fb7c-4c00-9025-0567fd915500.png)


### Approach 2: DFS, subsetsWithDupDFS()
This solution is optimal one, which we still use DFS to exhaust all possible solutions, but add pruning conditions to prevent explore duplicate elements:
```
if i > start and nums[i] == nums[i-1]:
    continue
```

Actural running time:\
![image](https://user-images.githubusercontent.com/25105806/134554935-fc255db8-3ce3-4a4e-b130-8b38bfc528d2.png)
