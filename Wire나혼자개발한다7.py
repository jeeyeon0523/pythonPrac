# wire 나혼자 개발한다 #7범칙금

def calc_penalty(limit, car_speed):
    penalty = 0
    #print('11111',limit*1.1)

    if int(limit * 1.1) <= car_speed < int(limit * 1.2):
        penalty = 3
    elif int(limit * 1.2) <= car_speed < int(limit * 1.3):
        penalty = 5
    elif int(limit * 1.3) <= car_speed:
        penalty = 7

    #print(limit, car_speed, penalty)
    return penalty

def solution(speed, cars):
    answer = 0

    for car in cars:
        answer += calc_penalty(speed, car)

    return answer

if __name__ == '__main__':
    speed = 100
    cars = [110, 98, 125, 148, 120, 112, 89]
    ret = solution(speed, cars)
    print(ret)

    speed = 110
    cars = [100, 110, 95, 130, 132, 120, 120, 90, 88]
    ret = solution(speed, cars)
    print(ret)