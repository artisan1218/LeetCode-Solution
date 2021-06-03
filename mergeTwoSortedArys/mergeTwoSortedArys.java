
public class mergeTwoSortedArys {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	Solution solver = new Solution();

	ListNode ary1 = new ListNode(1);
	ListNode two1 = new ListNode(2);
	ListNode three1 = new ListNode(3);
	ListNode four1 = new ListNode(4);
	ary1.next = two1;
	two1.next = three1;
	three1.next = four1;

	ListNode ary2 = new ListNode(1);
	ListNode two2 = new ListNode(1);
	ListNode three2 = new ListNode(6);
	ListNode four2 = new ListNode(7);
	ary2.next = two2;
	two2.next = three2;
	three2.next = four2;

	ListNode result = solver.mergeTwoLists2(ary1, ary2);

	do {
	    System.out.println(result.val);
	    result = result.next;
	} while (result != null);

    }

}

class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
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
	
	if(l1==null && l2!=null) {
	    cursor.next = l2;
	}else if(l1!=null && l2==null) {
	    cursor.next = l1;
	}

	return result.next;
    }

}