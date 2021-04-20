###################################################
#문제 url : https://programmers.co.kr/learn/courses/30/lessons/43163
###################################################

import sys

ans = 100
def compare(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            if count >= 2 :
                break;

    return True if count == 1 else 0


def dfs(start, target, words, used, cnt):
    global ans
    if target == start:
        ans = min(ans, cnt)
        return

    for i in range(len(words)):
        w = words[i]
        if used[i] == 0 and compare(start, w):
            used[i] = 1
            dfs(w, target, words, used, cnt+1)
            used[i] = 0


def solution(begin, target, words):
    used = [0 for _ in range(len(words))]
    dfs(begin, target, words, used, 0)
    return ans if ans < 100 else 0

# if __name__ == '__main__':
#    begin = "hit"
#    target = "cog"
#    words = ["hot", "dot", "dog", "lot", "log", "cog"]
#
#    solution(begin, target, words)
#    print(ans)

