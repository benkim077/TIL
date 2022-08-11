import sys

sys.stdin = open('input.txt')

T = int(input())

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for tc in range(1, T+1):
    N, K = tuple(map(int, input().split()))

    ans = 0
    # subset에 bit가 있는지 확인
    for subset in range(1 << len(lst)):
        ans_lst = []
        for bit in range(12):
            if subset & (1 << bit) != 0:
                ans_lst += [lst[bit]]
        # bit의 갯수가 N이라면
        if len(ans_lst) == N:
            sm = 0
            # 요소의 합을 더해서
            for i in range(N):
                sm += ans_lst[i]
            # K 인지 확인
            if sm == K:
                ans += 1

    print(f'#{tc} {ans}')

'''
비트마스킹을 통해 특정 비트의 값을 확인할 수 있다.
그래서 subset & (1 << bit) 연산을 비트 자리 수(12) 만큼 수행하는 것이다.
그렇게 비트마스킹을 다 했으면, 특정 subset이 어떤 원소를 갖는지 알 수 있다. (정확히는 idx를 파악할 수 있다.)
'''

'''
만약 (subset >> bit) & 1 == 1 이라 한다면,
0또는 1이 나오는 결과가 나온다. 비트마스킹 연산 결과를 활용하고 싶다면 이런 방법을 사용하자.
'''