# Word Ladder II problem
![image](https://user-images.githubusercontent.com/25105806/154579743-053e6b37-f15a-4f55-9108-0d6bb2815eef.png)

Leetcode Link: https://leetcode.com/problems/word-ladder-ii/

<br />

### Approach 1: BFS, ladderLengthBFS1(), ladderLengthBFS2()
Reference: https://leetcode.com/problems/word-ladder-ii/discuss/490116/Three-Python-solutions%3A-Only-BFS-BFS%2BDFS-biBFS%2B-DFS

The basic idea and structure of the solution is mostly based on [Word Ladder](https://github.com/artisan1218/LeetCode-Solution/tree/main/wordLadder) problem. We still use BFS as the data structure because we are going to find the shortest path. The difference is that we need to keep track of the path we take to get to each word in the graph. So the `queue` contains a list of list instead of list of word. The list represent the path we take to get to this word. 

Another difference is that we need to update the `visited` set only after we've explored all new words in the same level, otherwise we will only get one shorest path instead of all shortest path. This is way we use a variable called `sameLevelVisited` to temporarily store the new neighbors before adding them to `visited`.

```python3
def findLaddersBFS1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    if endWord not in wordList:
        return []
    else:
        # creating adjDictacency list
        # adjDict stores every possible pattern of each word as key and the corresponding word as value
        adjDict = dict()
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:] # pattern = '*ot', 'h*t' and 'ho*' for word 'hot'
                if pattern not in adjDict:
                    adjDict[pattern] = [word]
                else:
                    adjDict[pattern].append(word)

        # BFS
        queue = [[beginWord]]
        visited = set([beginWord])
        result = []
        while queue and len(result)==0:
            '''
            sameLevelVisited is used to guarantee words in one level can visit common words in the next level. 
            For example, in the 4th level, the words are [dog, log], the last level is [cog]. 
            In the first iteration, 'dog' goes to 'cog', sameLevelVisited will go from [] to [cog], 
            but visited remains []. In the second iteration, 'log' goes to 'cog', 
            sameLevelVisited will go from [] to [cog]. Only after finishing these two iterations, 
            visited will be updated to [cog]. So in a word, with sameLevelVisited, we can visit the 
            next level several times and get several paths, without it, we can only get one path.
            '''
            sameLevelVisited = set() # To allow a word be visited more than once at the current level

            for _ in range(len(queue)):
                wordSeq = queue.pop(0)
                if wordSeq[-1] == endWord:
                    result.append(wordSeq)
                else:
                    # get all patterns of this word and check for its neighbors
                    word = wordSeq[-1]
                    for i in range(len(word)):
                        pattern = word[:i] + '*' + word[i+1:]
                        for neighbor in adjDict.get(pattern, []):
                            if neighbor not in visited:
                                sameLevelVisited.add(neighbor) 
                                queue.append(wordSeq + [neighbor])
            visited = visited.union(sameLevelVisited)
        return result
```

The other way of doing the `sameLevelVisited` is to update the previous level visited words before we going through next level neighbors:
```python3
def findLaddersBFS2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    if endWord not in wordList:
        return []
    else:
        # creating adjDictacency list
        # adjDict stores every possible pattern of each word as key and the corresponding word as value
        adjDict = dict()
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:] # pattern = '*ot', 'h*t' and 'ho*' for word 'hot'
                if pattern not in adjDict:
                    adjDict[pattern] = [word]
                else:
                    adjDict[pattern].append(word)

        # BFS
        queue = [[beginWord]]
        visited = set()
        result = []
        while queue and len(result)==0:
            for _ in range(len(queue)):
                wordSeq = queue.pop(0)
                if wordSeq[-1] == endWord:
                    result.append(wordSeq)
                else:
                    # get all patterns of this word and check for its neighbors
                    word = wordSeq[-1]
                    visited.add(word) # alternatively, we can add the word in previous level before exploring next level words
                    for i in range(len(word)):
                        pattern = word[:i] + '*' + word[i+1:]
                        for neighbor in adjDict.get(pattern, []):
                            if neighbor not in visited:
                                queue.append(wordSeq + [neighbor])
        return result
```


Time complexity is O(nm^2) where n is the number of words in wordList and m is the number of possible patterns. n\*m is the max number of edges we need to explore, m is the number of neighbor we need to find for each word:\
![image](https://user-images.githubusercontent.com/25105806/154580912-18279cfb-1075-48e0-bfdb-ccf4ac878374.png)
