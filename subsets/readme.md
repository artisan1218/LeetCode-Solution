# Subsets problem
* Given an integer array `nums` of unique elements, return all possible subsets (the power set).


### Approach 1: Backtracking, backtrack()
This idea is similar to [combinations](https://github.com/artisan1218/LeetCode-Solution/tree/main/combinations) problem. We just need a loop that loops through all different length and get all combinations for all lengths.\
Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/132104051-670a7f93-10e1-4546-8b7c-aded3eb70bfb.png)


<br />

### Approach 2: Cascading, subsetsCascading()
The idea can bu summaried by the image below:\
![image](https://user-images.githubusercontent.com/25105806/132104075-2862fbcd-c983-49a1-9a69-10bcaa21911c.png)


Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/132104095-5c4e3987-d82b-4227-821c-ecd713acded6.png)







