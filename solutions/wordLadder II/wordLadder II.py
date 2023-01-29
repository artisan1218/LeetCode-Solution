# %%
from typing import List

class Solution:
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

if __name__ == '__main__':
    solver = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    result = solver.findLadders(beginWord, endWord, wordList)
    print(result)

# %%



