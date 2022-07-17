# Add Two Numebrs problem
* You are given two non-empty linked lists representing two non-negative integers. 
* The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
* You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Leetcode link: https://leetcode.com/problems/add-two-numbers/

<br />

All three approaches have time complexity of O(m+n)
### Approach 1: addTwoNumbersMathSlow()
Iterate through both linked list at the same time, add the corresponding digits at same position, keep the carryover digit and compute the next digit. This pretty straight-forward. But several egde cases to consider: 
* two numbers are not the same length
* carryover digit is the last digit, which means one more digit it needed to generate the answer

```java
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
```
![image](https://user-images.githubusercontent.com/25105806/179429985-88125922-9095-441f-b3d6-f1bcabf35936.png)


<br />

### Approach 2: addTwoNumbersMathQuick()
Similar to approach 1 but improve the logic, remove uncessary blocks and make it faster. 

```java
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
```

![image](https://user-images.githubusercontent.com/25105806/118186463-9ea4f380-b3f2-11eb-9dff-25e5bbcd933f.png)

<br />

### Approach 3: addTwoNumbersConversion()
Can also read the two linked list first, convert them to java BigInteger, do the math and convert the BigInteger back to linked list. This approach requires the use of BigInteger because the number might be too large for regular int in java. Thus the running time is slower than approach 2.

```java
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
```

![image](https://user-images.githubusercontent.com/25105806/118186596-c4ca9380-b3f2-11eb-9290-0937f89b8116.png)
