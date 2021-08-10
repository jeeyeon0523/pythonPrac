# wire 나혼자 개발한다 #4시저의 암호
def solution(data, n):
    answer = ''
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in range(len(data)):
        ch = data[i]

        if ch.islower():
            for c in lower:
                if c == ch:
                    index = lower.index(c)
            answer = answer + lower[(index + n) % 26]

        elif ch.isupper():
            for C in upper:
                if C == ch:
                    index = upper.index(C)
            answer = answer + upper[(index + n) % 26]

        else:
            answer = answer + ' '

    return answer

if __name__ == '__main__':
    data = "Hello"
    n = 3
    res = solution(data, n)
    print(res)

    data = "caeser"
    n = 4
    res = solution(data, n)
    print(res)

    data = "Caeser Cipher"
    n = 4
    res = solution(data, n)
    print(res)