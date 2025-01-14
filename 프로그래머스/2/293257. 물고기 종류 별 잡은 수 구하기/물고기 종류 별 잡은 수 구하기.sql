SELECT COUNT(*) AS FISH_COUNT, FISH_NAME
FROM FISH_INFO AS f JOIN FISH_NAME_INFO AS n ON f.FISH_TYPE = n.FISH_TYPE
GROUP BY FISH_NAME
ORDER BY FISH_COUNT DESC;
