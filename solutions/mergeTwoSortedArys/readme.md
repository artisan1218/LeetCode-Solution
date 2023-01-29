# Merge Two Sorted Lists problem
* Merge two sorted linked lists and return it as a **sorted** list. The list should be made by splicing together the nodes of the first two lists.
<img src="https://user-images.githubusercontent.com/25105806/120598322-fc799980-c3fa-11eb-8eeb-d543dfb00a41.png" width="60%" height="60%">

Leetcode link: https://leetcode.com/problems/merge-two-sorted-lists/

<br/>

### Approach 1: Switching, mergeTwoLists1()
This approach is simply get two least elements from the given two arrays `l1` and `l2`, compare them and append the smaller element to a new ListNode and finally return it.\

```java
public ListNode mergeTwoLists1(ListNode l1, ListNode l2) {
	ListNode result = new ListNode();
	ListNode cursor = result;

	while (l1 != null || l2 != null) {
	    if (l1 != null && l2 != null) {
		if (l1.val < l2.val) {
		    cursor.next = new ListNode(l1.val);
		    l1 = l1.next;
		} else {
		    cursor.next = new ListNode(l2.val);
		    l2 = l2.next;
		}
		cursor = cursor.next;
	    } else if (l1 != null && l2 == null) {
		cursor.next = new ListNode(l1.val);
		cursor = cursor.next;
		l1 = l1.next;
	    } else if (l1 == null && l2 != null) {
		cursor.next = new ListNode(l2.val);
		cursor = cursor.next;
		l2 = l2.next;
	    }
	}

	return result.next;
    }
```

Time complexity is simply O(m+n) where `m` is the length of `l1` and `n` is the length of `l2`.
![image](https://user-images.githubusercontent.com/25105806/120598711-7447c400-c3fb-11eb-8689-6c7968cab35f.png)

<br/>

### Approach 2: Switching, break when either one reaches end, mergeTwoLists2()
This approach is based on approach 1, the only difference is that, when either one array reaches the end, we can simply append the rest of the other array to the result ListNode because there is only one element left for comparsion and there is no need for comparsion. This way we can skip the unnecessary comparsion.

```java
public ListNode mergeTwoLists2(ListNode l1, ListNode l2) {
	ListNode result = new ListNode();
	ListNode cursor = result;

	while (l1 != null && l2 != null) {
	    if (l1.val < l2.val) {
		cursor.next = new ListNode(l1.val);
		l1 = l1.next;
	    } else {
		cursor.next = new ListNode(l2.val);
		l2 = l2.next;
	    }
	    cursor = cursor.next;
	}

	if (l1 == null && l2 != null) {
	    cursor.next = l2;
	} else if (l1 != null && l2 == null) {
	    cursor.next = l1;
	}

	return result.next;
    }
```

Time complexity is therefore O(min(m, n)) because we only read the shorter array to the end. We can see from the running time that it is indeed faster.\
![image](https://user-images.githubusercontent.com/25105806/120599038-dbfe0f00-c3fb-11eb-975b-dc3a8e98a82c.png)
