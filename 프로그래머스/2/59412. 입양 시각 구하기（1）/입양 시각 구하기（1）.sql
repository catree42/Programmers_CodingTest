-- 코드를 입력하세요
# 서브 쿼리에서 분산 처리 가능하게 하여 분산 시스템 상에서 속도 향상 기대 
SELECT HOUR, COUNT
FROM (
    SELECT HOUR(DATETIME) AS HOUR, COUNT(ANIMAL_ID) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR
) AS T
WHERE HOUR BETWEEN 9 AND 19
ORDER BY HOUR