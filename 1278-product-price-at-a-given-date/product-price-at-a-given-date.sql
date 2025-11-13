SELECT DISTINCT
    p1.product_id, 
    (
        CASE WHEN 
            p2.max_change_date IS NULL 
        THEN 
            10 
        ELSE 
            new_price 
        END
    ) AS price
FROM
    Products AS p1
    LEFT JOIN
    (
        SELECT 
            product_id, MAX(change_date) AS max_change_date
        FROM 
            Products 
        WHERE 
            change_date <= '2019-08-16'
        GROUP BY 
            product_id
    ) AS p2
    ON (p1.product_id = p2.product_id)

WHERE 
    p1.change_date = p2.max_change_date 
    OR 
    p2.max_change_date IS NULL