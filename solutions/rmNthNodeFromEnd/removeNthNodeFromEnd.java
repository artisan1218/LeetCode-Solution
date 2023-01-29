import java.util.HashMap;
import java.util.Map;

public class removeNthNodeFromEnd {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	ListNode one = new ListNode(1);
	ListNode two = new ListNode(2);
	ListNode three = new ListNode(3);
	ListNode four = new ListNode(4);

	one.next = two;
	two.next = three;
	three.next = four;

	ListNode result = removeNthFromEndOnePass(one, 2);
	do {
	    System.out.println(result.val);
	    result = result.next;
	} while (result != null);

    }

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

}

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
	this.val = val;
    }

    ListNode(int val, ListNode next) {
	this.val = val;
	this.next = next;
    }
}
