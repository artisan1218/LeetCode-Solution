# Remove Duplicates from Sorted List problem
* Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

### Approach 1: Iteration 1, deleteDuplicates1()
Use two pointers `pred` and `head` to iterate through the list. `head` will be used to check the next element an `pred` will be used to compare the value and skip duplicates

Time complexity is O(n):\
<img width="807" alt="image" src="https://user-images.githubusercontent.com/25105806/133155830-d0a0556c-e2e0-4905-8ddf-d63545e44694.png">


### Approach 2: Iteration 2, deleteDuplicates2()
Since idea but much concise code. The key part is we skip one duplicate a time, skip all duplicates after the loop
```
while cur.next!=None and cur.val==cur.next.val:
    cur.next = cur.next.next # skip one duplicate a time, skip all duplicates after the loop
```

Time complexity is O(n):\
<img width="800" alt="image" src="https://user-images.githubusercontent.com/25105806/133156080-fd532bf8-2baf-4f5a-907c-74c880a8f1c1.png">


### Approach 3: Recursion, deleteDuplicates3()
Credits to: https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/28625/3-Line-JAVA-recursive-solution

This might not be the most efficient solution, but the idea is simple:\
<img width="1002" alt="image" src="https://user-images.githubusercontent.com/25105806/133156260-ece0e662-4143-423c-9953-62750de1cd16.png">


We will keep entering the recursion stack with next element, so the linked list in each recursion stack is one less element than previous one. Then simply return the `head` of the linked list if the `head.val` is not same as `head.next.val` and return `head.next` if they are the same. This way we can ensure that the returned linked list is always unique with no duplicates.

Actual running time:\
<img width="800" alt="image" src="https://user-images.githubusercontent.com/25105806/133156873-6311db41-071d-4ee9-96fc-d685dea70f60.png">

