SELECT 
    person_name
FROM
    (
    SELECT 
        person_name, 
        SUM(weight) OVER(ORDER BY turn) AS weight_cum_sum
    FROM
        Queue
    ORDER BY
        turn
    ) AS q2
WHERE
    weight_cum_sum <= 1000
ORDER BY 
    weight_cum_sum DESC
LIMIT
    1