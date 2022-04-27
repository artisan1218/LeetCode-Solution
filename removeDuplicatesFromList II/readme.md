# Remove Duplicates from Sorted Array II problem
![image](https://user-images.githubusercontent.com/25105806/132615584-cf3801fe-4d5d-450a-9495-74925438523b.png)

Leetcode link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

<br />

### Approach 1: Two Pointers, removeDuplicates()
Use two pointers both starting at index 0, one for modify the array, another one for getting new values. The `checkCursor` will travel faster than `modCursor` because `checkCursor` will move to the right by one in each iteration.\
We will allow maximum of two duplicates elements in the array, so the key here is to check the elements two indices before the current `checkCursor`, since the array is sorted in acsending order, if the current element is greater than elements 2 indices before it, then we should assign the current value to the index pointed by `modCursor`. Basically, we are overwriting the first k elements with maximum of two repeating characters while keep the remaining part unchanged.

```
^ is modCursor and * is checkCursor

1 1 1 2 2 3 3
^ 
*

1 1 1 2 2 3 3
  ^ 
  *

1 1 1 2 2 3 3
    ^ 
    *

1 1 1 2 2 3 3
    ^ *
Note: 2 is greater than the element two indices before *, which is 1. So update element ^

1 1 2 2 2 3 3
    ^ *
      
1 1 2 2 2 3 3
      ^ *
      
1 1 2 2 2 3 3
        ^ *
Note: 3 is greater than the element two indices before *, which is 2. So update element ^

1 1 2 2 3 3 3
        ^ *
        
1 1 2 2 3 3 3
          ^ *

1 1 2 2 3 3 3
            ^ *
Done
```

```python3
def removeDuplicates(self, nums: List[int]) -> int:
    duplicates = 2
    modCursor = 0
    checkCursor = 0

    while checkCursor<len(nums):
        # for the beginning n words, simply increment the modCursor
        if modCursor < duplicates:
            modCursor+=1
        # this means we've met a new value, it's time to update the elements at modCursor
        elif nums[checkCursor] > nums[modCursor-duplicates]:
            nums[modCursor] = nums[checkCursor]
            modCursor+=1
        checkCursor+=1

    return modCursor
```

We will only read the array once, so the time complexity is O(n):\
![b8b725e518481931c451d44acc3399f](https://user-images.githubusercontent.com/25105806/132616264-e167cf3a-3a4f-4967-a893-979f442272ac.png)
