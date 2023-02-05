-- USING THE TWITTER.SQL DATABASE

-- 1. What query would you run to get all tweets from the user id of 1?
SELECT * -- "*" means ALL
FROM users
LEFT JOIN tweets ON users.id = tweets.user_id
WHERE users.id = 1;

-- you can just grab the tweets by:
SELECT tweets.tweet
FROM users
LEFT JOIN tweets ON users.id = tweets.user_id
WHERE users.id = 1;

-- You can rename the output column that you want by adding the "AS"
SELECT tweets.tweet AS kobe_tweets -- we added AS so we can modify the ouput column
FROM users
LEFT JOIN tweets ON users.id = tweets.user_id
WHERE users.id = 1;

-- 2. What query would return all the tweets that the user with id 2 has tagged as favorites?
SELECT first_name, tweet
FROM users
LEFT JOIN faves ON users.id = faves.user_id
LEFT JOIN tweets ON faves.tweet_id = tweets.id
WHERE users.id = 2;

-- 3 What query would you run to get all the tweets that user with id 2, or user with id 1, has tagged as favorites?
SELECT first_name, tweet
FROM users
LEFT JOIN faves ON users.id = faves.user_id
LEFT JOIN tweets ON faves.tweet_id = tweets.id
WHERE users.id = 1 OR users.id = 2;

-- 4. What query would you run to get all the users that are following the user with id 1?
SELECT users.first_name AS followed, users2.first_name AS follower
FROM users
LEFT JOIN follows ON users.id = follows.followed_id
LEFT JOIN users AS users2 ON users2.id = follows.follower_id
WHERE users.id = 1;

-- 5. What query would you run to get all users that are not following the user with id of 2?
SELECT *
FROM users
WHERE users.id NOT IN (
SELECT follower_id
FROM follows
WHERE followed_id = 2
) AND users.id != 2;

-- We can run functions on specific columns and often times it is paired up with the GROUP BY statement.
-- We will have plenty of practice with functions in the next tab.
SELECT users.first_name AS user, COUNT(users2.first_name) AS follower_count
FROM users
LEFT JOIN follows
ON users.id = follows.followed_id
LEFT JOIN users AS users2
ON users2.id = follows.follower_id
WHERE users.id = 1
GROUP BY users.id;

-- LEFT JOIN VS JOIN

-- LEFT JOIN:
SELECT first_name, tweet
FROM users
LEFT JOIN tweets
ON users.id = tweets.user_id;
-- Notice that this result includes a final row containing Rajon with no associated tweet. 

-- JOIN
SELECT first_name, tweet
FROM users
JOIN tweets
ON users.id = tweets.user_id;
-- Rajon is omitted from the table. When SQL uses the keyword JOIN,
-- it only includes those records that have matches on both sides.
-- It will omit any records that don't have a 'partner'. 











