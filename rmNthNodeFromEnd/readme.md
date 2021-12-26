# Remove Nth Node From End of List problem
* Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

![image](https://user-images.githubusercontent.com/25105806/120162598-67ce2c00-c1ad-11eb-869e-7d377d5d1797.png)  

Leetcode link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

<br />

### Approach 1: Two Pass, removeNthFromEndTwoPass()
First pass is to count the length of the entire linkedList `head`, second pass is to find the nth-1 node from the end so that we can delete the nth node.

```java
public static ListNode removeNthFromEndTwoPass(ListNode head, int n) {
	ListNode dummy = new ListNode();
	dummy.next = head;
	ListNode secPassCursor = dummy;

	// count the length excluding the dummy
	int len = 0;
	while (head != null) {
	    head = head.next;
	    len++;
	}

	// move cursor to the left node of the node that should be removed
	int counter = 0;
	while (counter < len - n) {
	    secPassCursor = secPassCursor.next;
	    counter++;
	}

	// remove the Nth node from the end by skipping it
	secPassCursor.next = secPassCursor.next.next;

	return dummy.next;
    }

```

Time complexity is O(n) although we uses a two pass algorithm. Space complexity is O(1).\
![image](https://user-images.githubusercontent.com/25105806/120163163-11adb880-c1ae-11eb-8876-db4c6d4e3dd7.png)


<br />
 
### Approach 2: Cache, removeNthFromEndCache()
The idea is similar to approach 1, we still need to go through the entire linkedList first to get the length and also, more importantly, cache each node reference by putting them in a hashmap so that we can retrieve the desired node based on its index using contant lookup time offered by hashmap. This saves one pass but uses more memory since we stored each node reference.\

```java
public static ListNode removeNthFromEndCache(ListNode head, int n) {
	ListNode dummy = new ListNode();
	dummy.next = head;
	ListNode result = dummy;

	// cache each node and its index by putting them into a hash map
	Map<Integer, ListNode> mapper = new HashMap<>();
	int idx = 0;
	while (dummy != null) {
	    mapper.put(idx, dummy);
	    dummy = dummy.next;
	    idx++;
	}

	// get the left node of the gap, skip the next node which is the removed node
	// idx is the length of the ListNode
	ListNode left = mapper.get(idx - n - 1);
	left.next = left.next.next;

	return result.next;
    }

```

Time complexity is O(n) and space complexity is O(n). We can see that this approach uses more memory.
![image](https://user-images.githubusercontent.com/25105806/120164001-f2635b00-c1ae-11eb-8e9a-7e6234ccb959.png)


<br />

### Approach 3: One Pass by maintaining the gap, removeNthFromEndOnePass()
The idea is to use two pointers `left` and `right` and keep the gap between these two pointers always to be `n` so that we can simply rewire the `left.next` to `left.next.next`. The first loop(for-loop) is to create the gap, the second loop(while-loop) is to maintain the gap by moving `right` to end.

<img src="https://user-images.githubusercontent.com/25105806/120165022-ff347e80-c1af-11eb-86ae-9ba6a2765f28.png" width="60%" height="60%">
<br />

```java
public static ListNode removeNthFromEndOnePass(ListNode head, int n) {
	ListNode dummy = new ListNode(0);
	dummy.next = head;

	ListNode left = dummy, right = dummy;

	// Move right to a pos where the distance/gap of left and right is equal to n
	for (int i = 0; i < n + 1; i++) {
	    right = right.next;
	}

	// Move right to the end, while moving left together, maintaining the gap
	while (right != null) {
	    left = left.next;
	    right = right.next;
	}
	// Skip the desired node
	left.next = left.next.next;
	return dummy.next;
    }
```

Time complexity is O(n), space complexity is O(1)\
![image](https://user-images.githubusercontent.com/25105806/120165481-7a963000-c1b0-11eb-81c7-1feb28f0794e.png)




