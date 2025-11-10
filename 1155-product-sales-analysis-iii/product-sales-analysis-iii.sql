SELECT 
    s1.product_id, first_year, quantity, price
From 
    Sales AS s1 
    JOIN 
    (SELECT product_id, MIN(year) AS first_year FROM Sales GROUP BY product_id) AS s2 
    ON(s1.product_id = s2.product_id)
WHERE 
    year = first_year