CREATE VIEW errors AS
SELECT date_trunc('day', time) as day, count(status) as visits
FROM log
WHERE status != '200 OK'
GROUP BY day;

CREATE VIEW total_visits AS
SELECT date_trunc('day', time) as day, count(status) as visits
FROM log
GROUP BY day;