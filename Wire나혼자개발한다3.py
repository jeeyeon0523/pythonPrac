# wire 나혼자 개발한다 #3콜라츠 추측
def solution(num):
    answer = 0
    #print()
    while(1):
        #print("num : ", num)

        if num == 1:
            answer = answer + 1
            break

        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1

        answer = answer + 1


        if answer > 500:
            answer = -1
            break

    return answer

if __name__ == '__main__':
    num = 1
    res = solution(num)
    print(res)

    num = 2
    res = solution(num)
    print(res)

    num = 7
    res = solution(num)
    print(res)

    num = 6
    res = solution(num)
    print(res)

    num = 16
    res = solution(num)
    print(res)

    num = 626331
    res = solution(num)
    print(res)

    num = 3630999
    res = solution(num)
    print(res)