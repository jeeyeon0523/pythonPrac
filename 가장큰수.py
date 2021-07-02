
# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
# compare override 참고 : https://velog.io/@sparkbosing/python-%EB%82%B4-%EB%A7%88%EC%9D%8C%EB%8C%80%EB%A1%9C-%EC%A0%95%EB%A0%ACsort

from functools import cmp_to_key

def compare(x,y):
    if(str(x) + str(y) > str(y) + str(x)):
        return -1
    else:
        return 1


def solution(numbers):
    answer = ''
    numbers = sorted(numbers, key=cmp_to_key(compare))
    for i in numbers:
        answer = answer + str(i)

    if int(answer) == 0:
        answer = '0'
    return answer

if __name__ == '__main__':
    #numbers = [3, 30, 34, 4, 40, 42, 421, 423, 45]
    #numbers = [0,0,0]
    numbers = [3, 30, 34, 5, 9]
    print(solution(numbers))


