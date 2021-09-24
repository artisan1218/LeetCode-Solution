# Reverse Linked List II problem
![image](https://user-images.githubusercontent.com/25105806/134728460-0e643792-5c29-4ce3-a22f-e996eb55eb18.png)


<br />

### Approach 1: Iteration, reverseBetween()
The solution is based on the [reverseLinkedList](https://github.com/artisan1218/LeetCode-Solution/tree/main/reverseLinkedList), the only difference is that we have to first identify the node at index `left-1` and `right` in order to reverse the nodes in between. The reversing process is same as [reverseLinkedList](https://github.com/artisan1218/LeetCode-Solution/tree/main/reverseLinkedList), where we use three pointers to hold the remaining linked list, reverse current node and refer the new head. 

Time complexity is O(n) and space complexity is O(1):
![image](https://user-images.githubusercontent.com/25105806/134728948-44a0f7b2-9c83-4cd0-b090-2447331aec4d.png)

