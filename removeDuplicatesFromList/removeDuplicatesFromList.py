from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        else:
            modifier = 1 # the current index of the updated list, to update list
            cursor = 0 # the index of the traverser, to read new element
            while cursor < len(nums):
                # if the new element is equal to the latest element of the 
                # updated list, we skip this index and check the next one. 
                # if the new element is different, then add it to updated list and update length
                if nums[modifier-1] != nums[cursor]:
                    nums[modifier] = nums[cursor]
                    modifier+=1
                cursor+=1
            return modifier

if __name__ == "__main__":
    solver = Solution()
    
    inputList = [1,2,3,3,4,5]
    length = solver.removeDuplicates(inputList)
    print("length is: ", length)
    print(inputList[:length])






