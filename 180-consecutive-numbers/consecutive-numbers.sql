SELECT DISTINCT
    num AS ConsecutiveNums
FROM
    (
        SELECT 
            num, 
            LAG(num, 1) OVER(ORDER BY id) AS num_lag_1,
            LAG(num, 2) OVER(ORDER BY id) AS num_lag_2
        FROM
            Logs
    ) AS LogsLags
WHERE
    num = num_lag_1
    AND
    num = num_lag_2