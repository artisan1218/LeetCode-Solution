import java.math.BigInteger;

public class AddTwoNums {

    public static class ListNode {
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

    public static void main(String[] args) {
	ListNode l11 = new ListNode(9);
	ListNode l12 = new ListNode(9);
	ListNode l13 = new ListNode(9);
	ListNode l14 = new ListNode(9);
	ListNode l15 = new ListNode(9);
	l11.next = l12;
	l12.next = l13;
	l13.next = l14;
	l14.next = l15;

	ListNode l21 = new ListNode(9);
	ListNode l22 = new ListNode(9);
	ListNode l23 = new ListNode(9);
	l21.next = l22;
	l22.next = l23;

	print(l11);
	print(l21);

	// print(addTwoNumbersConversion(l11, l21));
	print(addTwoNumbersMathQuick(l11, l21));
	// print(addTwoNumbersMathSlow(l11, l21));

    }

    public static ListNode addTwoNumbersConversion(ListNode l1, ListNode l2) {
	ListNode resultCursor = new ListNode();
	ListNode resultHead = resultCursor;

	StringBuilder num1str = new StringBuilder();
	StringBuilder num2str = new StringBuilder();
	while (l1 != null) {
	    num1str.append(new StringBuilder(String.valueOf(l1.val)));
	    l1 = l1.next;
	}
	while (l2 != null) {
	    num2str.append(new StringBuilder(String.valueOf(l2.val)));
	    l2 = l2.next;
	}

	BigInteger num1 = new BigInteger(num1str.reverse().toString());
	BigInteger num2 = new BigInteger(num2str.reverse().toString());
	BigInteger sum = num1.add(num2);

	while (sum != BigInteger.ZERO) {
	    BigInteger remainder = sum.remainder(BigInteger.TEN);
	    resultCursor.next = new ListNode(remainder.intValue());
	    resultCursor = resultCursor.next;
	    sum = sum.divide(BigInteger.TEN);
	}

	return resultHead.next;
    }

    public static ListNode addTwoNumbersMathQuick(ListNode l1, ListNode l2) {
	ListNode resultCursor = new ListNode();
	ListNode resultHead = resultCursor;
	int num1 = 0;
	int num2 = 0;
	int carry = 0;
	while (l1 != null || l2 != null || carry != 0) {
	    resultCursor.next = new ListNode();
	    resultCursor = resultCursor.next;
	    if (l1 != null) {
		num1 = l1.val;
		l1 = l1.next;
	    }
	    if (l2 != null) {
		num2 = l2.val;
		l2 = l2.next;
	    }
	    int sum = num1 + num2 + carry;
	    num1 = 0;
	    num2 = 0;
	    carry = sum / 10;
	    resultCursor.val = sum % 10;
	}
	return resultHead.next;
    }

    public static ListNode addTwoNumbersMathSlow(ListNode l1, ListNode l2) {
	ListNode resultCursor = new ListNode();
	ListNode resultHead = resultCursor;
	int carry = 0;
	int num1 = 0;
	int num2 = 0;
	while (l1.next != null && l2.next != null) {
	    num1 = l1.val;
	    num2 = l2.val;

	    int sum = num1 + num2 + carry;
	    carry = 0;
	    if (sum >= 10) {
		carry = sum / 10;
		sum = sum % 10;
	    }

	    resultCursor.val = sum;
	    resultCursor.next = new ListNode();
	    resultCursor = resultCursor.next;

	    l1 = l1.next;
	    l2 = l2.next;
	}

	num1 = l1.val;
	num2 = l2.val;
	int sum = num1 + num2 + carry;
	carry = 0;
	if (sum >= 10) {
	    carry = sum / 10;
	    sum = sum % 10;
	}
	resultCursor.val = sum;

	while (l1.next != null) { // l1 is longer
	    if (l1.next != null) {
		resultCursor.next = new ListNode();
		resultCursor = resultCursor.next;
	    }
	    l1 = l1.next;
	    sum = l1.val + carry;
	    carry = 0;
	    if (sum >= 10) {
		carry = sum / 10;
		sum = sum % 10;
	    }
	    resultCursor.val = sum;
	}
	while (l2.next != null) {
	    if (l2.next != null) {
		resultCursor.next = new ListNode();
		resultCursor = resultCursor.next;
	    }
	    l2 = l2.next;
	    sum = l2.val + carry;
	    carry = 0;
	    if (sum >= 10) {
		carry = sum / 10;
		sum = sum % 10;
	    }
	    resultCursor.val = sum;

	}

	if (carry != 0) {
	    resultCursor.next = new ListNode(carry);
	}
	return resultHead;
    }

    public static void print(ListNode head) {
	while (head != null) {
	    if (head.next == null) {
		System.out.print(head.val);
	    } else {
		System.out.print(head.val + "->");
	    }
	    head = head.next;
	}
	System.out.println();
    }
}
