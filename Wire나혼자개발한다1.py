# wire 나혼자 개발한다 #1기분 좋은 날
def solution(temperature, A, B):
    cnt = 0
    a = temperature[A - 1]
    b = temperature[B - 1]
    for t in range(A - 1 + 1, B - 1):
        if temperature[t] > a and temperature[t] > b:
            cnt = cnt + 1

    return cnt


if __name__ == '__main__':
    temperature = [3, 2, 1, 5, 4, 3, 3, 2]
    A = 1
    B = 6
    ret = solution(temperature, A, B)
    print("solution 함수의 반환 값은", ret, "입니다.")

    temperature = [-1, 0, -3, -1, -2, 0, 2, 4, 2, -1, 0, 3]
    A = 3
    B = 9
    ret = solution(temperature, A, B)
    print("solution 함수의 반환 값은", ret, "입니다.")

    temperature = [11, 10, 13, 8, 11, 10, 12, 14, 12, 11, 9, 12, 12]
    A = 2
    B = 8
    ret = solution(temperature, A, B)
    print("solution 함수의 반환 값은", ret, "입니다.")