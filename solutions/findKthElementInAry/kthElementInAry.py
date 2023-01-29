# %%
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = len(nums) - k
        # kth = k - 1 if want kth smallest element

        def quickSelect(l, r):
            # similar to quicksort
            # nums[r] is the pivot value
            ptr = l
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[ptr], nums[i] = nums[i], nums[ptr]
                    ptr += 1
            # swap ptr with nums[r](the pivot value) to make
            # every element less than pivot on the LHS of pivot
            # every element greater than pivot on the RHS of pivot
            nums[ptr], nums[r] = nums[r], nums[ptr]

            # ptr is the index of the pivot now
            if kth < ptr:
                # kth element index is less than p, then we know target k will be on the left hand side
                return quickSelect(l, ptr-1)
            elif kth > ptr:
                # kth element index is greater than p, then focus on right part of p
                return quickSelect(ptr+1, r)
            else:
                return nums[ptr]  # kth==p
        return quickSelect(0, len(nums)-1)


# %%
solver = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(solver.findKthLargest(nums, k))

# %%
