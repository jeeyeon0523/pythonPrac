###################################################
#문제 url : https://www.acmicpc.net/problem/10845
###################################################

import sys;
from queue import Queue

if __name__ == '__main__':
    N = int(input())

    que = Queue();

    for t in range(N):
        line = input().split()

        if line[0] == 'push':
            que.put(line[1])
        elif line[0] == 'pop':
            print(que.get() if que.qsize() > 0 else -1)
        elif line[0] == 'size':
            print(que.qsize())
        elif line[0] == 'empty':
            print(0 if que.qsize() > 0 else 1)
        elif line[0] == 'front':
            print(que.queue[0] if que.qsize() > 0 else -1)
        elif line[0] == 'back':
            print(que.queue[que.qsize()-1] if que.qsize() > 0 else -1)
