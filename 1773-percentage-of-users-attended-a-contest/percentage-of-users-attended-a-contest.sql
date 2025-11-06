SELECT contest_id, ROUND(100 * COUNT(*)/ NumUsersT.NumUsersC, 2) AS percentage
FROM Register CROSS JOIN (SELECT COUNT(*) AS NumUsersC FROM Users) AS NumUsersT
GROUP BY contest_id
ORDER BY percentage DESC, contest_id