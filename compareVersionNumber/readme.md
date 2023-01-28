# Compare Version Numbers problem
![image](https://user-images.githubusercontent.com/25105806/215246577-56ff1f7c-b2e7-4f88-b7be-d5f5ce8626c6.png)


Leetcode link: https://leetcode.com/problems/compare-version-numbers/description/

<br />

### Approach 1: `zip` Function, compareVersionZip()

The idea is to first split the version by `.`, then iterate over two version lists at the same time using `zip` function, convert each verstion digit to int and compare them. But since `zip` only iterate both lists for the shortest length, we have to deal with the remaining longer list if they are not the same length.

```python3
def compareVersionZip(self, version1: str, version2: str) -> int:
	split1 = version1.split('.')
	split2 = version2.split('.')

	for d1, d2 in zip(split1, split2):
		if int(d1) < int(d2):
			return -1
		elif int(d1) > int(d2):
			return 1

	if len(split1) > len(split2):
		for i in range(len(split2), len(split1)):
			if int(split1[i]) > 0:
				return 1
	else:
		for i in range(len(split1), len(split2)):
			if int(split2[i]) > 0:
				return -1
	return 0
```

Time complexity is O(n) where n is the length of the longest version:
![image](https://user-images.githubusercontent.com/25105806/215247839-3df34bfc-0d0a-4942-b9ad-7f974424a88c.png)


<br />

### Approach 2: `zip_longest` Function, compareVersionZipLongest()

Similar to Approach #1, we this time we use `zip_longest` function in `itertools`, this will iterate both lists for the longest length and shorter list will be padded with `None`. We only need a `if` for such case.

```python3
def compareVersionZipLongest(self, version1: str, version2: str) -> int:
	split1 = version1.split('.')
	split2 = version2.split('.')

	for d1, d2 in zip_longest(split1, split2):
		d1 = int(d1) if d1!=None else 0
		d2 = int(d2) if d2!=None else 0
		if d1 < d2:
			return -1
		elif d1 > d2:
			return 1
	return 0
```

Time complexity is O(n) where n is the length of longest version:
![image](https://user-images.githubusercontent.com/25105806/215247956-824c68ef-86ea-4e22-a4c1-1d2fb76f7072.png)
