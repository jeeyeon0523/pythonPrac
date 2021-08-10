# wire 나혼자 개발한다 #6투표결과

def solution(n, votes):
    answer = -1

    voted = [0 for _ in range(n+1)]

    for i in votes:
        voted[i] = voted[i] + 1

    for i in range(len(voted)):
        if voted[i] > int(len(votes) / 2):
            answer = i

    return answer

if __name__ == '__main__':
    n = 3
    votes = [1, 2, 1, 3, 1, 2, 1]
    ret = solution(n, votes)
    print(ret)

    n = 2
    votes = [2, 1, 2, 1, 2, 2, 1]
    ret = solution(n, votes)
    print(ret)

    n = 3
    votes = [2, 3, 2, 1, 1, 2, 3, 3, 1, 2, 1]
    ret = solution(n, votes)
    print(ret)