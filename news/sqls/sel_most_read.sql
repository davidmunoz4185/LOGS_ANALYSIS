SELECT NAME,
COUNT(*)
FROM AUTHORS INNER JOIN ARTICLES
ON (ARTICLES.AUTHOR = AUTHORS.ID)
INNER JOIN LOG
ON (TRIM(SUBSTR(PATH, length('/article/') +1)) = TRIM(SLUG))
WHERE PATH LIKE '/article/%'
AND STATUS = '200 OK'
GROUP BY 1
ORDER BY 2 DESC;
