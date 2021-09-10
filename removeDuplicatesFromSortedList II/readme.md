# Remove Duplicates from Sorted List II problem
* Given the `head` of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.


### Approach 1: Two Pointers, deleteDuplicates()
Use two pointers, one fast, one slow. Slow pointer will be used to modify the linked list while fast pointer will be used to get new value and check for duplicates.

Time complexity is O(n):\
![9400470eb4f90d209f7648cc75c51eb](https://user-images.githubusercontent.com/25105806/132803589-5d3e76a1-1b84-4da3-ba9c-ad96259d6a89.png)
