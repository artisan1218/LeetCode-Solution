# Remove Nth Node From End of List problem
* Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

![image](https://user-images.githubusercontent.com/25105806/120162598-67ce2c00-c1ad-11eb-869e-7d377d5d1797.png)  

<br />

### Approach 1: Two Pass, removeNthFromEndTwoPass()
First pass is to count the length of the entire linkedList `head`, second pass is to find the nth-1 node from the end so that we can delete the nth node. Time complexity is O(n) although we uses a two pass algorithm. Space complexity is O(1).
![image](https://user-images.githubusercontent.com/25105806/120163163-11adb880-c1ae-11eb-8876-db4c6d4e3dd7.png)

### Approach 2: Cache, removeNthFromEndCache()
The idea is similar to approach 1, we still need to go through the entire linkedList first to get the length and also, more importantly, cache each node reference by putting them in a hashmap so that we can retrieve the desired node based on its index using contant lookup time offered by hashmap. This saves one pass but uses more memory since we stored each node reference.\
Time complexity is O(n) and space complexity is O(n). We can see that this approach uses more memory.
![image](https://user-images.githubusercontent.com/25105806/120164001-f2635b00-c1ae-11eb-8e9a-7e6234ccb959.png)

### Approach 3: One Pass by maintaining gap, removeNthFromEndOnePass()
The idea is to use two pointers `left` and `right` and keep the gap between these two pointers always to be `n` so that we can simply rewire the `left.next` to `left.next.next`. The first loop(for-loop) is to create the gap, the second loop(while-loop) is to maintain the gap by moving `right` to end.

<img src="https://user-images.githubusercontent.com/25105806/120165022-ff347e80-c1af-11eb-86ae-9ba6a2765f28.png" width="60%" height="60%">
<br />

Time complexity is O(n), space complexity is O(1)\
![image](https://user-images.githubusercontent.com/25105806/120165481-7a963000-c1b0-11eb-81c7-1feb28f0794e.png)




