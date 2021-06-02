# Regular Expression Matching problem
* Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where: 
* `'.'` Matches any single character.
* `'*'` Matches zero or more of the preceding element.
* The matching should cover the **entire** input string (not partial).

### Approach 1: Dynamic Programming, isMatchDP()
Credits to https://www.youtube.com/watch?v=l3hda49XcDE and https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation

The idea is to build a 2d matrix `match` of size `s.length()+1` and `p.length()+1`, where `match[row][column]` stands for whether pattern `p` up to position `column` matches the text `s` up to position `row`.\
The goal is to find if `match[s.length()][p.length()]==true`. One example matrix is shown below:\
<img src="https://user-images.githubusercontent.com/25105806/118464165-65e87100-b6b5-11eb-9e20-e941ca9c6030.png" height="50%" width="50%">

The way to contruct this matrix is to start from the top left corner, where the value is always `true`, which means **empty pattern always matches empty string.**\
Then for the first row, we fill in the value by iterating chars of `p` to see whether the char of p is `*`. 
1. If it's not `*`, then the value in `match` should be `false` because any char pattern does not match empty string, we can simply check the next char because the matrix will have default value of false. 
2. If the char is indeed `*`, then check the char two indices before `*`, if that char in match is true, then the current column is also true because that's sayiny adding this Kleene star operation does not affect the matching.\

e.g. if `"abc"` matches a string, then `"abcd*"` still matches that string

Then for each row of the matrix, we iterate over every column of that row. There are three cases:
1. the new char in `s` and `p` are the same or the char in `p` is a dot(`'.'`), which means adding this char does not change the current result, then simply assign the value at position (row, column) to be the value at position (row-1, column-1) because (row-1, column-1) stands for not adding this char.\
e.g. for `s="abc"` and `p="ab*c"`, if `s[2]==p[3]`, which means `'c'=='c'`, then the value only depends on if `"ab*"` matches `"ab"`, and this value is stored at `match[row-1][column-1]`.
<img src="https://user-images.githubusercontent.com/25105806/118466166-74378c80-b6b7-11eb-868f-e4f879cd4a25.png" height="60%" width="60%">

2. the new char in `p` is a kleene star(`'*'`). We have two sub cases here:
    1. if the `char*` is considered as empty, is the result true?\
    The result of row `s` up to position `column-2` is true, which means the `'*'`can be considered as empty.\
		e.g. for `s="a"` and `p="a*b*"`, if `"a*"` matches `"a"`, then `"a*b*"` also matches `"a"`. Adding `"b*"` does not change the result.
    2. if the `char*` is considered once or more times, is the result true?\
    The char before `'*'` in `p` is equal to `s` at row-1 (the current s char) or the char before `'*'` is a dot(`'.'`), which matches any char.\
    e.g. for `s="ab"`, `p="ab*"`, `"a"` alone does not match `"ab"`. `s[2-1]==p[3-2]=="b"`, so the value only depends on whether `"ab*"` maches `"a"`.
    <img src="https://user-images.githubusercontent.com/25105806/118468369-8a464c80-b6b9-11eb-88e6-5d88a1e855df.png" height="70%" width="70%">

3. the new char in `s` and `p` are not the same, the value will be false, which is default value, so no need to explicitly assign.

Time complexity is O(m\*n) because we iterate through each spot in the matrix of m\*n. Space complexity is also O(m\*n) because we need to store a matrix of size m\*n

![image](https://user-images.githubusercontent.com/25105806/118468815-fb85ff80-b6b9-11eb-9432-a0836139b509.png)


### Approach 2: DFA/NFA, Skipped

Since every regular expression can be represented by an NFA and every NFA has equivalent DFA, it's viable that we construct a DFA according to the given pattern `p` and run the string `s` on that state machine to see if the string ends at accept state. However this approach is skipped due to difficulty of constructing valid DFA from pattern `p`. It is easier to construct NFA out of pattern `p` but NFA is not that efficient.
