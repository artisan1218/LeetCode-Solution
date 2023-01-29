# %%
from typing import List

class Solution:
    def ladderLengthBFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
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
            visited = set([beginWord]) # we begin with beginWord
            queue = [beginWord]
            result = 1 
            while queue:
                # explore the graph level by level
                for _ in range(len(queue)):
                    word = queue.pop(0)
                    if word == endWord:
                        return result
                    else:
                        # get all patterns of this word and check for its neighbors
                        for i in range(len(word)):
                            pattern = word[:i] + '*' + word[i+1:]
                            for neighbor in adjDict.get(pattern, []):
                                if neighbor not in visited:
                                    queue.append(neighbor)
                                    visited.add(neighbor)
                result += 1 # we increment the path length counter by 1 only after we've explored the entire level
            return 0


    def ladderLengthBiBFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        else:
            wordList.append(beginWord)
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

            # Bidirectional BFS
            beginVisited, endVisited = set([beginWord]), set([endWord])
            beginQ, endQ = [beginWord], [endWord]
            result = 1
            while beginQ and endQ:
                # always search from the end with fewer explored node
                # beginQ always represent the queue with fewer node, not necessarily the top-down queue
                if len(beginQ) > len(endQ):
                    beginQ, endQ = endQ, beginQ
                    beginVisited, endVisited = endVisited, beginVisited
                
                # explore the graph level by level
                for _ in range(len(beginQ)):
                    word = beginQ.pop(0)
                    for i in range(len(word)):
                        pattern = word[:i] + '*' + word[i+1:]
                        for neighbor in adjDict.get(pattern, []):
                            # both visited sets have this node, which means we've reached an overlapping word
                            # we can simply return the result
                            if neighbor in endVisited:
                                return result + 1
                            
                            if neighbor not in beginVisited:
                                beginVisited.add(neighbor)
                                beginQ.append(neighbor)
                result += 1
            return 0


if __name__ == '__main__':
    solver = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(solver.ladderLengthBiBFS(beginWord, endWord, wordList))

# %%



