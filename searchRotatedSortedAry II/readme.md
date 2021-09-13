# Search in Rotated Sorted Array II problem
![image](https://user-images.githubusercontent.com/25105806/132747051-fa5cdaf3-64ab-4bbf-8fdd-8465cba2664b.png)


### Approach 1: Binary Search, search()
The idea is same as [searchRotatedSortedAry](https://github.com/artisan1218/LeetCode-Solution/tree/main/searchRotatedSortedAry), first find the pivot point using a binary search, then find the `target` using another binary search in the correct subarray that contains the `target`. The only difference is that we need to handle the duplicates in the `nums` while using binary search to find the pivot point:
```
#handle the duplicates
while left<right and nums[mid]==nums[left]:
  left+=1
```

Time complexity is O(logn), worst case is O(n) --- when all elements are duplicates\
![image](https://user-images.githubusercontent.com/25105806/132747553-e3ebc633-4734-408e-bbfa-909c9fce7e4e.png)


