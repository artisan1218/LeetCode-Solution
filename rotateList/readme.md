# Rotate List problem
* Given the head of a linked list, rotate the list to the right by `k` places.
  ![image](https://user-images.githubusercontent.com/25105806/128293111-5722a2c3-a1a9-4d67-8fed-57503e8cf190.png)

<br />

### Approach 1: Create Circle and Move, rotateRight()
The idea of this solution is to first connect the tail to `head` so that we form a circle. Then we will move the `head` to correct index by subtract `k` from the length of the linked list, finally cut the circle at index before `head`.
Note that `k` is updated by `k%length of linked list` because if k is longer than the length of the linked list, we can simply get the mod because rotating 7 times of a length 6 linked list is no difference than rotating once

Time complexity is O(n):

![8ffc16572bcd6bc6f02ee411ae874c7](https://user-images.githubusercontent.com/25105806/128293291-95fec2ce-fcef-425e-9cf4-b42762a552ee.png)


