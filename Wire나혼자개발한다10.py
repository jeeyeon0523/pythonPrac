# wire 나혼자 개발한다 #10지그재그 행렬

class TwoArray:
    size = 0
    start = 0
    step = 0

    def __init__(self, size, start, step):
        self.size = size
        self.start = start
        self.step = step

    def createTwoAray(self):
        array = [[0 for _ in range(size)] for _ in range(size)]
        num = start

        for i in range(size):
            if i%2 == 0:
                for j in range(len(array)):
                    array[i][j] = num
                    num = num + step
            else:
                for j in range(len(array)-1, -1, -1):
                    array[i][j] = num
                    num = num + step

        return array



    def sumTwoArray(self, ary):
        sum = 0

        for i in range(len(ary)):
            sum += ary[i][i]

        return sum

def solution(size, start, step):
    answer = 0
    ta = TwoArray(size, start, step)
    res = ta.createTwoAray()
    # print(res)
    answer = ta.sumTwoArray(res)
    return  answer

if __name__ == '__main__':
    size = 2
    start = 1
    step = 1
    res = solution(size, start, step)
    print(res)

    size = 3
    start = -5
    step = -1
    res = solution(size, start, step)
    print(res)

    size = 4
    start = 1
    step = 2
    res = solution(size, start, step)
    print(res)
