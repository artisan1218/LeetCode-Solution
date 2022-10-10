# Reverse Words in a String problem
![image](https://user-images.githubusercontent.com/25105806/194787880-a6243981-27a6-4e6c-a4b5-36f5090d82ff.png)

Leetcode link: https://leetcode.com/problems/reverse-words-in-a-string/

<br />

### Approach 1: One-line, reverseWords(), Python

This solution takes advantages of python's slicing and built-in function. However, this is solution is not the best aproach because it requires extra space to do the slicing and reversing. 

```python3
def reverseWords(self, s: str) -> str:
    return ' '.join(s.split()[::-1])
```

Time complexity is O(n) and space complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/194788067-b7e9a6fc-1862-48d0-81f2-b557124249fa.png)


<br />

### Approach 1: Constant Space, reverseWords(), C++

Credits to: https://leetcode.com/problems/reverse-words-in-a-string/discuss/1531693/C++-2-solutions-O(1)-space-Picture-explain-Clean-and-Concise/1452391

The idea behind this approach is to first reverse the entire string `s`, for example `hello world` becomes `dlrow olleh`. Next is step is to modify the string `s` in-place so that there is only one space between words. We use two pointers `fast` and `slow` to do this, `fast` is always ahead of or at the same index as `slow`, which means we will only modify characters that are seen and we will never miss any characters. Then the next step is to reverse each word again and add exact one space. Finally, truncate the remaining characters to the right as we do not need them anymore, and return `s`.

![image](https://user-images.githubusercontent.com/25105806/194788303-ba3665c8-d322-409d-9e4d-b0d42288252f.png)


```cpp
string reverseWords(string s) {
	// reverse the entire string
	reverse(s.begin(), s.end());

	int slow = 0, fast = 0, end = 0;
	while (fast < s.size()) {
		// skip all spaces and find the starting index of the non-space word
		while (fast < s.size() && s[fast] == ' ') {
			fast++;
		}

		// fill the string s with words and only one space between words
		int start = slow;
		while (fast < s.size() && s[fast] != ' ') {
			s[slow++] = s[fast++];
			end = slow;
		}

		// reverse the word
		reverse(s.begin() + start, s.begin() + slow);
		// add a space after each word
		if (slow < s.size()) {
			s[slow++] = ' ';
		}
	}
    
	// truncate the remaining char on the right
	s.resize(end);
	return s;
}
```

Time complexity is O(n) and space complexity is O(1):\
![image](https://user-images.githubusercontent.com/25105806/194788338-ab430aa0-668b-415a-981e-e78924e61e89.png)

