###################################################
#문제 url : https://www.acmicpc.net/problem/10828
###################################################
import sys;

if __name__ == '__main__':
    N = int(input())
    stack = []
    for t in range(N):
        temp = input()
        cmd = temp.split()[0]

        if cmd == 'push':
            stack.append(temp.split()[1])

        elif cmd == 'top':
            print(stack[-1] if len(stack) > 0 else -1)

        elif cmd == 'size':
            print(len(stack))

        elif cmd == 'empty':
            print(0 if len(stack) > 0 else 1)

        elif cmd == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)

