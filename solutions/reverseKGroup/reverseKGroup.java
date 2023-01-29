public class reverseKGroup {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	ListNode ary1 = new ListNode(1);
	ListNode two1 = new ListNode(2);
	ListNode three1 = new ListNode(3);
	ListNode four1 = new ListNode(4);
	ListNode five1 = new ListNode(5);
	ary1.next = two1;
	two1.next = three1;
	three1.next = four1;
	four1.next = five1;

	Solution solver = new Solution();
	ListNode result = solver.reverseKGroupConstantSpace(ary1, 3);

	System.out.println();
	do {
	    System.out.print(result.val + "->");
	    result = result.next;
	} while (result != null);
    }

    private static class Solution {
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
    }

}
