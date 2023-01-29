# Implement strStr() problem
* Implement strStr()/indexOf().
* Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
* For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Leetcode link: https://leetcode.com/problems/implement-strstr/

<br />

### Approach 1: Sliding Window, strStrSlidingWindow()
The idea is to fix a window size of `len(needle)`, slide the window from the beginning of the `haystack` one char by one char and check if the `needle` is equal to this window.

```
haystack = h e l l o w o r l d
needle = l l o

1. h e l l o w o r l d
   ^---^
   h e l != l l o, check next one
   
2. h e l l o w o r l d
     ^---^
   e l l != l l o, check next one 
   
3. h e l l o w o r l d
       ^---^
   l l o == l l o, return 
```

```python3
def strStrSlidingWindow(self, haystack: str, needle: str) -> int:
    left = 0
    right = len(needle)
    while right <= len(haystack):
       if haystack[left:right] == needle:
           return left
       else:
           left+=1
           right+=1
    return -1
```

Since we will iterate over the string `haystack` and use slicing to check equality, which is also a O(n) operation, the time complexity is O(kn) where k is the window size, which is equal to `len(needle)`.\
![image](https://user-images.githubusercontent.com/25105806/120944435-4f986880-c6e9-11eb-914e-10aa43b60c73.png)


<br />

### Approach 2: Sliding Window Improved, strStrImprovedSlidingWindow()
The comparsion using slicing is too expensive, turns out we can simplify this process by only checking the first char of the `needle` with every char in `haystack`, if the first char matches, then we can proceed to check the remaining char in `needle`. This way, the comparsion using slicing only happens when the first char matches.

```
haystack = h e l l o w o r l d
needle = l l o

1. h e l l o w o r l d
   ^
   h != l, check next one
   
2. h e l l o w o r l d
     ^
   e != l, check next one 
   
3. h e l l o w o r l d
       ^
   l == l, check if l o == l o
   l o == l o, return
```

```python3
def strStrImprovedSlidingWindow(self, haystack: str, needle: str) -> int:
    if needle == '':
        return 0
    else:
        for idx in range(len(haystack)):
            if haystack[idx] == needle[0]:
                if needle[1:] == haystack[idx+1: idx+len(needle)]:
                    return idx
        return -1
```

Time complexity reduces to O(n+k\*a), k is the length of window, a is the number of char in `haystack` that matches the first char of `needle`, n is simply the length of `haystack`:\
![image](https://user-images.githubusercontent.com/25105806/120944565-0dbbf200-c6ea-11eb-8a53-da53f124b176.png)

<br />

### Approach 3: Two Pointers, strStrTwoPointers()
We can also use two pointers to solve this. One pointer points to the `haystack` and the other one points to `needle`. We will check equality one char a time. The idea is to first compare the first char of the `needle` with `haystack`, if they match, then check the second char of `needle` with the next char in `haystack`, if they still match, then check the next one, if not, then reset pointer in `needle` back to first char and reset pointer in `haystack` back to the next char of machting char. Repeat this process until we reach the end of `haystack` or `needle`.

```
haystack = t h i s i s a t e s t
needle = i s a

1. t h i s i s a t e s t
   ^
   i s a
   ^
   t != i, check next one in haystack
   
2. t h i s i s a t e s t
     ^
   i s a
   ^
   h != i, check next one in haystack
   
3. t h i s i s a t e s t
       ^
   i s a
   ^
   i == i, check next one in haystack and needle

4. t h i s i s a t e s t
         ^
   i s a
     ^
   s == s, check next one in haystack and needle
   
5. t h i s i s a t e s t
           ^
   i s a
       ^
   i != a, reset two pointers

6. t h i s i s a t e s t
         ^
   i s a
   ^
   s != i, check next one in haystack
   
7. t h i s i s a t e s t
           ^
   i s a
   ^
   i == i, check next one in haystack and needle
   
8. t h i s i s a t e s t
             ^
   i s a
     ^
   s == s, check next one in haystack and needle
   
9. t h i s i s a t e s t
               ^
   i s a
       ^
   a == a, reached the end of needle, return
```

```python3
def strStrTwoPointers(self, haystack: str, needle: str) -> int:
    if len(haystack) < len(needle): # early termination
        return -1
    elif needle == '':
        return 0
    else:
        strPtr = 0
        ndlPtr = 0
        while ndlPtr < len(needle) and strPtr < len(haystack): 
            # if they are not equal, check the next char in haystack and reset needle pointer
            if haystack[strPtr] != needle[ndlPtr]:
                # strPtr is not simply +=1 because maybe we're not checking the first char of needle
                strPtr = strPtr - ndlPtr + 1
                ndlPtr = 0
            else: 
                strPtr += 1
                ndlPtr += 1

        # the entire needle has been matched
        if ndlPtr == len(needle):
            return strPtr-ndlPtr
        else:
            return -1
```

Time complexity is O((n-k)\*n):\
![image](https://user-images.githubusercontent.com/25105806/120944703-caae4e80-c6ea-11eb-9ca5-535039fb30d2.png)

<br />

### Approach 4: KMP Algorithm, strStrKMP()

Credits to: https://www.youtube.com/watch?v=GTJr8OvyEVQ and https://github.com/mission-peace/interview/blob/master/src/com/interview/string/SubstringSearch.java

There is even a O(n+k) algorithm called KMP algorithm. The idea is pretty similar to approach 3 except that when a bad match happens, that is, when two chars does not match, KMP algorithm will move the pointer to the next char of common prefix/suffix to avoid checking some of the common prefix/suffix twice, while the two pointers solution will always go the next position of the same char, which will check duplicating chars more than one time. \
Time complexity is O(n+k) where n is size of `haystack` and k is the size of `needle`. First of all, we generate the `nextList` array to show any possible duplicates of prefix and postfix within needle. Then we go through haystack. Every time we see a bad match, move `ndlPtr(needle pointer)` to `nextList[ndlPtr-1]` and keep `strPtr(haystack pointer)` in current position; otherwise, move both of them to next position.


```python3
def strStrKMP(self, haystack: str, needle: str) -> int:
    # generate 'nextList' array, need O(k) time
    i = 1
    j = 0
    strLen = len(haystack)
    ndlLen = len(needle)
    nextList = [0] * ndlLen # nextList stores the jumping index when a bad match happens
    while i < ndlLen:
        # first index in nextList is always 0, which means 0 itself is a common prefix/suffix
        if needle[i] == needle[j]:
            nextList[i] = j + 1
            j += 1
            i += 1
        else:
            if j!=0:
                j = nextList[j-1]
            else:
                nextList[i] = 0
                i+=1

    #the actual checking starts here, need O(n) time
    strPtr = ndlPtr = 0
    while strPtr < strLen and ndlPtr < ndlLen:
        # if the char matches, check the next one
        if haystack[strPtr] == needle[ndlPtr]:
            strPtr += 1
            ndlPtr += 1
        # bad check happend, find the next position needle pointer needs to go according to nextList
        else:
            if ndlPtr != 0:
                # go the char before common prefix/suffix so that we can avoid checking already checked chars
                ndlPtr = nextList[ndlPtr-1]
            else:
                # needle pointer is still at first index, move string pointer to next
                strPtr += 1
    # the entire needle has been matched
    if ndlPtr == ndlLen:
        return strPtr-ndlPtr
    else:
        return -1
```


Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/120967315-2b09b400-c71c-11eb-987c-e9e4a3cb0f61.png)

