SELECT reports_to AS employee_id, e2.name, COUNT(*) AS reports_count, ROUND(AVG(age)) AS average_age
FROM 
    Employees AS e1 
    JOIN 
    (SELECT employee_id, name FROM Employees) AS e2 
    ON (e1.reports_to = e2.employee_id)
GROUP BY reports_to
ORDER BY employee_id