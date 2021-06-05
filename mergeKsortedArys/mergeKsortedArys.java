import java.util.PriorityQueue;

public class mergeKsortedArys {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	ListNode ary1 = new ListNode(1);
	ListNode two1 = new ListNode(4);
	ListNode three1 = new ListNode(5);
	ary1.next = two1;
	two1.next = three1;

	ListNode ary2 = new ListNode(1);
	ListNode two2 = new ListNode(3);
	ListNode three2 = new ListNode(4);
	ary2.next = two2;
	two2.next = three2;

	ListNode ary3 = new ListNode(2);
	ListNode two3 = new ListNode(6);
	ary3.next = two3;

	ListNode[] lists = new ListNode[] { ary1, ary2, ary3 };

	Solution solver = new Solution();
	ListNode result = solver.mergeKListsMergeSort(lists);

	do {
	    System.out.println(result.val);
	    result = result.next;
	} while (result != null);
    }

    private static class Solution {
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

    }
}
