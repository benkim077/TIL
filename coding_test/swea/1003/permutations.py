# a, b, c, d, e 중 3개를 뽑아 나열하는 순열
def permutation (arr, r):
    arr = sorted(arr)
    check = [False for _ in range(len(arr))]

    def gernerate(chosen, check):
        if len(chosen) == r:
            print(chosen)
            return

        for i in range(len(data)):
            if not check[i]:
                check[i] = True
                chosen.append(data[i])
                gernerate(chosen, check)
                check[i] = False
                chosen.pop()

    gernerate([], check)


data = ['a', 'b', 'c', 'd', 'e']
r = 3

permutation(data, r)