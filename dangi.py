import sys

dX = [-1, 0, 1, 0]
dY = [0, 1, 0, -1]

c = 0

def dfs(x, y, mat, visit):
    visit[x][y] = 1
    global c
    c = c + 1
    for i in range(4):
        nx = x + dX[i]
        ny = y + dY[i]
        if 0 <= nx < n and 0 <= ny < n:
            if mat[nx][ny] != 0 and visit[nx][ny] == 0:
                dfs(nx, ny, mat, visit)



if __name__ == '__main__':
    n = int(input())
    mat = []
    visit = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().strip()))
        mat.append(temp)

    danji = 0
    cntArr = []
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0 and visit[i][j] == 0:
                c = 0
                danji = danji + 1
                dfs(i, j, mat, visit)
                cntArr.append(c)

    cntArr.sort()
    print(danji)
    for i in range(len(cntArr)):
        print(cntArr[i])