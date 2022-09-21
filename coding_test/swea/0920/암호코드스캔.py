dct1 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
dct3 = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}

T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    old_st = []
    ans = []
    for st in arr:
        # 이전 값과 다르고,  모두 0이 아니면(1이 하나라도 있으면)
        if st != old_st and st.count('0') != len(st):
            old_st = st  # 이전 문자열과 바뀌면 처리
            # [1] 16진수 -> 2진수(str)
            bst = ''
            for ch in st:
                bst += dct1[ch]

            # [2] 0,1개수 저장 cnts
            old = 0
            cnts = []
            for i in range(len(bst)):
                if bst[old] != bst[i]:
                    cnts.append(i - old)
                    old = i
            # print(cnts)

            # [3] 가장작은 width을 기준을 나눗셈(단위두께)
            pwd = []
            for i in range(1, len(cnts), 4):
                mn = min(cnts[i:i + 3])
                key = str(cnts[i] // mn) + str(cnts[i + 1] // mn) + str(cnts[i + 2] // mn)
                pwd.append(dct3[key])

            # [4] 8개씩 숫자 중복제거해서, 리스트에 저장
            for i in range(0, len(pwd), 8):
                if pwd[i:i + 8] not in ans:
                    ans.append(pwd[i:i + 8])

    sol = 0
    for code in ans:
        even = code[0] + code[2] + code[4] + code[6]
        odd = code[1] + code[3] + code[5] + code[7]
        if (even * 3 + odd) % 10 == 0:
            sol += even + odd

    print(f'#{test_case} {sol}')