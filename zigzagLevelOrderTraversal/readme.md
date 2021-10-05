# Binary Tree Zigzag Level Order Traversal problem
![image](https://user-images.githubusercontent.com/25105806/135959482-4e9db087-7ec6-4300-beba-708fab26fe28.png)

<br />

### Approach 1: zigzagLevelOrder()
This solution is based on [levelOrderTraversal](https://github.com/artisan1218/LeetCode-Solution/tree/main/levelOrderTraversal) but use another variable to mark in which order should we add the node in current level in the `result` list, then simply alternating the order

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/135959603-8349b72a-e499-47a7-be5b-dd0ce965ec60.png)
