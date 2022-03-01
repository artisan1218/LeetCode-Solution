# Inversion problem
* Given an array `arr[]` of size `n`. Three elements `arr[i]`, `arr[j]` and `arr[k]` form an inversion of size 3 if `a[i] > a[j] > a[k]` and `i < j < k`. Find total number of inversions of size 3.


<br />

### Approach 1: Backtracking, inversion()
The idea is to use backtracking algorithm to explore all permutations and count the number of valid inversions. The key is to keep track of current length and the previous number because if the current length reaches 3, that means we've found a valid inversion. And we only consider a number as valid if it's smaller than the previous number in the current sequence. For example, if the current sequence is `[5, 4]`, then next number can be anyone in `[1, 2, 3]`.

We use the `nonlocal` keyword to modify the value of an integer in the nested function.

```python3
def inversion(arr):
    count = 0
    def helper(uniqueArr, curLen, idx, prevNum):
        nonlocal count
        if curLen == 3:
            count += 1
        else:
            for i in range(idx, len(uniqueArr)):
                if curLen==0 or uniqueArr[i] < prevNum:
                    helper(uniqueArr, curLen + 1, i + 1, uniqueArr[i])

    seen = set()
    uniqueArr = list()
    for num in arr:
        if num not in seen:
            seen.add(num)
            uniqueArr.append(num)

    helper(uniqueArr, 0, 0, 0)
    return count
```

Time complexity is O(n^3) in worst case.

<br />

### Approach 2: Backtracking, inversion2()
This solution is similar to approach 1 but instead of counting the number of inversions, we store the content of inversions. To do this, we simply append the valid inversions to a list `result` to store it. 

```python3
def inversion2(arr):
    def helper (arr, curSeq, idx):
        if len(curSeq)== 3:
            result.append(curSeq)
        else:
            for i in range(idx, len(arr)) :
                if len(curSeq)==0 or arr[i] < curSeq[-1]:
                    helper(arr, curSeq+[arr[i]], i + 1)

    result = list()
    seen = set()
    uniqueArr = list()
    for num in arr:
        if num not in seen:
            seen.add(num)
            uniqueArr.append(num)

    helper (uniqueArr, [], 0)
    return result
```

Time complexity is O(n^3) in worst case.

<br />

### Approach 3: inversion3()
This solution uses two loops to do the job. In the first loop, it will count: for each elements in the arr, how many element on the right are smaller than it? This number is simply the count of size-2-inversions for starting with each number.

In the second loop, it will 'connect' the third number to the front of the size-2-inversions. We only care about the count, then simply add up the count for size-2-inversions.

This works because for size-3-inversions starting with a specific number, its counts are simply the sum of all size-2-inversions that are smaller than that number

```python3
def inversion3(arr):
    greater = [0] * len(arr)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                greater[i] += 1
    # count for each elements in the arr, how many element on the right are smaller than it
    # this number is simply the count of size-2-inversions for each number

    result = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                # if arr[i] > arr[j], we can make a size-3-inversion by connecting arr[i].
                # we only care about the count, then simply add up the count for size-2-inversions
                # this works because for size-3-inversions starting with a specific number, its counts 
                # are simply the sum of all size-2-inversions that are smaller than that number
                result += greater[j]

    return result
```

Time complexity is O(n^2)

<br />

### Approach 4: Expand around middle, inversion4()
The idea is to go over the elements of `arr` from index 1 to the end, treat each number as the middle number of the inversion and count how many numbers on the left are greater than the middle number, and how many numbers on the right are smaller than the middle number. Then simply multiply these two counts and add up the result for the rest of `arr`. The multiplication result indicates the number of inversion with `arr[i]` as the middle number. 

```python3
def inversion4(arr):
    result = 0    
    for mid in range(1, len(arr)):
        smaller = 0
        for right in range(mid+1, len(arr)):
            if arr[mid] > arr[right]:
                smaller += 1
        
        greater = 0
        for left in range(0, mid):
            if arr[left] > arr[mid]:
                greater += 1
        
        result += smaller * greater

    return result
```

Time complexity is O(n^2)
