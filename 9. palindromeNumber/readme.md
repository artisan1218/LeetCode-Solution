# Palindrome Number problem
* Given an integer `x`, return true if `x` is palindrome integer.
* An integer is a **palindrome** when it reads the same backward as forward. For example, `121` is palindrome while `123` is not.

### Approach 1: Math, isPalindrome()
Since all negative numbers are not palindrome numbers, we can simply rule out all negnative numbers. Then we get the least digit, append it backwards to a new number, compare the new number and the original number to see if they are equal.
![image](https://user-images.githubusercontent.com/25105806/118416321-ee3e2600-b663-11eb-8ee4-8791338ee869.png)


