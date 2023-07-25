# Duplicate Emails problem
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/08112370-ecc0-44e8-b57c-9b8eb9793f23)

Leetcode link: https://leetcode.com/problems/duplicate-emails/description/

<br />

### Approach 1: 

Duplicate emails in `Person` table is just rows with different id than other rows but with same email. We can simply select from `Person` twice, then constructing conditions to find rows with different id and same email:

```sql
SELECT DISTINCT(p1.Email) AS Email
FROM Person AS p1, Person AS p2
WHERE p1.id != p2.id AND p1.email = p2.email;
```

Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/5a13667c-fc17-45bb-a07f-1045f4da06de)

<br />

### Approach 2: 

Instead of selecting from `Person` twice, we can simply group by email and check for occurrences because duplicate emails will have more than one count.

```sql
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1
```

Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/c6115c62-f42d-4f86-8488-709dce56053a)
