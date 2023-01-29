#  Unique Binary Search Trees II problem
![image](https://user-images.githubusercontent.com/25105806/135388326-25fba09e-8e4f-46d6-9763-3e4c8a395de6.png)

Leetcode link: https://leetcode.com/problems/unique-binary-search-trees-ii/

<br />

### Approach 1: Recursion, generateTrees()
Credits to: https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/929000/Recursive-solution-long-explanation

The idea is to iterate through each node in the range `[1, n]` because each of them can be the root of a BST. Then divide the range into two parts, one is `[1:n]` and another one is `[n+1:n]`, representing the left branches and right branches respectively. After we have all possible left branches and right branches for a root value, then we can start constructing all possible BST by connecting left branch and right branch to current root value. We do this recursively to get all BSTs.

```python3
def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    nList = list(range(1, n+1))
    return self.helper(nList)

def helper(self, nList):
    # if all values are used, return an empty branch of [None], not a None value!
    if len(nList)==0:
        return [None]
    else:
        # result that holds all branches under current root
        result = []
        for i in range(len(nList)):
            leftBranches = self.helper(nList[:i]) # get all left branches
            rightBranches = self.helper(nList[i+1:]) # get all right branches

            # go through each combination of left and right branch
            for leftBranch in leftBranches:
                for rightBranch in rightBranches:
                    # construct a binary tree with current value as root 
                    root = TreeNode(nList[i])
                    root.left = leftBranch
                    root.right = rightBranch

                    result.append(root)
        return result
```

Actual running time:

![image](https://user-images.githubusercontent.com/25105806/135388854-342988b4-c172-4f85-b701-e2c4574bd7aa.png)



