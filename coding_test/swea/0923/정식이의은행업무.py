import sys
sys.stdin = open('input.txt')


def n_to_h(n, lst, length):
    sm = 0
    for i in range(length):
        sm += lst[i] * (n ** (length - i - 1))
    return sm


T = int(input())
for tc in range(1, T + 1):
    a2_data = list(map(int, input()))
    b3_data = list(map(int, input()))
    A, B = len(a2_data), len(b3_data)

    # bit
    a2_transform = []
    for i in range(A):
        a2_data[i] = bool(a2_data[i] - 1)
        a2_transform.append(n_to_h(2, a2_data, A))
        a2_data[i] = bool(a2_data[i] - 1)
    # print(a2_transform)

    a3_transform = []
    for i in range(B):
        if b3_data[i] == 0:
            b3_data[i] = 1
            a3_transform.append(n_to_h(3, b3_data, B))
            b3_data[i] = 2
            a3_transform.append(n_to_h(3, b3_data, B))
            b3_data[i] = 0
        elif b3_data[i] == 1:
            b3_data[i] = 0
            a3_transform.append(n_to_h(3, b3_data, B))
            b3_data[i] = 2
            a3_transform.append(n_to_h(3, b3_data, B))
            b3_data[i] = 1
        elif b3_data[i] == 2:
            b3_data[i] = 0
            a3_transform.append(n_to_h(3, b3_data, B))
            b3_data[i] = 1
            a3_transform.append(n_to_h(3, b3_data, B))
            b3_data[i] = 2
    # print(a3_transform)

    for num in a2_transform:
        if num in a3_transform:
            ans = num
            break

    print(f'#{tc} {ans}')