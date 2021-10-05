# Binary Tree Level Order Traversal problem
![image](https://user-images.githubusercontent.com/25105806/135959044-2e29e7f5-0ff8-4524-b092-7bcc5a8d91df.png)

<br />

### Approach 1: BFS, levelOrder1()
The approach uses two list `level` and `nextLevel` to hold the nodes in current level and next level, so that we don't mix them together. 

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/135959177-22711919-b83c-4649-a66e-5a43a7bd7cf4.png)

<br />

### Approach 2: BFS, levelOrder2()
Instead of using two list, we can instead using only one queue. But we need to get the length of each level at the beginning of loop so that we don't mix them up with the nodes on the next level

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/135959285-5c415451-324c-4e50-9957-152bfb79ee48.png)
