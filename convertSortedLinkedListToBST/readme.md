# Convert Sorted List to Binary Search Tree problem
![image](https://user-images.githubusercontent.com/25105806/136265678-ea7faf58-ea09-45af-9e0e-0d76e35ed259.png)

<br />

### Approach 1: Convert to List, sortedListToBST()
The idea is based on [convertSortedAryToBST](https://github.com/artisan1218/LeetCode-Solution/tree/main/convertSortedAryToBST) and easy to think of. Simply convert the linked list to a list, and use the same approach as convertSortedAryToBST to solve this.

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/136265953-7bba2928-f03a-423b-bb37-d5950a6fb318.png)


### Approach 1: Inorder Simulation, sortedListToBST()

![image](https://user-images.githubusercontent.com/25105806/136266096-9aface95-4183-4447-80b7-97e68aaec3d1.png)
![image](https://user-images.githubusercontent.com/25105806/136266159-3c261487-e44a-4dd8-ba2d-47e4ab013239.png)
![image](https://user-images.githubusercontent.com/25105806/136266184-99df86e0-ac06-4b28-9639-34a59b9be04d.png)

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/136266353-a0709edf-0e0c-4ae8-8828-f6ded9d6a2a4.png)
