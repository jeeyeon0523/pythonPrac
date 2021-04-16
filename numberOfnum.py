###################################################
# 문제 url : https://www.acmicpc.net/problem/2577
###################################################

import sys

if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())

    mul = A*B*C

    arr = [0 for _ in range(10)]
    s_mul = str(mul)

    for i in range(len(s_mul)):
        s = int(s_mul[i])
        arr[s] += 1

    for i in range(10):
        print(arr[i])
