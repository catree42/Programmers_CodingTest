-- 코드를 작성해주세요
SELECT COUNT(T.LENGTH) AS FISH_COUNT, MAX(T.LENGTH) AS MAX_LENGTH, FISH_TYPE
FROM (
    SELECT FISH_TYPE, IFNULL(LENGTH,10) AS LENGTH
    FROM FISH_INFO
) AS T
GROUP BY FISH_TYPE
HAVING AVG(T.LENGTH) >= 33
ORDER BY FISH_TYPE;