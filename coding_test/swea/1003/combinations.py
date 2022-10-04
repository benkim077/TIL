def combination(arr, r):
    arr = sorted(arr)

    def gernerate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            gernerate(chosen)
            chosen.pop()

    gernerate([])


data = ['a', 'b', 'c', 'd', 'e']
r = 3

combination(data, r)