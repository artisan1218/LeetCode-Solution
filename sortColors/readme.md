# Sort Colors problem
* Given an array nums with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
* We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.
* You must solve this problem without using the library's sort function.

Leetcode link: https://leetcode.com/problems/sort-colors/

<br />

### Approach 1: Naive, sortColorsNaive()
The naive solution is to iterate through the list, move all 0's to the front and move all 2's to the end. There are many ways to implement this and some are quicker due to the implementation of `move` operation. 

```python3
def sortColorsNaive(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    moveCounter = 0
    i = 0
    while i<len(nums): # O(n)
        if nums[i] == 0:
            if i!=0:
                moveCounter+=1
                nums.insert(0, 0) # O(n)
                nums.pop(i+1) # O(n) for arbitrary element and O(1) for last element
            # first element is 0, no need to exchange position, simply check the next one
            i+=1
        elif nums[i] == 2:
            moveCounter+=1
            nums.append(2) # O(1)
            nums.pop(i) # O(n)
        else:
            # 1's position does not need to be changed
            i+=1
        if moveCounter == len(nums):
            break
```

In this solution, even though I only iterate through the list once, the time complexity is still O(n^2) since the `nums.insert()` will take O(n) time. \
![image](https://user-images.githubusercontent.com/25105806/131936278-0243a949-ffc2-40f8-894b-29f371d4e5fc.png)

<br />

### Approach 2: One Pointer Two Pass, sortColorsOnePtrTwoPass()
The idea is to move all 0's to the front by swaping, which is O(1), in a first pass and move all 1's to the end of last 0 in the second pass. Since we will only go through the list twice and each swaping operation is O(1). 

```python3
def sortColorsOnePtrTwoPass(self, nums: List[int]) -> None:
    # move all 0's to the head
    head = 0
    for i in range(len(nums)):
        if nums[i]==0:
            nums[i], nums[head] = nums[head], nums[i]
            head+=1

    # head is now the index of first non-0 number
    # move all 1's to the place after 0
    for i in range(head, len(nums)):
        if nums[i]==1:
            nums[i], nums[head] = nums[head], nums[i]
            head+=1
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/131936510-2e373a1c-72fe-42a9-a197-550c82a9e891.png)

<br />

### Approach 3: Two Pointers One Pass, sortColorsTwoPtrsOnePass()
We can use two pointers, one for moving 0's to the front and the other one for moving 2's to the end in one pass. Notice that when moving 2 to the end, we do not change the current cursor index `i` because we need to see if the exchanged value is still 2.

```python3
def sortColorsTwoPtrsOnePass(self, nums: List[int]) -> None:
    head = 0
    tail = len(nums)-1
    for i in range(len(nums)):
        # i is not changed because we need to see if the exchanged value is still 2
        while i<=tail and nums[i]==2:
            nums[i], nums[tail] = nums[tail], nums[i]
            tail-=1
        if nums[i] == 0:
            nums[i], nums[head] = nums[head], nums[i]
            head+=1
```

Time complexity is still O(n):\
![image](https://user-images.githubusercontent.com/25105806/131936683-83fb60c5-0c6f-4e81-b478-a1cf5748f869.png)

<br />

### Approach 4: Two Pointers One Pass 2, sortColorsTwoPtrsOnePass2()
Same idea, different implementation than approach 3.

```python3
def sortColorsTwoPtrsOnePass2(self, nums: List[int]) -> None:
    head = 0
    tail = len(nums)-1
    i = 0
    while i<=tail:
        if nums[i] == 0:
            nums[i], nums[head] = nums[head], nums[i]
            head+=1
            i = max(head, i)
        elif nums[i] == 2:
            nums[i], nums[tail] = nums[tail], nums[i]
            tail-=1
        else:
            i+=1
```

![image](https://user-images.githubusercontent.com/25105806/131936772-21bba409-becf-49aa-8058-242b09f24c52.png)

<br />

### Approach 5: Two Pointers One Pass 3, sortColorsTwoPtrsOnePass3()
Same idea, different implementation than approach 3.

```python3
def sortColorsTwoPtrsOnePass3(self, nums: List[int]) -> None: 
    head = 0
    tail = len(nums)-1
    i = 0
    while i<=tail:
        if nums[i]==0:
            nums[i], nums[head] = nums[head], nums[i]
            head+=1
            i+=1
        elif nums[i]==2:
            # i is not changed because we need to see if the exchanged value is still 2
            nums[i], nums[tail] = nums[tail], nums[i]
            tail-=1
        else:
            i+=1
```

![image](https://user-images.githubusercontent.com/25105806/131936875-b266183d-9e0a-4b6e-a291-646c646554c6.png)

<br />

### Approach 6: Value Assignment, sortColorsValAssign()
Instead of sorting the list by swapping, we can directly modify the value. Just use two variables to store the ending index of 0's and 1's.

```python3
def sortColorsValAssign(self, nums: List[int]) -> None: 
    # zero is the ending index of group 0
    # one is the ending index of group 1
    zero, one = 0, 0
    for i in range(len(nums)):
        num = nums[i]
        nums[i] = 2
        # if the original number is 0 or 1, we need to 'move' it to the front
        # by changing current number to 2, and changing the ending index of 1 to 1
        if num == 1:
            nums[one] = 1
            one += 1
        # if the original number is 0, we need to not only update ending index of 1 but also ending index of 0
        # because 1 is after 0, updating 0 also requires updating 1
        elif num == 0:
            # equivalent to shift 1 to the right by one and shift 0 to the right by 1
            nums[one] = 1
            nums[zero] = 0
            one += 1
            zero += 1
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/131937003-13aa7f06-cf71-4c0b-8e0e-b54b9533ebc9.png)
