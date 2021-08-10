# wire 나혼자 개발한다 #8소수찾기
import math

def checkPrime(data):

    if data == 1:
        return False

    for i in range(2, int(math.sqrt(data))):
        if data % i == 0:
            return False

    return True

def solution(data):
    answer = []

    for d in data:
        if checkPrime(d):
            answer.append(d)

    if len(answer) <= 0:
        answer.append(-1)
    return answer

if __name__ == '__main__':
    data = [22, 1, 51, 31, 52, 111]
    result = solution(data)
    print(result)

    data = [13, 71, 17, 55, 23, 101, 36, 27, 44]
    result = solution(data)
    print(result)

    data = [12, 22, 10, 56, 36, 27]
    result = solution(data)
    print(result)