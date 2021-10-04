# Scramble String problem
<img width="664" alt="image" src="https://user-images.githubusercontent.com/25105806/135890718-6e82f9df-ccaa-4b27-95f7-cdef1ec9673d.png">

<br />

### Approach 1: DFS, isSameTreeDFS()
The idea is to use DFS to explore two trees `p` and `q` at the same time. If we found at any stage, `p.val != q.val`, we can return False.

Time complexity is O(n) where n is the size of tree:\
<img width="647" alt="image" src="https://user-images.githubusercontent.com/25105806/135891054-6655ae0c-f9d9-4ab6-aa62-0cdfafe386c5.png">
