from itertools import combinations

def is_unique(relation, cols):
    seen = []  # 지금까지 본 projection 결과를 저장
    for row in relation:
        # cols에 해당하는 값들로 키를 만든다
        key = tuple(row[c] for c in cols)
        # 이미 본 키와 비교
        duplicate = False
        for s in seen:
            if s == key:
                duplicate = True
                break
        if duplicate:
            return False
        seen.append(key)
    return True

def solution(relation):
    n_cols = len(relation[0])
    candidates = []  # 최종 후보키 조합을 (튜플로) 저장

    # 1) 컬럼 개수 1부터 n_cols까지 조합 생성
    for r in range(1, n_cols + 1):
        for cols in combinations(range(n_cols), r):
            # 2) 최소성 검사: 기존 후보키(prev)가 cols의 부분집합이면 스킵
            minimal = True
            for prev in candidates:
                # prev의 모든 원소가 cols에 들어 있는지 확인
                match_count = 0
                for p in prev:
                    for c in cols:
                        if p == c:
                            match_count += 1
                            break
                # prev 크기만큼 다 카운트됐으면 prev ⊆ cols
                if match_count == len(prev):
                    minimal = False
                    break
            if not minimal:
                continue

            # 3) 유일성 검사
            if is_unique(relation, cols):
                candidates.append(cols)

    return len(candidates)



relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
rs = solution(relation)
print(rs)