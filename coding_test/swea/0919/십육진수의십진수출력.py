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

T = int(input())
for tc in range(1, T + 1):
    data = list(input())

    bin_data = ''
    for char in data:
        bin_data += hashing[char]

    bin_data = list(map(int, bin_data))

    S, R = len(bin_data) // 7, len(bin_data) % 7
    ans = []
    for i in range(S):
        sm = 0
        for j in range(7):
            sm += bin_data[i * 7 + j] * (2 ** (6 - j))
        ans.append(sm)

    sm = 0
    i += 1
    for j in range(R):
        sm += bin_data[i * 7 + j] * (2 ** (R - 1 - j))
    ans.append(sm)

    print(f'#{tc}', *ans)