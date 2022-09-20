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

pwd_dict = {
    '001101':0,
    '010011':1,
    '111011':2,
    '110001':3,
    '100011':4,
    '110111':5,
    '001011':6,
    '111101':7,
    '011001':8,
    '101111':9,
}

T = int(input())
for tc in range(1, T + 1):
    data = input()

    bin_data = ''
    for char in data:
        bin_data = bin_data + hashing[char]

    print(f'#{tc}', end=' ')
    i = 0
    while i < len(bin_data):
        if i + 6 < len(bin_data):
            pwd = pwd_dict.get(bin_data[i : i + 6])
            if pwd == None:
                i += 1
            else:
                print(pwd, end=' ')
                i += 6
        else:
            break
    print()