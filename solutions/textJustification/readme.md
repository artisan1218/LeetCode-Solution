# Text Justification problem
* Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
* You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
* Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
* For the last line of text, it should be left-justified and no extra space is inserted between words.
* Note: A word is defined as a character sequence consisting of non-space characters only. Each word's length is guaranteed to be greater than 0 and not exceed maxWidth. The input array words contains at least one word.

Leetcode link: https://leetcode.com/problems/text-justification/

<br />

### Approach 1: fullJustify()
First step is to group the words in `words` into different lines so that we can deal with each line easily. Then loop through each line, padding each line with correct number of spaces using `.join()` and `.ljust()` function.

```python3
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
```

Time complexity is O(n):\
![1af078d1e14825eb94662a0b6800d17](https://user-images.githubusercontent.com/25105806/130343707-7dc43106-7508-45a4-974b-d698e3fbca30.png)

