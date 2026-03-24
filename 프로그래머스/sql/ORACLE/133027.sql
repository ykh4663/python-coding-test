SELECT FLAVOR
FROM (
    SELECT F.FLAVOR AS FLAVOR
    FROM FIRST_HALF F, (SELECT FLAVOR, SUM(TOTAL_ORDER) JULY_SUM FROM JULY GROUP BY FLAVOR) J
    WHERE F.FLAVOR = J.FLAVOR
    ORDER BY (F.TOTAL_ORDER + J.JULY_SUM) DESC
)
WHERE ROWNUM <= 3;
-- 오라클의 로우넘은 mysql의 limit과 다르게 동작, order by 보다 먼저 수행되기에 from절에서 서브쿼리 날려서 처리하고
-- rownum으로 잘라버려야 원하는 동작 수행 가능