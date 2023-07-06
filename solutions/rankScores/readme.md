# Rank Scores problem
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/925e5515-63e2-42b9-be78-e2d528b51c9a)
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/f5c2116a-c278-4fee-acee-9d54419206e1)


Leetcode link: https://leetcode.com/problems/rank-scores/description/

<br/>


### Approach 1: ROW_NUMBER()

Since we want the ranking of the scores and same score should have same ranking, we first think of sorting the table by unique scores then give it a ranking by `ROW_NUMBER`, this will give us a table that maps each unique score to a ranking, then we can simply left join with `Scores` table to fill in the rankings for each score. 

```sql
SELECT
  s.score,
  r.rank
FROM Scores AS s 
LEFT JOIN (
  SELECT
    row_num.score,
    ROW_NUMBER() OVER () AS 'rank'
  FROM (
    SELECT 
      DISTINCT(score)
    FROM Scores
    ORDER BY score DESC
  ) AS row_num
) AS r ON s.score = r.score
ORDER BY s.score DESC
```

Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/8210556f-cc0f-4560-bc45-448cb18a56f0)

<br/>

### Approach 2: COUNT(DISTINCT score)

We can also think of the ranking of each score as 'how many scores each score are bigger than?'. To answer this question, we need two tables, one is for the result table, with each score and its ranking, the one is for comparison. Note the code below, the main query is used to get the result for each score, the sub-query is for answering the above mentioned question.

```sql
SELECT
  score,
  (
    SELECT COUNT(DISTINCT score) 
    FROM Scores 
    WHERE score >= s.score
  ) AS 'rank'
FROM Scores AS s
ORDER BY score DESC
```

Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/5f967c03-8ed5-4362-9ad6-6142c7e6d4a6)
