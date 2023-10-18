# Repeated DNA Sequences problem
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/1c903946-e99f-4d41-a5aa-f1be09e6367a)


Leetcode link: https://leetcode.com/problems/repeated-dna-sequences/description/

<br />

### Approach 1: Sliding Window, findRepeatedDnaSequences()

Since we want DNA sequences with occurrences greater than 1, it's straightforward to think of making a hashset/hashmap to count the occurrences of each DNA sequences, then pick the sequences with value more than 1.

```sql
def findRepeatedDnaSequences(self, s: str) -> List[str]:
	if len(s) < 10:
		return []
	
	counter = dict()
	for i in range(0, len(s)-9):
		seq = s[i:i+10]
		if seq not in counter:
			counter[seq] = 1
		else:
			counter[seq] += 1
	return [seq for seq in counter if counter[seq]>1]
```

Time complexity is O(n):
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/ff895b55-da22-450e-b06b-9bc4b6073a09)
