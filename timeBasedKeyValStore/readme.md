# Time Based Key-Value Store problem
<img width="1116" alt="image" src="https://user-images.githubusercontent.com/25105806/137700504-52ff0d6a-c1d6-4600-8b5b-bc6bd717e79c.png">

Leetcode link: https://leetcode.com/problems/time-based-key-value-store/

<br />


### Approach 1: Binary Search
The idea is to store the `key` as dict key and `value`, `timestamp` tuple as value. Then use binary search to search through a list given a `key`

```python
class TimeMap:

    def __init__(self):
        self.dict = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append((value, timestamp))
        else:
            self.dict[key] = [(value, timestamp)]
        
    def get(self, key: str, timestamp: int) -> str:  
        
        pairList = self.dict.get(key, [])
        
        ans = -1
        left = 0
        right = len(pairList)-1
        while left<=right:
            mid = (left+right)//2
            if pairList[mid][1] <= timestamp:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return '' if ans==-1 else pairList[ans][0]
        
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

Time complexity is O(logn):\
<img width="727" alt="image" src="https://user-images.githubusercontent.com/25105806/137700413-4ae00c87-f150-4a40-a3ee-4c78a1f1bf84.png">

