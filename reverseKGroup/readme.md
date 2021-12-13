# Reverse Nodes in k-Group problem
* Given a linked list, reverse the nodes of a linked list `k` at a time and return its modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

![image](https://user-images.githubusercontent.com/25105806/145905179-fbb05704-d3b6-42bc-bd13-a4576d89874b.png)

Leetcode link: https://leetcode.com/problems/reverse-nodes-in-k-group/

<br/>

### Approach 1: Cache k values, reverseKGroupCachePointers()
This approach is fairly easy to come up with, simply read `k` nodes a time and cache them in a list, then add the nodes in this list in reverse order to a new ListNode.
Downside of this approach is pretty straightforward: it uses O(k) space because we will store all k pointers/values in a list.

```java
public ListNode reverseKGroupCachePointers(ListNode head, int k) {
	    ListNode result = new ListNode();
	    ListNode cursor = result;

	    int[] pointers = new int[k];
	    int i = 0;
	    while (head != null || i != 0) {
		if (i == k) {
		    // add the pointers in reverse order
		    for (i = pointers.length - 1; i >= 0; i--) {
			cursor.next = new ListNode(pointers[i]);
			cursor = cursor.next;
		    }
		    i = 0;
		} else if (head == null && i < k) {
		    // we've reached the end, add remaining pointers in order
		    for (int j = 0; j < i; j++) {
			cursor.next = new ListNode(pointers[j]);
			cursor = cursor.next;
		    }
		    i = 0;
		} else {
		    // read next value in current group
		    pointers[i] = head.val;
		    head = head.next;
		    i++;
		}
	    }

	    return result.next;
	}
```
Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/120912350-202f2080-c643-11eb-862d-b072b6c36b6c.png)

<br />

### Approach 2: Add Node in Reverse Order Directly, reverseKGroupConstantSpace()
Credits to: https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11491/Succinct-iterative-Python-O(n)-time-O(1)-space

This approach is a little more complicated in that we introduce several more pointers to reverse the ListNode using O(1) memory complexity. The idea is to first identify each group of k nodes, reverse the nodes inside current group, then connect previous group to this reversed group, repeat this process untill we reach the end.
```
k = 3 for example:

step 0: (previous k-group) -> a -> b -> c -> (next k-group)

step 1: (previous k-group) ->      b -> c -> (next k-group)
                                          a ---^

step 2: (previous k-group) ->           c -> (next k-group)
                                     b -> a ---^

step 3: (previous k-group) ->                (next k-group)
                                c -> b -> a ---^

finish: (previous k-group) -> c -> b -> a -> (next k-group)
```
This algorithm may seem complex and hard to understand at the first glance but it reduces memory complexity to O(1), which means the number of extra pointers used to achieve the 'reversal' **does not grow with `k`**, we will always uses same amount of pointers to reverse.

```java
public ListNode reverseKGroupConstantSpace(ListNode head, int k) {
	    ListNode result = new ListNode();
	    ListNode jump = result;

	    result.next = head;
	    ListNode left = head;
	    ListNode right = head;

	    while (true) {
		int count = 0;
		while (right != null && count < k) {
		    count++;
		    right = right.next;
		}
		if (count == k) {
		    ListNode tmp, cur, prev;
		    cur = left;
		    prev = right;
		    for (int i = 0; i < k; i++) {
			tmp = cur.next;
			cur.next = prev;
			prev = cur;
			cur = tmp;
		    }
		    jump.next = prev;
		    jump = left;
		    left = right;
		} else {
		    return result.next;
		}
	    }
	}
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/120912515-ad26a980-c644-11eb-9bf5-652969d3af3d.png)
