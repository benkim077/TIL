# 재귀 함수 설계
    # 1. 종료 조건
    # 2. 하부 호출을 포함한 단위 작업
# 라이브러리처럼 호출

import sys
sys.stdin = open('input.txt')


lookup_table = [0, 2, 3, 1] # 가위바위보 결과를 미리


# 현재 lst 입력받고, 2칸씩 이긴 사람 리스트를 리턴하는 함수
def get_winner(s, e) -> list:
    # 종료 조건
    if s == e:
        return s

    # 하부 호출을 포함한 단위 작업: 2등분 해서 각각 승자 구하고 최종 승자 구함
    a = get_winner(s, (s + e) // 2)
    b = get_winner((s + e) // 2 + 1, e)

    if lookup_table[data[a]] == data[b]:    # b가 이긴 경우
        return b
    else:                       # 비기거나 a가 이긴 경우
        return a


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [0] + list(map(int, input().split()))

    ans = get_winner(1, N)  # 1 ~ N 사이의 최종 승리자의 index를 리턴하는 함수

    print(f'#{tc} {ans}')
