import sys

def dfs(n, sum, k, H):
    if sum > n:
        return

    if n == sum :
        H[k] = 1

    for i in range(1,4):
        dfs(n, sum + i, k+str(i),H)

if __name__ == "__main__":
    T = int(input())
    H = {}
    for t in range(T):
        n = int(input())
        H.clear()
        dfs(n, 0 ,'',H)
        print(len(H.items()))
