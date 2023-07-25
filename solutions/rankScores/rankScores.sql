# Solution 1
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



# Solution 2
SELECT
  score,
  (
    SELECT COUNT(DISTINCT score) 
    FROM Scores 
    WHERE score >= s.score
  ) AS 'rank'
FROM Scores AS s
ORDER BY score DESC

