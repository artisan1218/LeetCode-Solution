# Swap Nodes in Pairs problem
* Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

  ![image](https://user-images.githubusercontent.com/25105806/120906832-9155e000-c611-11eb-8ef6-e16dc8516897.png)


### Approach 1: One Pass Iteration, swapPairsOnePass()
We need to swap the node in each pair, which means swapping per two nodes. The idea is to use two pointers `left` and `right` to get each pair of nodes and add them to a new ListNode in order of right and left(because we swapped left and right). `left` and `right` will move forward twice a time to get to the next pair of two nodes.\
Time complexity is O(n).\
![image](https://user-images.githubusercontent.com/25105806/120906892-04f7ed00-c612-11eb-873a-82349f83bfd5.png)


### Approach 2: Recursion, swapPairsRecursion()
Turns out we can use recursion to solve this. The sub-problem is *swapping two nodes in a pair*, and we swap all pairs recursively. The idea is to first idenfity the new head, then find out the new node that current head should points to and finally make new head points to (old)head.\
Actual running time:

![image](https://user-images.githubusercontent.com/25105806/120906955-76d03680-c612-11eb-8b48-549780c85121.png)

