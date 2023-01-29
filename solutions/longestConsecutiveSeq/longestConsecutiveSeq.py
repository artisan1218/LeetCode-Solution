# %%
from typing import List

class Solution:
    def longestConsecutiveExpand(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        seen = set()
        for num in nums:
            seen.add(num)
            left = num - 1 # we need left or right to make this num a streak
            right = num + 1
            while left in numSet or right in numSet:
                if left in numSet:
                    left -= 1
                    seen.add(left)
                if right in numSet:
                    right += 1
                    seen.add(right)
                
            longest = max(longest, right-left-1)

            if len(seen) == len(numSet):
                break
        return longest
        
    def longestConsecutiveFindStart(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet: # we want to iterate over the set not original num list because set removes duplicates and it's faster
            if num-1 not in numSet: # this is the start of a streak
                end = num + 1 # looking for the end of the streak
                while end in numSet:
                    end += 1
                longest = max(longest, end-num)
        return longest

if __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    solver = Solution()
    print(solver.longestConsecutiveFindStart(nums))

# %%



