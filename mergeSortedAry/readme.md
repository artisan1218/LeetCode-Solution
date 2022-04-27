# Merge Sorted Array problem
![image](https://user-images.githubusercontent.com/25105806/133915975-f8f37e95-ae90-4bb2-95ee-3042a4c670a7.png)

Leetcode link: https://leetcode.com/problems/merge-sorted-array/

<br />

### Approach 1: Start from Back, merge()
The key here is to start filling `nums1` from the back, this way we can avoid inserting elements to front. Use three pointers, one at the back of `nums1`, one at the back of `nums2` and one at the `m-1` index of `nums1`. Then start comparing the elements at the back of `nums2` and index `m-1` of `nums1`, pick the greater one (because we fill in from the back, so greater value goes to the end of `nums1` first), add it to end of `nums1`, then decrement the pointer by 1 to check next(previous) element.


```python3
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    mod = m+n-1
    cur1 = m-1
    cur2 = n-1

    # fill in nums1 from back
    while cur1>=0 and cur2>=0:
        if nums1[cur1] > nums2[cur2]:
            nums1[mod] = nums1[cur1]
            cur1-=1
        else:
            nums1[mod] = nums2[cur2]
            cur2-=1
        mod-=1

    # fill in with the rest elements in nums2
    if cur2>=0:
        nums1[0:cur2+1] = nums2[0:cur2+1]
```

Time complexity is O(m+n):\
![image](https://user-images.githubusercontent.com/25105806/133916062-2e887230-4f87-4cf6-870f-0cb3e077f95c.png)
