# Find Leaves of Binary Tree problem
<img width="689" alt="image" src="https://user-images.githubusercontent.com/25105806/138186311-5ee9c485-077f-4ce9-b4d0-e749a0b29e6c.png">

Leetcode link: https://leetcode.com/problems/find-leaves-of-binary-tree/

<br />

### Approach 1: DFS, findLeaves1()
The idea is to use DFS to traverse the entire tree and keep track of the height of current subtree along the way, so that we know which is leaf node. Then simply use a `result` list with it's index to be the level of leaf node to hold all results.

Note that the variable `height` means the height of subtree, which is the number of levels of its children, not depth

```python
def findLeaves1(self, root: Optional[TreeNode]) -> List[List[int]]:
    result = []

    def dfs(root):
        if root==None:
            return 0
        else:
            height = max(dfs(root.left), dfs(root.right))
            if height >= len(result):
                result.append([])
            result[height].append(root.val)
            return height+1

    dfs(root)
    return result
```
Time complexity is O(n), where n is the number of nodes in the tree `root`:\
<img width="669" alt="image" src="https://user-images.githubusercontent.com/25105806/138186595-1fabea90-b169-4742-967e-5cb7940cfcc4.png">

<br />

### Approach 2: DFS, findLeaves2()
The idea is to first use DFS to find all lead nodes, which are the nodes whose left and right children are all `None`, then remove the all leaves and find new leaves until all nodes are removed. The key is to update left and right branch as we traverse the tree, either return `None`(remove) or return itself (not remove) 

```python
def findLeaves2(self, root: TreeNode) -> List[List[int]]:
    leaves = []
    result = []

    def removeLeaves(root):
        if root!=None:
            if root.left==None and root.right==None:  # a leaf node
                leaves.append(root.val)
                return None # return None means we've removed the current lead node
            else:
                # root.left and root.right will be None if it's a leat node
                root.left = removeLeaves(root.left) 
                root.right = removeLeaves(root.right)
                return root # otherwise return itself, do nothing to the node

    while root!=None:
        root = removeLeaves(root)
        result.append(leaves)
        leaves = []

    return result
```

Time complexity is O(n), where n is the number of nodes in the tree `root`:\
<img width="665" alt="image" src="https://user-images.githubusercontent.com/25105806/138186759-3483f99f-214a-4838-95ad-bb92cee67fc6.png">
