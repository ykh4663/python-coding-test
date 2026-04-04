SELECT PT_NAME, PT_NO, GEND_CD, AGE, COALESCE(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME;

/*
COALESCE (널을 다른 값으로 채우기)
목적: NULL이 싫어서 다른 유의미한 값으로 대체하고 싶을 때 사용합니다.

문법: COALESCE(값1, 값2, 값3, ...)

설명: 값1부터 확인해서 가장 먼저 등장하는 NULL이 아닌 값을 반환합니다.

활용:

전화번호가 없으면 '발신자표시제한' 출력

가격이 입력 안 되어 있으면 0원 처리
*/