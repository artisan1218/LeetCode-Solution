# RemoveB problem
There is a string S consisting of N letters 'a' and 'b'. In one move, a single letter can be removed. Removing the first or the last letter in the string costs 1 and removing any other letter costs 2. After removing a letter from the middle, the two remaining parts are joined.
For example, given S = "abaab", removing the central letter 'a' from S costs 2. The string that would remain after this operation is "abab".
What is the minimum cost needed to obtain a string without any letter 'b'?
Write a function:
class Solution { public int solution(String S); }
that, given a string S, returns the minimum cost of removals so that the remaining sequence does not contain any letter 'b'.
Examples:
1. Given S = "aabaa", the function should return 2. After removing 'b' from the middle, the remaining sequence contains no 'b's.
2. Given S = "abbaaba", the function should return 5. We can perform the following operations: abbaaba → bbaaba → baaba → aaba → aaa. The cost of these operations is 1 + 1 + 1 + 2 = 5. Another option is: abbaaba → bbaaba → baaba → aaba → aab → aa, resulting in a cost of 1 + 1 + 1 + 1 + 1 = 5.
3. Given S = "bbb", the function should return 3. We can keep removing the last letter from the string until the string is empty.
4. Given S = "abbbaabaabbba", the function should return 10. We can remove the middle letter 'b' (cost 2), then the first four letters ("abbb") and the last four letters ("bbba"), each at a cost of 4.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000];
string S consists only of the characters 'a' and/or 'b'

### Approach 1: Recursion, solution()
The idea is to first find left-most `b` and right-most `b`. Since we don't know where there are more `b`'s in the middle, we use recursion to exhaust all possible ways of removing current `b`: `cost += min(solution(optionOne)+2, solution(optionTwo)+firstIdx+1, solution(optionThree)+lenS-lastIdx)` and pick the way with smallest cost
