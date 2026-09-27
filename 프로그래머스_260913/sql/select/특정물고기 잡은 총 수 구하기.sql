SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO A
JOIN FISH_NAME_INFO B
ON A.FISH_TYPE = B.FISH_TYPE
WHERE FISH_NAME IN ('BASS', 'SNAPPER')
--주의사항
--전체 마릿수(단일 값)를 원한다면 GROUP BY 없이 COUNT만 쓰는 것이 정석이고, 종류별로 각각의 통계를 보고 싶을 때만 GROUP BY를 출동시키면 됩니다!