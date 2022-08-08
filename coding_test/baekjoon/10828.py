N = int(input())

stack = []
idx = -1

for _ in range(N):
    cmd = input()
    if cmd[0:4] == 'push':
        idx += 1
        stack[idx] = int(cmd[5:])
    elif cmd == 'pop':
        if idx < 0:
            print(-1)
        else:
            print(stack[idx])
            stack = stack[0:idx]
            idx -= 1
    elif cmd == 'size':
        print(idx+1)
    elif cmd == 'empty':
        if idx < 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if idx < 0:
            print(-1)
        else:
            print(stack[idx])
    else:
        pass
