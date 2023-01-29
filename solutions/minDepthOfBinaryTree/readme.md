# Minimum Depth of Binary Tree problem
![image](https://user-images.githubusercontent.com/25105806/140287305-d24bc143-1f9f-4be5-9546-f0536b865eba.png)

Leetcode link: https://leetcode.com/problems/minimum-depth-of-binary-tree/

<br />

### Approach 1: DFS, minDepth1()
This approach is a kind of brute force solution. We will explore the tree using DFS and update the minimal depth of current subtree every time we reach a leaf node. We use a list `depthList` with only one element to keep track of the minimal depth so far.

```python
def minDepth1(self, root: Optional[TreeNode]) -> int:
    def depth(root, curDepth, depthList):
        if root.left==None and root.right==None: # this is a leaf node
            depthList[0] = min(depthList[0], curDepth)
        else:
            if root.left!=None:
                left = depth(root.left, curDepth+1, depthList)
            if root.right!=None:
                right = depth(root.right, curDepth+1, depthList)

    if root==None:
        return 0
    else:
        depthList = [float('inf')]
        depth(root, 1, depthList)
        return depthList[0]
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/140287691-a8302041-8b0c-44ab-b214-2e35f872d711.png)

<br />

### Approach 2: DFS, minDepth2()
Credits to: https://leetcode.com/problems/minimum-depth-of-binary-tree/solution/210711

This is solution is similar to approach 1 but more concise. The structure is similar to the code of calculating 'maxDepth' of a binary tree. The difference is that we need to consider the case where a node has only left subtree or right subtree, otherwise the minimal depth will just be 1 since we're taking the minimal of all subtrees. The workaround is just skip those cases.

```python
def minDepth2(self, root: Optional[TreeNode]) -> int:
    if root==None:
        return 0
    else:
        if root.left==None:
            return self.minDepth2(root.right) + 1 # left node is none, only counting right node
        elif root.right==None:
            return self.minDepth2(root.left) + 1 # right node is none, only counting left node
        else:
            # counting both and take minimal if both left and right are non-null
            left = self.minDepth2(root.left) + 1
            right = self.minDepth2(root.right) + 1
            return min(left, right)
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/140288146-a8404de6-1d6d-47af-b356-7a42f7a1a68d.png)


