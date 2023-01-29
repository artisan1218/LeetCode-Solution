# Min Stack problem

<img src="https://user-images.githubusercontent.com/25105806/212526665-c5467494-27dc-4d2c-b4ab-9833977abd77.png" width=80% length=80%>

Leetcode link: https://leetcode.com/problems/min-stack/description/

<br/>

### Approach 1: Doubly LinkedList, minStackDoublyLinkedList

The idea is to have a doubly linked list storing the current min value at each node. This way when popping the top node, we can remove the min value associated with that node at the same time, so min value can also be updated.

`topNode` always points to the newly pushed node.

```python3
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.min = float('inf')
        self.next = None
        self.prev = None
        
class minStack:
    def __init__(self):
        self.topNode = ListNode()
        self.begin = self.topNode
        
    def push(self, val):
        newVal = ListNode(val)
        if val < self.topNode.min:
            newVal.min = val
        else:
            newVal.min = self.topNode.min
        self.topNode.next = newVal
        newVal.prev = self.topNode
        self.topNode = self.topNode.next
        
    def pop(self):
        result = self.topNode
        self.topNode = self.topNode.prev
        self.topNode.next = None
        result.prev = None
        return result.val
        
    def top(self):
        return self.topNode.val
        
    def getMin(self):
        return self.topNode.min
        
```

Complexity is O(1) for all operations:
![image](https://user-images.githubusercontent.com/25105806/212527088-ef68e646-3778-4334-aa2e-e61a94dd840c.png)

<br/>

### Approach 2: Two Stacks, minStackTwoStack

Another approach is to have two stacks storing value and current min separately. For the sake of simplicity, python built-in stack is used as a regular stack, we will build minStack on top of two regular stacks. Everytime we push new value into minStack, we will update both stacks `stack` and `min`, `stack` is used to store the actual new value and `min` is used to store the current min value associated with new value `val`, and these two stacks are also popped together to stay synced. 

```python3
class minStackTwoStack:
    def __init__(self):
        self.stack = list()
        self.min = list()
        
    def push(self, val):
        self.stack.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        else:
            self.min.append(min(self.min[-1], val))
        
    def pop(self):
        self.min.pop()
        return self.stack.pop()
        
    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.min[-1]       
```

Time complexity is also O(1) for every function:
![image](https://user-images.githubusercontent.com/25105806/212527500-0973aa52-36ba-4a1c-9b19-389d06f04512.png)

