# Consecutive Numbers problem
![Screenshot 2023-07-24 at 5 18 26 PM](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/d69c7e8c-56f7-4763-bfae-f9a6a1384843)


Leetcode link: https://leetcode.com/problems/consecutive-numbers/description/

<br />

### Approach 1:

The key part is how to deal with `consecutively` requirement. By defination, consecutive number is just numbers with consecutive ids, so we can start with enforcing ids. We can select from three `Logs` and make sure their ids are consecutive and nums are the same.

```sql
SELECT DISTINCT(l1.num) AS ConsecutiveNums
FROM Logs AS l1, Logs AS l2, Logs AS l3
WHERE l1.id = l2.id - 1 AND l2.id = l3.id - 1 AND l1.num = l2.num AND l2.num = l3.num;
```


Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/cc1bebdc-05a5-4580-b20d-4a508ed8d0a8)
