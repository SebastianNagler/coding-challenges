SELECT aStart.machine_id, ROUND(AVG(aEnd.timestamp - aStart.timestamp), 3) AS processing_time
FROM (SELECT machine_id, process_id, timestamp FROM Activity WHERE activity_type = 'start') aStart JOIN 
(SELECT machine_id, process_id, timestamp FROM Activity WHERE activity_type = 'end') aEnd ON (aStart.machine_id, aStart.process_id) = (aEnd.machine_id, aEnd.process_id)
GROUP BY machine_id