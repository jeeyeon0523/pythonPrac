# wire 나혼자 개발한다 #5숫자 다양성 측정
def solution(data):
    answer = 0
    data = str(data)
    visit = [0 for _ in range(10)]

    for i in range(len(data)):
        ch = int(data[i])
        visit[ch] = visit[ch] + 1

    for i in visit:
        if i > 0:
            answer = answer + 1

    return answer

if __name__ == '__main__':
    data = 1
    res = solution(data)
    print(res)

    data = 1000000000
    res = solution(data)
    print(res)

    data = 34915
    res = solution(data)
    print(res)

    data = 5755647
    res = solution(data)
    print(res)

    data = 740832
    res = solution(data)
    print(res)