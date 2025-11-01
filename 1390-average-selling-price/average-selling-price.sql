SELECT Prices.product_id, COALESCE(ROUND(SUM(price * units) / SUM(units), 2), 0) AS average_price
FROM Prices LEFT JOIN UnitsSold ON (Prices.product_id = UnitsSold.product_id AND DATEDIFF(UnitsSold.purchase_date, Prices.start_date) >= 0 AND DATEDIFF(UnitsSold.purchase_date, Prices.end_date) <= 0)
GROUP BY Prices.product_id