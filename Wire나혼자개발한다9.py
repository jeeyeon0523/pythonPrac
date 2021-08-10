# wire 나혼자 개발한다 #9책주문

class Book:
    title = ''
    price = 0

    def __init__(self, title, price):
        self.title = title
        self.price = price

def buyBook(title,price):
    booklist = []
    for i in range(len(title)):
        booklist.append(Book(title[i], price[i]))

    return booklist

def calcPrice(st):
    sum = 0
    for book in st:
        sum += book.price

    return sum


def solution(title, price):
    answer = 0
    booklist = buyBook(title, price)
    answer = calcPrice(booklist)

    return answer

if __name__ == '__main__':
    title = ["어린왕자", "현대미술", "사피엔스", "철학파스타"]
    price = [1000, 2000, 1500, 2100]
    totalprice = solution(title, price)
    print(totalprice)

    title = ["시골의사", "그리스인 조르바", "유토피아", "무정", "인간 실격", "데미안"]
    price = [12000, 2200, 10500, 21000, 11000, 31000]
    totalprice = solution(title, price)
    print(totalprice)