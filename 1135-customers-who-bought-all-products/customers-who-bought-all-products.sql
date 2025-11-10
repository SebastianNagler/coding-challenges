SELECT
    customer_id
FROM
    (SELECT customer_id, COUNT(DISTINCT product_key) AS num_prods FROM Customer GROUP BY customer_id) AS Customer2
WHERE Customer2.num_prods = (SELECT COUNT(*) FROM Product)