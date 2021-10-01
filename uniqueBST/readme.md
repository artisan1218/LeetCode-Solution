# Unique Binary Search Trees problem
![image](https://user-images.githubusercontent.com/25105806/135387175-511bad80-5fa9-4eb8-b362-976c02a8a0ac.png)


### Approach 1: Dynamic Programming, numTrees()
We can find the pattern as follows:

![image](https://user-images.githubusercontent.com/25105806/135387595-dc41348f-7a88-4c59-aa74-053627a32123.png)

`count[n]` means the number of unique BSTs with `n` nodes. Therefore, we can convert this problem to many subproblems.

The key lien of code to solve this is `cur += result[j] * result[i-j-1]`, where we iteratively calculate the number of sub-BSTs given different node as root. We will go through the case where each node between `[1,n]` is the root

Actual running time:

![image](https://user-images.githubusercontent.com/25105806/135387965-96f15b5f-86f6-4683-b8cb-a4fe114aca41.png)
