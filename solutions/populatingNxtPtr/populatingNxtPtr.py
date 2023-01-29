# %%
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connectBFS(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        else:
            stack = [root]
            nextLevel = []

            while len(stack)!=0:
                node = stack.pop(0)
                if node.left is not None:
                    nextLevel.append(node.left)
                if node.right is not None:
                    nextLevel.append(node.right)

                if len(stack)==0:
                    for i in range(len(nextLevel)-1):
                        nextLevel[i].next = nextLevel[i+1]
                    stack = nextLevel.copy()
                    nextLevel = []
            return root

    def connectBFS2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head = root # sentinel node
        while root and root.left:
            nextLevel = root.left # reference to the next level
            # populating next pointer at the same level
            while root is not None:
                root.left.next = root.right
                if root.next is not None: # default value for next pointer is None, so no need to change it if root.next is None
                    root.right.next = root.next.left
                root = root.next
            # move to the next level
            root = nextLevel
        return head

    def connectRecursion(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def recursion(root):
            if root is None:
                return None
            else:
                if root.left is not None:
                    root.left.next = root.right
                    if root.next is not None:
                        root.right.next = root.next.left
            recursion(root.left)
            recursion(root.right)

        recursion(root)
        return root


if __name__ == '__main__':
    solver = Solution()
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    solver.connectBFS(root)



