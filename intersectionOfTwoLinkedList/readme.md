# Intersection of Two Linked Lists problem
![image](https://user-images.githubusercontent.com/25105806/157149100-303b6b81-d90e-4a69-8ad9-52a81fd080a5.png)

![image](https://user-images.githubusercontent.com/25105806/157149144-06632216-8e59-422d-b05f-ecb0c86c9dab.png)

![image](https://user-images.githubusercontent.com/25105806/157149169-3ba48816-97a8-447a-ae30-cb5888d2288c.png)


Leetcode link: https://leetcode.com/problems/intersection-of-two-linked-lists/

<br/>

### Approach 1: Hash, getIntersectionNodeHash()
The idea is to first traverse a linked list, either one is ok, add all its nodes to a hash set `seen`, then traverse another linked list, compare the current node with seen nodes to see if the current node is an intersection. We will return the first intersection node.

```python3
def getIntersectionNodeHash(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
	seen = set()
	while headA is not None:
		seen.add(headA)
		headA = headA.next

	while headB is not None:
		if headB in seen:
			return headB
		else:
			headB = headB.next
	return None
```

Time complexity is O(m+n) where `m` and `n` are the length of linked list A and B and space complexity is O(n) or O(m):\
![image](https://user-images.githubusercontent.com/25105806/157149588-b26d964f-92e4-417f-8559-665eccb7e935.png)

<br/>

### Approach 2: Count, getIntersectionNodeCount()
This solution will first get the length of linked list A and B. We'll then find the longer linked list, first traverse the difference length between A and B so that the two pointers for two linked list are aligned. Then simply compare the nodes and return the first same node.

The key observation is that two intersected linked list share the back portion of the linked list, but not the front portion. What we can do is to align the pointer of the front portion by adjusting the 'offset' calculated by the difference in length to make sure that two pointers meet at the first intersection node.

```python3
def getIntersectionNodeCount(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
	# calculate length of headA
	lenA = 0
	counterA = headA
	while counterA is not None:
		counterA = counterA.next
		lenA += 1

	# calculate length of headB
	lenB = 0
	counterB = headB
	while counterB is not None:
		counterB = counterB.next
		lenB += 1

	# swap A and B if B is longer than A, make sure A is always the longer one
	if lenB > lenA:
		headA, headB = headB, headA
		lenA, lenB = lenB, lenA

	# move the longer pointer to the same position as the shorter one
	lenDiff = lenA - lenB
	while lenDiff > 0:
		headA = headA.next
		lenDiff -= 1

	# start comparing, if they share an intersection, the pointers must be equal
	while headA != headB:
		headA = headA.next
		headB = headB.next

	return headA # headB is also ok because they are same
```

Time complexity is O(m+n) and space complexity is O(1):\
![image](https://user-images.githubusercontent.com/25105806/157150256-a71445c8-64a2-4f90-8003-300ebd526a19.png)

<br/>

### Approach 3: Count, getIntersectionNodeCount2()
Instead of calculating the length difference and adjust the position of pointer of the longer linked list, we can directly traverse both pointer til the end of linked list A and B, then for pointer A, move the pointer to the begining of linked list B and for pointer B, move pointer B to the begining of linked list A. This way, we make sure that ptrA and ptrB, after reaching the end of A and B, are aligned, which means they will reach the intersection node at the same time.

This is the same idea as approach 2, but with a different implementation

```python3
def getIntersectionNodeCount2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
	ptrA, ptrB = headA, headB
	while ptrA != ptrB:
		# traverse A til the end, then points A to headB, do the same for B
		# this will make sure that ptrA and ptrB, after reaching the end of A and B,
		# are aligned, which means they will reach the intersection node at the same time
		if ptrA is None:
			ptrA = headB
		else:
			ptrA = ptrA.next

		if ptrB is None:
			ptrB = headA
		else:
			ptrB = ptrB.next
	return ptrA
```

Time complexity is O(m+n) and space complexity is O(1):\
![image](https://user-images.githubusercontent.com/25105806/157150581-e7b6ca94-7a5e-4726-8d57-96a3f33e6f3f.png)
