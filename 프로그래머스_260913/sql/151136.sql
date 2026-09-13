-- 코드를 입력하세요
SELECT ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
GROUP BY CAR_TYPE
HAVING CAR_TYPE = 'SUV'
--반올림 할 때 ~에서 반올림이면(ex 1번쨰 자리) 0번째까지로 생각해서 ,1을 생략하면 됨