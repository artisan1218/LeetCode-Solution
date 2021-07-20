# Next Permutation problem
* Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
* If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
* The replacement must be in place and use only constant extra memory.


### Approach 1: Narayana Pandita Algorithm, nextPermutation()

Credits to: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order and https://leetcode.com/problems/next-permutation/discuss/13867/C%2B%2B-from-Wikipedia

NP algorithm is a algorithm presented by Narayana Pandita in 14th century. The idea of this algorithm can be divided into four steps:
1. Find the largest index `i` such that `nums[i] < nums[i + 1]`. If no such index exists, just reverse `nums` and we are done.
2. Find the largest index `j > i` such that `nums[i] < nums[j]`.
3. Swap `nums[i]` and `nums[j]`.
4. Reverse the sub-array `nums[i + 1:]`.

![31_Next_Permutation](https://user-images.githubusercontent.com/25105806/121766492-ef4d6080-cb06-11eb-981d-a47990e20315.gif)


Time complexity is O(n). In worst case, only two scans of the whole array are needed.\
Actual running time:

![image](https://user-images.githubusercontent.com/25105806/121766478-d2189200-cb06-11eb-9984-01be0cb3563f.png)
