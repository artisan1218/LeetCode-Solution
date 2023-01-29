# %%
from typing import List

class Solution:
    def minDaysBruteForce(self, bloomDay: List[int], m: int, k: int) -> int:
        def countBouquet(bloomed, k):
            bouquetCount = 0
            rosesCount = 0
            for i in range(len(bloomed)):
                if bloomed[i] and (rosesCount == 0 or bloomed[i-1]): #bloom
                    rosesCount += 1
                    if rosesCount == k:
                        rosesCount = 0
                        bouquetCount += 1
                else:
                    rosesCount = 0
            return bouquetCount

        bloomed = [False] * len(bloomDay)
        checkDays = sorted(list(set(bloomDay)))
        for i in checkDays:
            for j in range(len(bloomDay)):
                if bloomDay[j] == i:
                    bloomed[j] = True
            numBouquet = countBouquet(bloomed, k)
            if numBouquet >= m:
                return i
        
        return -1

    def minDaysBinarySearch(self, bloomDay: List[int], m: int, k: int) -> int:
        def countBouquet(k, bloomDay, midDay):
            bouquetCount = 0
            rosesCount = 0
            for i in range(len(bloomDay)):
                if midDay>=bloomDay[i] and (rosesCount == 0 or midDay>=bloomDay[i-1]): #bloom
                    rosesCount += 1
                    if rosesCount == k:
                        rosesCount = 0
                        bouquetCount += 1
                else:
                    rosesCount = 0
            return bouquetCount
        
        # binary search through all days
        days = sorted(bloomDay)

        # binary search
        lo = 0
        hi = len(days) - 1
        ans = -1
        while lo <= hi:
            mid = (lo+hi)//2
            midDay = days[mid]
            numBouquet = countBouquet(k, bloomDay, midDay)
            if numBouquet >= m:
                hi = mid - 1
                ans = midDay
            else:
                lo = mid + 1

        return ans
            

if __name__ == '__main__':
    solver = Solution()

    bloomDay = [7,7,7,7,12,7,7]
    m = 2
    k = 3

    result = solver.minDaysBinarySearch(bloomDay, m, k)
    print(result)   

# %%



