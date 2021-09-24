# Reverse Linked List problem
![image](https://user-images.githubusercontent.com/25105806/134618110-5dc5ca46-5639-4737-88f3-8c87c5d90371.png)


<br />

### Approach 1: Naive, reverseListNaive()
Simply iterate through the entire linked list and store all references of node in a list and create a new linked list then add all stored node in reverse order

Time complexity and space complexity are both O(n):
![image](https://user-images.githubusercontent.com/25105806/134618259-523f9959-2d02-40df-9ce0-d4a37f15ba53.png)


### Approach 2: Iteration, reverseListIteration()
We can use two extra pointers to do this interatively in O(n) time. The key is to always have a pointer points to the remaining linked list and point current `head` to `prevHead`

![68f45cb3d4ad770c3e1c88208be1c44](https://user-images.githubusercontent.com/25105806/134618460-33b124f1-d0a0-41b1-b6c0-c811f573eebd.jpg)

Time complexity is O(n) and since we do not store any extra nodes, space complexity is O(1):
![image](https://user-images.githubusercontent.com/25105806/134618534-96ef6760-cb19-42e5-ab06-4b2271b1a71d.png)


### Approach 3: Recursion, reverseListRecursion()
The idea is similiar to approach 2 but use recursion to do the job. We will keep entering recursive stack until `head` is None, and change the direction of `head` in each recursion to reverse

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/134618613-e8445d44-d804-4335-9ed9-f36a2b456786.png)





