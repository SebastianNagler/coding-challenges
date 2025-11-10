SELECT MAX(num) AS num
FROM (SELECT num, COUNT(*) AS num_count FROM MyNumbers GROUP BY num) AS MyNumbers2
WHERE num_count = 1