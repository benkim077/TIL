import sys
sys.stdin = open('input.txt')


def solve(lst):
    N = len(lst)
    
    # 입력값 확인
    if len(lst[-1]) != 3:
        return 'ERROR'

    # 중복 카드가 있는 경우 => 에러
    for i in range(N - 1):
        for j in range(i + 1, N):
            if lst[i] == lst[j]:
                return 'ERROR'

    # 모자란 카드 숫자
    cnt = {'S': 13, # 스페이드
           'D': 13, # 다이아몬드
           'H': 13, # 하트
           'C': 13} # 클로버
    
    # 모자란 카드 수가 음수가 되면 => 에러
    for k in range(N):
        cnt[lst[k][0]] -= 1
        if cnt[lst[k][0]] < 0:
            return 'ERROR'

    # 정상일 경우의 출력
    return ' '.join(map(str, [cnt['S'], cnt['D'], cnt['H'], cnt['C']]))


T = int(input())
for tc in range(1, T + 1):
    data = list(input())

    lst = []

    for k in range(len(data) // 3):
        lst.append(data[3 * k:3 * (k + 1)])

    print(f'#{tc} {solve(lst)}')

