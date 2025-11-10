SELECT
    class
FROM
    (SELECT class, COUNT(*) AS num_students FROM Courses GROUP BY class) AS c2
WHERE
    num_students >= 5