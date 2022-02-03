# %%
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
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
            

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    solver = Solution()
    print(solver.maxPathSumRecursion(root))
        

# %%



