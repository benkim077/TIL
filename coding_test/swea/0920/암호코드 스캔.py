import sys
sys.stdin = open('input.txt')

hashing = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

pwd = {
    0: [0,0,0,1,1,0,1],
    1: [0,0,1,1,0,0,1],
    2: [0,0,1,0,0,1,1],
    3: [0,1,1,1,1,0,1],
    4: [0,1,0,0,0,1,1],
    5: [0,1,1,0,0,0,1],
    6: [0,1,0,1,1,1,1],
    7: [0,1,1,1,0,1,1],
    8: [0,1,1,0,1,1,1],
    9: [0,0,0,1,0,1,1],
}


def get_sp():
    global si, sj
    for i in range(4, N - 4, 5):
        for j in range(M - 1, 5, -14):
            if data[i][j] != '0':
                j += 1
                while True:
                    if data[i][j] == '0':
                        si, sj = i, j - 1
                        if data[si][sj - 14:sj + 1] not in code_lst:
                            code_lst.append(data[si][sj - 14:sj + 1])
                        break
                    j += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(input().strip()) for _ in range(N)]

    si, sj = 0, 0
    code_lst = []
    get_sp()
    print(code_lst)

    cipher_text = []
    for code in code_lst:
        bin_code = '0000'
        for char in code:
            bin_code += hashing[char]
        cipher_text.append(bin_code)
    print(cipher_text)

    # bin_code를 잘 찾았다고 할 수 있을까?
    # 중간에 0이 들어가는 경우는 없을까?