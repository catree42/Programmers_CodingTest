-- 코드를 작성해주세요
SELECT E.DEPT_ID, DEPT_NAME_EN, AVG_SAL
FROM (
    SELECT DEPT_ID, ROUND(AVG(SAL),0) AS AVG_SAL
    FROM HR_EMPLOYEES 
    GROUP BY DEPT_ID
) AS E JOIN HR_DEPARTMENT AS D ON E.DEPT_ID = D.DEPT_ID
ORDER BY AVG_SAL DESC;