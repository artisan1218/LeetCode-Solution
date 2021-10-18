# Snapshot Array problem
<img width="872" alt="image" src="https://user-images.githubusercontent.com/25105806/137702471-f0a2920e-906c-489c-b885-b2fe132d3a45.png">

Leetcode link: https://leetcode.com/problems/snapshot-array/

<br />


### Approach 1: Iteration
The idea is to record the `snap_id` along with each `set` operation and search through all `snap_id` to get the answer

```python
class SnapshotArray:

    def __init__(self, length: int):
        self.snapshotArray = [dict() for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.snapshotArray[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        cur = snap_id
        while cur > 0 and cur not in self.snapshotArray[index]:
            cur -= 1
        return self.snapshotArray[index].get(cur, 0)


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
```

Time complexity is O(n):\
<img width="682" alt="image" src="https://user-images.githubusercontent.com/25105806/137702804-9fae81fb-234b-4b5f-818e-6ffc52515ef8.png">
