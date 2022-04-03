# twoSum problem
* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
* You may assume that each input would have exactly one solution, and you may not use the same element twice.
* You can return the answer in any order.

Leetcode link: https://leetcode.com/problems/two-sum/

<br />

### Approach 1: Brute force, bruteForce()
For each number in list, go through every other number in the list and test if they add up to target. 

```java
public static int[] bruteForce(int[] nums, int target) {
	int[] result = new int[2];
	int addend = 0;
	int addendIt = 0;
	boolean find = false;
	for (int i = 0; i < nums.length && !find; i++) {
	    addend = nums[i];
	    for (int j = i + 1; j < nums.length && !find; j++) {
          addendIt = nums[j];
          if (addend + addendIt == target) {
              result[0] = i;
              result[1] = j;
              find = true;
          }
	    }
	}
	return result;
}
```

Time complexity is O(n^2):\
![image](https://user-images.githubusercontent.com/25105806/160227036-be353df6-cd5c-4649-bc52-fd31ac32afde.png)

<br />

### Approach 2: twoPassHashMap()
First build a HashMap that stores all number in the list, then iterate through the list to see if the target-num(complement) exists in the HashMap. 

```java
public static int[] hashMapTwoPass(int[] nums, int target) {
  Map<Integer, Integer> s = new HashMap<>();
  for (int i = 0; i < nums.length; i++) {
      s.put(nums[i], i);
  }

  for (int j = 0; j < nums.length; j++) {
      int complement = target - nums[j];
      if (s.containsKey(complement) && s.get(complement) != j) {
          return new int[] { j, s.get(complement) };
      }
  }
  return null;
}
```

Since HashMap has constant lookup time, it saves O(n), So time complexity is O(n), but use space complexity of O(n) to store the HashMap:\
![image](https://user-images.githubusercontent.com/25105806/118185941-f98a1b00-b3f1-11eb-8ddc-d7cd8cc805fb.png)


<br />

### Approach 3: onePassHashMap()
Turns out we can check if the complement exists in the HashMap while building the HashMap. HashMap is the element:index pair of the list. Iterate through the list, if the HashMap contains the complement, then we've found the answer, simply return the current index and the index of the complement; if the HashMap does not contain the complement, then adding this number and its index to the HashMap. 

```java
public static int[] hashMapOnePass(int[] nums, int target) {
    HashMap<Integer, Integer> map = new HashMap<>();
    int[] result = new int[2];

    for (int i = 0; i < nums.length; i++) {
        int addend = nums[i];
        int complement = target - addend;
        if (map.containsKey(complement)) {
            result[0] = map.get(complement);
            result[1] = i;
            return result;
        } else {
            map.put(addend, i);
        }
    }
    return result;
}
```

Since the HashMap has contant lookup time, the overall time complexity is O(n) and space complexity is O(n). Best case is when the two numbers are the first two elements of the list, which will be returned when we get the second element because now the complement is the first element and it's in the HashMap already. Worst case is when either one of the two numbers is at the end of the list, which will not be found until we reach the end.

![image](https://user-images.githubusercontent.com/25105806/118185798-cb0c4000-b3f1-11eb-810c-a6b45f642959.png)

