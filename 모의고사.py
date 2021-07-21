#문제 : https://programmers.co.kr/learn/courses/30/lessons/42840

index = [0, 0, 0]

def getScore(n, x):
    global index
    jjic = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    return 1 if n == jjic[x][index[x]] else 0

def addIndex():
    global index
    index[0] = (index[0] + 1) % 5
    index[1] = (index[1] + 1) % 8
    index[2] = (index[2] + 1) % 10

def solution(answers):
    global index
    answer = []
    score = [0, 0, 0]
    for i in answers:
        for j in range(3):
            score[j] += getScore(i, j)
        addIndex()

    m = max(score[0], score[1], score[2])

    for i in range(3):
        if score[i] >= m:
            answer.append(i+1)

    answer.sort()

    return answer

if __name__ == '__main__':
    #answers = [1,2,3,4,5]
    answers = [1,3,2,4,2]
    print(solution(answers))