# Palindrome Number problem
* Given an integer `x`, return true if `x` is palindrome integer.
* An integer is a **palindrome** when it reads the same backward as forward. For example, `121` is palindrome while `123` is not.

Leetcode link: https://leetcode.com/problems/palindrome-number/

<br/>

### Approach 1: Math, isPalindrome()
Since all negative numbers are not palindrome numbers, we can simply rule out all negnative numbers. Then we get the least digit, append it backwards to a new number, compare the new number and the original number to see if they are equal.
![image](https://user-images.githubusercontent.com/25105806/118416321-ee3e2600-b663-11eb-8ee4-8791338ee869.png)


```java
public static boolean isPalindrome(int x) {
	int reverse = 0;
	int ori = x;
	if (x < 0) {
	    return false;
	} else {
	    while (x > 0) {
		reverse = reverse * 10 + x % 10;
		x = x / 10;
	    }
	}
	return reverse == ori;
    }
```


Time complexity is O(log10(n)) because max number of times we loop is equal to number of digits in the given number and number of digits in a given number is equal to Ceil(log10(n)) where n is the input number.\
Time complexity analysis credits to https://leetcode.com/problems/palindrome-number/solution/793827
