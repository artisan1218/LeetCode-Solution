# Find And Replace in String problem
![image](https://user-images.githubusercontent.com/25105806/136635688-12e354ed-79b5-4a82-b97f-6040c9c78ceb.png)
![image](https://user-images.githubusercontent.com/25105806/136635738-b8a50b6a-d92f-445c-9228-29c583e8f545.png)

Leetcode link: https://leetcode.com/problems/find-and-replace-in-string/

<br />

### Approach 1: Replace Left to Right, findReplaceStringLeftToRight()
The most staightforward way to solve this is to scan from left to right, then check each index in `indices` to match the substring in `sources`, and finally replace with substring in `targets`. In this process we have to maintain a variabel `pre` that keeps track of the sum of length differences between source and target. But we have to sort the indices in ascending order otherwise the `pre` does not work.

```python
def findReplaceStringLeftToRight(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
    pre = 0
    # sort the three tuple in acsending order 
    # so that pre is always the difference between source and target
    for idx, source, target in sorted(zip(indices, sources, targets)):
        # check if source exists at index idx
        if source == s[idx+pre:idx+len(source)+pre]:
            s = s[0:idx+pre] + target + s[idx+pre+len(source):]
            pre += len(target)-len(source)
    return s
```

Actural running time:\
![image](https://user-images.githubusercontent.com/25105806/136635897-8550cae0-a5fc-4639-a68c-096cf5dbb2bf.png)

<br />

### Approach 2: Replace Right to Left, findReplaceStringRightToLeft()
This approach is identical to approach 1 except for the fact that we don't need the `pre` to maintain the length difference because we're scanning the string `s` from right to left. That is, the replaced string is always at the right side of the current index and will not affect the length of the substring at the left side of current index. But this also requires us to sort the `indices` first.

```python
def findReplaceStringRightToLeft(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
    # going from right to left does not require maintaining the delta length between source and target
    for idx, src, tgt in sorted(zip(indices, sources, targets), reverse=True):
        if s[idx:idx+len(src)] == src: # if s[idx:].startswith(src):
            s = s[0:idx] + tgt + s[idx+len(src):]
    return s
```

Actural running time:\
![image](https://user-images.githubusercontent.com/25105806/136636025-c73209d7-3a15-4b0a-ba88-b5c791664fd2.png)

<br />


### Approach 2: Piece Table, findReplaceStringPieceTable()
The idea is to first go over the `indices` to record any matching substring in `s` and `sources`. We will save the value in `indices` as key and index of `indices` as value because the index of `indices` can also be used to get the value in `sources` and `targets`.\
Then we will go over the string `s` character by character and add any matching substring in `targets` to form the new string.

```python
def findReplaceStringPieceTable(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
    table = dict()
    for i in range(len(indices)):
        if s[indices[i]:].startswith(sources[i]):
            table[indices[i]] = i

    result = list()
    i = 0
    while i<len(s):
        if i in table:
            result.append(targets[table[i]])
            i += len(sources[table[i]])
        else:
            result.append(s[i])
            i += 1
    return ''.join(result)
```

Actural running time:\
![image](https://user-images.githubusercontent.com/25105806/136636180-9d5cedec-c6c7-45c6-bd69-f82c8e39846f.png)

