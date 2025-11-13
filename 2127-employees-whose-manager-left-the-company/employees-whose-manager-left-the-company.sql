SELECT
    e1.employee_id
FROM 
    Employees AS e1
    LEFT JOIN 
    (SELECT employee_id, name FROM Employees) AS e2
    ON (e1.manager_id = e2.employee_id)
WHERE
    salary < 30000 AND e2.name IS NULL AND manager_id IS NOT NULL
ORDER BY employee_id