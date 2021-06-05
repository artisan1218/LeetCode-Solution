public class swapPairs {

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
	ListNode result = solver.swapPairsRecursion(ary1);

	System.out.println();
	do {
	    System.out.print(result.val + "->");
	    result = result.next;
	} while (result != null);
    }

    private static class Solution {
	public ListNode swapPairsOnePass(ListNode head) {
	    if (head == null || head.next == null) {
		return head;
	    } else {
		ListNode result = new ListNode();
		ListNode cursor = result;

		ListNode left = head;
		ListNode right = head.next;
		while (left != null && right != null) {
		    cursor.next = new ListNode(right.val);
		    cursor = cursor.next;
		    cursor.next = new ListNode(left.val);
		    cursor = cursor.next;
		    if (right.next == null) {
			break;
		    } else {
			left = left.next.next;
			right = right.next.next;
		    }

		}
		// there is one extra element at the end yet to add
		if (right == null) {
		    cursor.next = new ListNode(left.val);
		    cursor = cursor.next;
		}
		return result.next;
	    }
	}

	public ListNode swapPairsRecursion(ListNode head) {
	    // base case
	    if (head == null || head.next == null) {
		return head;
	    } else {
		// recursive step
		// sub-problem is swapping two pairs
		ListNode newHead = head.next;
		head.next = swapPairsRecursion(newHead.next);
		newHead.next = head;
		return newHead;
	    }
	}
    }

}
