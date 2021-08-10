# wire 나혼자 개발한다 #2
def solution(minDan, maxDan):
    answer = 0

    minDan = 1 if minDan <= 0 else minDan
    maxDan = 19 if maxDan > 19 else maxDan

    for x in range(minDan, maxDan + 1):
        for i in range(1, 20):
            if x != i:
                answer = answer + x * i

    return answer

if __name__ == '__main__':
    minDan = 1
    maxDan = 3
    result = solution(minDan, maxDan)
    print(result)

    minDan = 9
    maxDan = 12
    result = solution(minDan, maxDan)
    print(result)

    minDan = -2
    maxDan = 4
    result = solution(minDan, maxDan)
    print(result)