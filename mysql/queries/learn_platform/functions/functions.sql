-- MYSQL Functions:

-- ======== Text ==========
-- CONCAT()
SELECT CONCAT('Mr.', ' ', first_name, ' ', last_name) AS full_name FROM clients;
-- CONCAT_WS()
SELECT CONCAT_WS(' ', first_name, last_name, 'cool') AS full_name FROM clients;
-- LENGTH()
SELECT LENGTH(last_name) AS last_len FROM clients;
-- LOWER()
SELECT LOWER(first_name)AS first_lowercase FROM clients;

-- ======= DATE FUNCTIONS =========
-- HOUR()
SELECT HOUR(joined_datetime) AS date_hour, joined_datetime FROM clients;
-- DAYNAME()
SELECT DAYNAME(joined_datetime) AS day_name, joined_datetime FROM clients;
-- MONTH()
SELECT MONTH(joined_datetime) AS month_number, joined_datetime FROM clients;
-- NOW()
SELECT NOW() AS right_now;
-- DATE_FORMAT()
SELECT DATE_FORMAT(joined_datetime, '%W %M %e, %Y') AS day_date FROM clients;