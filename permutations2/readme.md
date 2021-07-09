# Permutations II problem
* Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permutations in any order.

### Approach 1: DFS, permuteUnique()
The idea is very similar to [Permutations](https://github.com/artisan1218/LeetCode-Solution/tree/main/permutations), the only difference is that, when there are duplicates, we simply skip it. The main structure remians the same as [Permutations](https://github.com/artisan1218/LeetCode-Solution/tree/main/permutations), but we use another variable of set to determine the uniqueness of a new number.

Running time:

![image](https://user-images.githubusercontent.com/25105806/125022296-3741a380-e031-11eb-94b4-8eac954da88a.png)

