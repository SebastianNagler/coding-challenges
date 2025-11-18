SELECT
    s1.id, COALESCE(s2.student, s1.student) AS student
FROM
    Seat as s1 LEFT JOIN Seat as s2 ON (FLOOR((s1.id + 1) / 2) = FLOOR((s2.id + 1) / 2) AND s1.id <> s2.id)
ORDER BY
    s1.id