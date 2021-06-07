# Implement strStr() problem
* Implement strStr()/indexOf().
* Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
* For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

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

Since we will iterate over the string `haystack` and use slicing to check equality, which is also a O(n) operation, the time complexity is O(kn) where k is the window size, which is equal to `len(needle)`.
![image](https://user-images.githubusercontent.com/25105806/120944435-4f986880-c6e9-11eb-914e-10aa43b60c73.png)


<br />

### Approach 2: Sliding Window Improved, strStrImprovedSlidingWindow()
The comparsion using slicing is too expensive, turns out we can simplify this process by only checking the first char of the `needle` with every char in `haystack`, if the first char matches, then we can proceed to check the remaining char in `needle`. This way, the comparsion using slicing only happens when the first char matches.\

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
Time complexity reduces to O(n+k\*a), k is the length of window, a is the number of char in `haystack` that matches the first char of `needle`, n is simply the length of `haystack`.
![image](https://user-images.githubusercontent.com/25105806/120944565-0dbbf200-c6ea-11eb-8a53-da53f124b176.png)

<br />

### Approach 3: Two Pointers, strStrTwoPointers()
We can also use two pointers to solve this. One pointer points to the `haystack` and the other one points to `needle`. We will check equality one char a time. The idea is to first compare the first char of the `needle` with `haystack`, if they match, then check the second char of `needle` with the next char in `haystack`, if they still match, then check the next one, if not, then reset pointer in `needle` back to first char and reset pointer in `haystack` back to the next char of machting char. Repeat this process until we reach the end of `haystack` or `needle`.\

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

Time complexity is O(n)

![image](https://user-images.githubusercontent.com/25105806/120944703-caae4e80-c6ea-11eb-9ca5-535039fb30d2.png)



