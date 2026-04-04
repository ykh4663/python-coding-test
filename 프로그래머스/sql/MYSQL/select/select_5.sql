-- 과일로 만든 아이스크림 고르기

SELECT F.FLAVOR
FROM FIRST_HALF AS F
JOIN ICECREAM_INFO AS I
ON F.FLAVOR = I.FLAVOR
WHERE F.TOTAL_ORDER > 3000 AND I.INGREDIENT_TYPE LIKE "fruit_based"
ORDER BY F.TOTAL_ORDER DESC

-- ALIAS는 SELECT에서 선언한거는 WHERE절 같은 곳에서 못씀

-- 쿼리 실행 순서 참고
-- SELECT 부서, SUM(월급)
-- FROM 직원테이블
-- WHERE 퇴사여부 = 'N'   -- 1. [WHERE] 이미 퇴사한 사람은 계산에서 아예 뺌 (참가 자격 박탈)
-- GROUP BY 부서          -- 2. [GROUP BY] 남은 '재직자'들끼리만 부서별로 뭉침