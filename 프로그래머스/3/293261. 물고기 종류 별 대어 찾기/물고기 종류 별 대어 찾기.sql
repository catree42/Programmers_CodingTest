-- 코드를 작성해주세요

SELECT ID, N.FISH_NAME, LENGTH 
FROM FISH_INFO AS I JOIN FISH_NAME_INFO AS N ON I.FISH_TYPE = N.FISH_TYPE
WHERE (LENGTH, I.FISH_TYPE) IN (
    SELECT MAX(LENGTH), FISH_TYPE
    FROM FISH_INFO
    GROUP BY FISH_TYPE
)
ORDER BY ID;

