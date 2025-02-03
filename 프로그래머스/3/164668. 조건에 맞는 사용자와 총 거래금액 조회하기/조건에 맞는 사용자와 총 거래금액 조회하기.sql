-- 코드를 입력하세요
SELECT U.USER_ID, NICKNAME, TOTAL_SALES
FROM (
    SELECT WRITER_ID, SUM(PRICE) AS TOTAL_SALES
    FROM USED_GOODS_BOARD
    WHERE STATUS = "DONE"
    GROUP BY WRITER_ID 
    HAVING SUM(PRICE) >= 700000
) AS B JOIN USED_GOODS_USER AS U ON B.WRITER_ID = U.USER_ID
ORDER BY TOTAL_SALES;