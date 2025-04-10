-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES)
FROM (
    SELECT BOOK_ID, SALES
    FROM BOOK_SALES 
    WHERE SALES_DATE LIKE "2022-01%"
) AS S JOIN BOOK AS B ON S.BOOK_ID = B.BOOK_ID
GROUP BY CATEGORY
ORDER BY CATEGORY;