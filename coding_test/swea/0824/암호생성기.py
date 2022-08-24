import sys

sys.stdin = open('input.txt')

# 원형큐를 활용한 풀이
def encryption(plaintext):
    N = len(plaintext)
    c_q = plaintext                 # 원형 큐
    strg = ''                       # 리턴할 때 사용할 str

    front = 0
    rear = N - 1
    while True:
        for k in range(1, 6):
            front = (front + 1) % N     # deQ
            rear = (rear + 1) % N       # enQ
            c_q[rear] -= k              # - k

            if c_q[rear] <= 0:          # 0 이하인지 체크
                c_q[rear] = 0               # 0으로 바꿔주기

                for i in range(N):          # 리턴 포맷팅
                    strg += ' ' + str(c_q[(rear + 1 + i) % N])
                return strg



'''
def encryption(plaintext):
    front = 0
    rear = 7
    while True:
        for k in range(1, 6):
            plaintext.append(plaintext.pop(front) - k)
            if plaintext[rear] <= 0:
                plaintext[rear] = 0
                return plaintext    # 암호화된 문서 리턴
'''

T = 8
for _ in range(1, T + 1):
    tc = input()
    data = list(map(int, input().split()))
    ans = encryption(data)
    print(f'#{tc}{ans}')
