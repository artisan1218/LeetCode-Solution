# Second Highest Salary problem
![Screenshot 2023-07-04 at 9 41 47 PM](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/74c979cd-1588-4f70-8dab-32af06247c3f)


Leetcode link: https://leetcode.com/problems/second-highest-salary/description/

<br />

### Approach 1: 

We want the second highest salary, which is the highest salary excluding the highest salary from `Employee` table. We can just use a sub query to get the highest salary and only select those not equal to highest salary, then pick the highest among them.


```code
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary != (SELECT MAX(salary) FROM Employee)
```

Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/c6eed949-3e20-4fc6-89f6-9556d7e16432)
