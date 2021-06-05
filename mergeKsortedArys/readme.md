# Merge k Sorted Lists problem
* You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.
* Merge all the linked-lists into one sorted linked-list and return it.


### Approach 1: Compare one by one, mergeKListsNaive()
This approach is simply get each least elements from the given arrays, compare them and append the smaller element to a new ListNode and finally return it.\
Time complexity is O(kn) where k is the numebr of linked-list and n is the number of element in the linked-list because we will compare the least elements between all linked-list and we will do the comparsion n times. 
![image](https://user-images.githubusercontent.com/25105806/120882363-18f90b80-c58c-11eb-943a-c9ab8b955342.png)


### Approach 2: Insertion, mergeKListsInsertion()
This approach is based on insertion sort. The idea is to read the `ListNode` one by one, insert each element of the current `ListNode` to the right place of the new ListNode.\
Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/120882500-2f539700-c58d-11eb-82f9-d1a533a32f3a.png)

### Approach 3: PriorityQueue, mergeKListsPriorityQueue()
This approach fully utilizes the PriorityQueue. First do a traversal over all elements in all linked-list, add all of them to the priority queue one by one. Since priority queue will always return the least element first when polling, we can then poll all of them out of the priority queue and add them to a new linked list and return it. The priority queue will do the 'sorting' for us.\
Time complexity is O(nlogk), k is the number of linked-list and n is the numebr of elements in linked-list. Insertion of all n elements with O(logk) time will result in O(nlogk) and the retrieval time is simply O(1)\
![image](https://user-images.githubusercontent.com/25105806/120882639-f2d46b00-c58d-11eb-93a8-cfafb01317da.png)

### Approach 4: MergeSort, Divide and Conquer, mergeKListsMergeSort()
This approach takes idea from mergesort. The idea is to divide the given `lists` into several pairs(2 ListNodes) of ListNode and merge these 2 ListNode using method in [mergeTwoSortedArys](https://github.com/artisan1218/LeetCode-Solution/tree/main/mergeTwoSortedArys) into one sorted array, then merge other ListNode recursively. This approach is very similar to merge sort.\
Image below shows how this works, note that black block denotes **unsorted lists** while red block denotes **sorted ListNode**
<img src="https://user-images.githubusercontent.com/25105806/120882961-80648a80-c58f-11eb-9217-7fddd7a8c45c.png" height="50%" width="50%">

Time complexity is also O(nlogk), actual running time:\
![image](https://user-images.githubusercontent.com/25105806/120883037-d1747e80-c58f-11eb-9563-38ef3b6b9c61.png)


