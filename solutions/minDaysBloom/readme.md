# Minimum Number of Days to Make m Bouquets problem
![image](https://user-images.githubusercontent.com/25105806/149723867-a3fdffc2-3f42-4af1-a92a-fc96f2b392da.png)

Leetcode link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

<br />

### Approach 1: Brute Force, minDaysBruteForce()
This approach is a brute force solution. We simply go through all days in `bloomDay` in order from lowest to highest, then choose the first one that meet the requirement of `m` bouquets.

```python
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
```

Time complexity is O(n^2) and is TLE.

<br />

### Approach 2: Binary Search, minDaysBinarySearch()
We noticed that we can sort the `bloomDays` in ascending order and the more days we wait, the more bouquets we will make. So the bouquets is strictly non-decreasing given more days. This means we can use binary search to search through `bloomDay`, if a certain day generates more bouquets than required, we decrease the day by half. If a certain day generates less bouquets than required, we increase the day by half. 

```python
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
```

Time complexity is O(nlogn), the sorting takes O(nlogn) and the binary search with bouquets calculation takes O(nlogn):\
![image](https://user-images.githubusercontent.com/25105806/149724900-a06c1a88-d707-4996-b444-c88cf4fe6d53.png)


