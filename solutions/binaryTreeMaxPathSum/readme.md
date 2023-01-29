# Binary Tree Maximum Path Sum problem
![image](https://user-images.githubusercontent.com/25105806/152286835-2b8b8d3c-37f9-48bc-9ea5-8b4133ad6ae8.png)

Leetcode link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

<br />

### Approach 1: Brute Force, maxPathSumBruteForce()
Since we need not only the children node but also the parent node, we can first construct an adjacent matrix containing all nodes as key and their parent, left and right node as values. This way, we can keep track of all nodes. Then simply use recursion to explore all possible paths starting at each node and record the max sum value.

```python3
def maxPathSumBruteForce(self, root: Optional[TreeNode]) -> int:
    def getAdjMatrix(parent, cursor):
        if cursor !=None:
            adjMatrix[cursor] = [parent, cursor.left, cursor.right]
            getAdjMatrix(cursor, cursor.left)
            getAdjMatrix(cursor, cursor.right)

    def findMaxPath(adjMatrix, root, curMax, visited):
        visited.add(root)
        curMax+=root.val
        self.max = max(self.max, curMax)

        parent, left, right = adjMatrix[root][0], adjMatrix[root][1], adjMatrix[root][2]
        if (parent in visited or parent is None) and (left in visited or left is None) and (right in visited or right is None):
            self.max = max(self.max, curMax)
        else:
            if parent not in visited and parent:
                visited.add(parent)
                findMaxPath(adjMatrix, parent, curMax, visited)
                visited.remove(parent)

            if left not in visited and left:
                visited.add(left)
                findMaxPath(adjMatrix, left, curMax, visited)
                visited.remove(left)

            if right not in visited and right:
                visited.add(right)
                findMaxPath(adjMatrix, right, curMax, visited)
                visited.remove(right)

    adjMatrix = dict()
    getAdjMatrix(None, root)
    self.max = float('-inf')
    for subroot in adjMatrix.keys():
        findMaxPath(adjMatrix, subroot, 0, set())

    return self.max
```

This solution leads to TLE and the time complexity is O(n^2)

<br />

### Approach 2: Recursion, maxPathSumRecursion()
Credits to: https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/er-cha-shu-zhong-de-zui-da-lu-jing-he-by-leetcode-/ and https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram

The idea is to compute the max gain we can get from each sub-tree, then add up the gains from each sub-tree to find the max path sum. When computing the max gain, the max path sum is simply the value sum of parent node, left child and right child. However, the max gain for this subtree is the value of `parent.val + max(left.val, right.val)' because we cannot traverse all nodes in a sub-branch from another sub-branch. 

```python3
def maxPathSumRecursion(self, root: Optional[TreeNode]) -> int:
    self.maxSum = float('-inf')
    def maxGain(node):
        if not node:
            return 0 # 
        else:
            leftGain = max(maxGain(node.left), 0) 
            rightGain = max(maxGain(node.right), 0)

            # the max path sum we can get is the sum of all values of parent, left and right
            pathSum = node.val + leftGain + rightGain 
            self.maxSum = max(self.maxSum, pathSum)

            # however, when we return the maxGain for a branch, the value should be parent + left OR parent + right
            # because we cannot traverse all nodes in a sub-branch from another sub-branch
            return node.val + max(leftGain, rightGain) 

    maxGain(root)
    return self.maxSum  
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/152287838-d5e9c9b9-2509-410d-93c8-2d145ffb213d.png)

