#!/usr/bin/env python
# coding: utf-8

# In[46]:


from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        
        # group words in lines
        totalLen = 0
        lineList = []
        for word in words:
            totalLen += len(word)
            if totalLen <= maxWidth:
                lineList.append(word)
                totalLen+=1
            else:
                result.append(lineList)
                lineList = [word]
                totalLen = len(word) + 1
        # append last line
        if lineList:
            result.append(lineList)
            
        # justify lines of words
        for idx, line in enumerate(result):
            if idx==len(result)-1:
                # For the last line of text, it should be left-justified and no extra space is inserted between words.
                result[idx] = (' '.join(line)).ljust(maxWidth)
            else:
                justifiedLine = ' '.join(line)
                # does not need any padding
                if len(justifiedLine) == maxWidth:
                    result[idx] = justifiedLine
                else:
                    # padding
                    if len(line)==1:
                        # there is only one word in this line
                        result[idx] = line[0].ljust(maxWidth)
                    else:
                        totalLenWords = len(''.join(line))
                        totalPadding = maxWidth - totalLenWords
                        totalGaps = len(line)-1
                        if totalPadding % totalGaps == 0:
                            # paddings can be evenly distributed
                            padding = ' ' * int(totalPadding / totalGaps)
                            result[idx] = padding.join(line)
                        else:
                            # cannot be evenly distributed
                            extra = totalPadding % totalGaps
                            base = totalPadding // totalGaps
                            # uneven padding needs 1 more space than based padding
                            extraPadding = ' ' * int(base + 1)
                            basePadding = ' ' * base
                            # connecting uneven padding with even padding
                            justifiedLine = extraPadding.join(line[0:extra+1]) + basePadding + basePadding.join(line[extra+1:])
                            result[idx] = justifiedLine

        return result
        
if __name__ == "__main__":
    solver = Solution()
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 16
    result = solver.fullJustify(words, maxWidth)
    for line in result:
        print(line)
    

