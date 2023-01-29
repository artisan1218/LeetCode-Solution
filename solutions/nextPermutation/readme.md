# Next Permutation problem
* Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
* If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
* The replacement must be in place and use only constant extra memory.

Leetcode link: https://leetcode.com/problems/next-permutation/

<br />

### Approach 1: Narayana Pandita Algorithm, nextPermutation()

Credits to: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order and https://leetcode.com/problems/next-permutation/discuss/13867/C%2B%2B-from-Wikipedia

NP algorithm is a algorithm presented by Narayana Pandita in 14th century. The idea of this algorithm can be divided into four steps:
1. Find the largest index `i` such that `nums[i] < nums[i + 1]`. If no such index exists, just reverse `nums` and we are done.
2. Find the largest index `j > i` such that `nums[i] < nums[j]`.
3. Swap `nums[i]` and `nums[j]`.
4. Reverse the sub-array `nums[i + 1:]`.

![31_Next_Permutation](https://user-images.githubusercontent.com/25105806/121766492-ef4d6080-cb06-11eb-981d-a47990e20315.gif)

```python3
def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    i = len(nums) - 2
    # Find the largest index i such that nums[i] < nums[i + 1]. 
    # If no such index exists, just reverse nums and we are done.
    while i>=0 and nums[i] >= nums[i+1]:
        i -= 1

    if i==-1:
        nums.reverse()
    else:
        # Find the largest index j > i such that nums[i] <= nums[j].
        j = len(nums) - 1
        while j>i and nums[j] <= nums[i]:
            j-=1
        # Swap the value of i with that of j.
        nums[i], nums[j] = nums[j], nums[i]

        # Reverse the sub-array nums[i + 1:].
        nums[i+1:] = nums[i+1:][::-1]
    return
```

Time complexity is O(n). In worst case, only two scans of the whole array are needed.\
Actual running time:

![image](https://user-images.githubusercontent.com/25105806/121766478-d2189200-cb06-11eb-9984-01be0cb3563f.png)
