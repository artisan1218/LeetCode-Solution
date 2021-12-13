# Merge k Sorted Lists problem
* You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.
* Merge all the linked-lists into one sorted linked-list and return it.

![image](https://user-images.githubusercontent.com/25105806/145904452-bf34f862-e786-4757-aa0f-f4c151df3b0b.png)

Leetcode link: https://leetcode.com/problems/merge-k-sorted-lists/

<br/>

### Approach 1: Compare one by one, mergeKListsNaive()
This approach is simply get each least elements from the given arrays, compare them and append the smaller element to a new ListNode and finally return it.

```java
public ListNode mergeKListsNaive(ListNode[] lists) {
    ListNode result = new ListNode();
    ListNode resultCursor = result;
    int numberOfNullArys = 0;

    while (numberOfNullArys != lists.length) {
  int leastNodeIdx = 0;
  int leastVal = Integer.MAX_VALUE;
  numberOfNullArys = 0;
  // find the least value and its pointer in current column
  for (int i = 0; i < lists.length; i++) {
      ListNode cursor = lists[i];
      if (cursor != null) {
    if (cursor.val < leastVal) {
        leastVal = cursor.val;
        leastNodeIdx = i;
    }
      } else {
    numberOfNullArys++;
      }
  }
  // if numberOfNullArys==lists.length, then all arys have been added
  if (numberOfNullArys != lists.length) {
      // move the pointer to next
      lists[leastNodeIdx] = lists[leastNodeIdx].next;
      // update result
      resultCursor.next = new ListNode(leastVal);
      resultCursor = resultCursor.next;
  }
    }

    return result.next;
}
```

Time complexity is O(kn) where k is the numebr of linked-list and n is the number of element in the linked-list because we will compare the least elements between all linked-list and we will do the comparsion n times. \
![image](https://user-images.githubusercontent.com/25105806/120882363-18f90b80-c58c-11eb-943a-c9ab8b955342.png)

<br/>

### Approach 2: Insertion, mergeKListsInsertion()
This approach is based on insertion sort. The idea is to read the `ListNode` one by one, insert each element of the current `ListNode` to the right place of the new ListNode.

```java
public ListNode mergeKListsInsertion(ListNode[] lists) {
    ListNode result = new ListNode();

    for (ListNode ary : lists) {
  ListNode insertionCursor = result;
  while (ary != null) {
      int val = ary.val;
      // found the right place for insertion
      while (insertionCursor.next != null && val > insertionCursor.next.val) {
    insertionCursor = insertionCursor.next;
      }
      // insert val into result
      ListNode tmp = insertionCursor.next;
      insertionCursor.next = new ListNode(val);
      insertionCursor.next.next = tmp;
      ary = ary.next;
  }
    }

    return result.next;
}
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/120882500-2f539700-c58d-11eb-82f9-d1a533a32f3a.png)

<br/>

### Approach 3: PriorityQueue, mergeKListsPriorityQueue()
This approach fully utilizes the PriorityQueue. First do a traversal over all elements in all linked-list, add all of them to the priority queue one by one. Since priority queue will always return the least element first when polling, we can then poll all of them out of the priority queue and add them to a new linked list and return it. The priority queue will do the 'sorting' for us.

```java
public ListNode mergeKListsPriorityQueue(ListNode[] lists) {
    // add all values to a priorityQueue
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    for (ListNode ary : lists) {
  while (ary != null) {
      pq.add(ary.val);
      ary = ary.next;
  }
    }
    // priorityQueue will ensure that we always pull the smallest value out first
    ListNode result = new ListNode();
    ListNode cursor = result;
    while (pq.size() != 0) {
  cursor.next = new ListNode(pq.poll());
  cursor = cursor.next;
    }
    return result.next;
}
```

Time complexity is O(nlogk), k is the number of linked-list and n is the numebr of elements in linked-list. Insertion of all n elements with O(logk) time will result in O(nlogk) and the retrieval time is simply O(1)\
![image](https://user-images.githubusercontent.com/25105806/120882639-f2d46b00-c58d-11eb-93a8-cfafb01317da.png)

<br/>

### Approach 4: MergeSort, Divide and Conquer, mergeKListsMergeSort()
This approach takes idea from mergesort. The idea is to divide the given `lists` into several pairs(2 ListNodes) of ListNode and merge these 2 ListNode using method in [mergeTwoSortedArys](https://github.com/artisan1218/LeetCode-Solution/tree/main/mergeTwoSortedArys) into one sorted array, then merge other ListNode recursively. This approach is very similar to merge sort.

Image below shows how this works, note that black block denotes **unsorted lists** while red block denotes **sorted ListNode**
<img src="https://user-images.githubusercontent.com/25105806/120882961-80648a80-c58f-11eb-9217-7fddd7a8c45c.png" height="50%" width="50%">

```java
public ListNode mergeKListsMergeSort(ListNode[] lists) {
    if (lists == null || lists.length == 0) {
  return null;
    }
    return sort(lists, 0, lists.length - 1);
}

private ListNode sort(ListNode[] lists, int lo, int hi) {
    if (lo >= hi) {
  return lists[lo];
    } else {
  int mid = lo + (hi - lo) / 2;
  // divide and conquer, divide each portion of the lists into single ListNode
  // and merge two ListNode
  ListNode l1 = sort(lists, lo, mid);
  ListNode l2 = sort(lists, mid + 1, hi);
  // mergeTwoLists will simply return the merged two sorted list
  return mergeTwoLists(l1, l2);
    }
}

public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
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

Time complexity is also O(nlogk), actual running time:\
![image](https://user-images.githubusercontent.com/25105806/120883037-d1747e80-c58f-11eb-9563-38ef3b6b9c61.png)


