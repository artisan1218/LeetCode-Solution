# Symmetric Tree problem
<img width="648" alt="image" src="https://user-images.githubusercontent.com/25105806/135892405-0eea0e18-d62c-4294-beb3-f0408300a1ef.png">

### Approach 1: DFS, isSymmetric()
The idea is adapt the code from [sameTree](https://github.com/artisan1218/LeetCode-Solution/tree/main/sameTree), because we can consider the left subtree as `p` and right subtree as `q`. The only difference is that, when traverse over the tree, two subtrees need different order as they are 'mirror': `sameTree(p.left, q.right) and sameTree(p.right, q.left)`

Time complexity is O(n):\
<img width="642" alt="image" src="https://user-images.githubusercontent.com/25105806/135892910-0847a735-242e-4330-9402-62f5b0d97ff5.png">


