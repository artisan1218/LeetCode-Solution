# Word Pattern problem
<img width="724" alt="image" src="https://user-images.githubusercontent.com/25105806/163648454-165f95bb-189b-4270-8d36-6895d9930ee7.png">

Leetcode link: https://leetcode.com/problems/word-pattern/

<br />

### Approach 1: Two Maps/Dict, wordPattern(), Python3, CPP

The idea is to first split the input string `s` by space so that we can work on individual words. Then simply use two maps to store the pattern-word and word-pattern relations in two maps because it requires a bijection, which means each word has to be mapped to an unique pattern and vice versa. 

Python implementation is simpler because we can use the built-in `.split()` function:
```python3
def wordPattern(self, pattern: str, s: str) -> bool:
    wordList = s.split(' ')
    if len(wordList) == len(pattern):
        word2p = dict()
        p2word = dict()
        for word, p in zip(wordList, pattern):
            if word not in word2p:
                word2p[word] = p
            elif word2p[word] != p:
                    return False

            if p not in p2word:
                p2word[p] = word
            elif p2word[p] != word:
                    return False
        return True
    else:
        return False
```

In CPP:
```cpp
bool wordPattern(string pattern, string s) {
  // split the string by space
  vector<string> strSplits;
  int start = 0;
  int end = 0;
  while (end < s.length()) {
      if (s[end] == ' ') {
          strSplits.push_back(s.substr(start, end - start));
          start = end + 1;
      }
      end++;
  }
  strSplits.push_back(s.substr(start, end - start + 1));

  if (strSplits.size() == pattern.length()) {
      unordered_map<char, string> char2Str;
      unordered_map<string, char> str2Char;

      for (int i = 0; i < strSplits.size(); i++) {
          char p = pattern.at(i);
          string str = strSplits.at(i);

          if (char2Str.find(p) != char2Str.end()) {
              if (char2Str[p] != str) {
                  return false;
              }
          } else {
              char2Str[p] = str;
          }

          if (str2Char.find(str) != str2Char.end()) {
              if (str2Char[str] != p) {
                  return false;
              }
          } else {
              str2Char[str] = p;
          }
      }
      return true;
  } else {
      return false;
  }
}
```

Time complexity is O(n):\
<img width="625" alt="image" src="https://user-images.githubusercontent.com/25105806/163648758-7138ebb6-bda3-467b-b904-0f3fcbbfecca.png">


<img width="651" alt="image" src="https://user-images.githubusercontent.com/25105806/163648779-544c00e8-05ff-41ef-98a5-d84a314e3120.png">

      
