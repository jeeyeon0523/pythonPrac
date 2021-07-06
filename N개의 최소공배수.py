#문제 : https://programmers.co.kr/learn/courses/30/lessons/12953
#유클리드 호제법 참고 : https://coding-factory.tistory.com/599

def getGcm(a, b):
    if a % b == 0:
        return b

    gcm = getGcm(b, a % b)

    return gcm;

def solution(arr):
    lcm = arr[0]
    for n in arr:
        gcm = getGcm(lcm, n)
        lcm = (lcm * n) / gcm;

    return int(lcm)


if __name__ == '__main__':
    arr = [1,2,3]
    #arr = [2,6,8,14]
    print(solution(arr))