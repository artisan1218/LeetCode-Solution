from typing import List
from collections import Counter

class Solution:
    def findSubstringBruteForce(self, s: str, words: List[str]) -> List[int]:
        result = []
        wordLen = len(words[0])
        for strPtr in range(len(s)-wordLen+1):
            # window is the substring bounded by strPointer with the same length as word in words
            window = s[strPtr:strPtr + wordLen]
            # used to move the strPtr without modifying it
            strPtrMover = 0
            tmpWords = words.copy()
            while window in tmpWords:   
                tmpWords.remove(window)              
                strPtrMover += 1
                # get the next window word in s
                window = s[strPtr + wordLen * strPtrMover: strPtr + wordLen * (strPtrMover+1)]
                
            # wordPointer walked all the way to the end of words list, which means every word in the list has been found in s
            if len(tmpWords)==0:
                result.append(strPtr)
                
        return result
    
    '''https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13658/Easy-Two-Map-Solution-(C++Java)'''
    def findSubstringTwoMaps(self, s: str, words: List[str]) -> List[int]:
        result = list()
        # store the word and its frequency in a dict
        count = dict(Counter(words))
        wordLen = len(words[0])
        
        for strPtr in range(len(s)-wordLen*len(words) + 1):
            current = dict()
            window = s[strPtr:strPtr + wordLen]
            # i is used to keep track of how many words we've added to current dict
            # iterate over all word in words list
            for i in range(len(words)):
                if window in count:
                    if window in current:
                        current[window] += 1
                        if current[window] > count[window]:
                            i-=1
                            break
                    else:
                        current[window] = 1
                else:
                    # the window word does not exist in words list
                    # we can directly jump to the end of this word
                    strPtr = strPtr + wordLen * (i+2)
                    i-=1
                    break
                # get next word
                window = s[strPtr + wordLen * (i+1): strPtr + wordLen * (i+2)]
                     
            if i == len(words) - 1:
                result.append(strPtr)

        return result


if __name__ == "__main__":
    solver = Solution()
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    print(solver.findSubstringTwoMaps(s, words))





