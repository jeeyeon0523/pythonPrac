###################################################
# 문제 url : https://www.acmicpc.net/problem/11660
###################################################
import sys

if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    mat = []
    sumMap = [[0 for _ in range(N+1)] for _ in range(N+1)]
    mat.append([0 for _ in range(N+1)])
    for i in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        temp.insert(0, 0)
        mat.append(temp)

    for i in range(1, N+1):
        for j in range(1, N+1):
            sumMap[i][j] = sumMap[i-1][j] + sumMap[i][j-1] + mat[i][j] - sumMap[i-1][j-1]

    for i in range(M):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

        print(sumMap[x2][y2] - sumMap[x1-1][y2] - sumMap[x2][y1-1] + sumMap[x1-1][y1-1])

