# Recover Binary Search Tree problem
<img width="647" alt="image" src="https://user-images.githubusercontent.com/25105806/135798681-1922443d-3ec8-48f0-b301-ec1e6129110b.png">

### Approach 1: DFS, recoverTree()
Since we only need to swap two mistaken nodes'value, if we do the inorder traversal, we can find that all values are in ascending order except for the two mistake node. Our job is to find the two targets and swap them.

We can use a simple DFS in-order traversal to explore all nodes in ascending order, this make sure that we only need to compare a node with its predecessor. Then update the first mistake target and second mistake target as we explore the nodes.

Time complexity is O(n):\
<img width="629" alt="image" src="https://user-images.githubusercontent.com/25105806/135799041-8fa4a95e-8d8f-4409-b535-eeb2e645798c.png">

