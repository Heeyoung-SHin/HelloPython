#이름 짓기
#파스칼 표기법 :
#       첫 단어를 대문자로 시작하며 이름을 지음
#       Employee, Customer
#       RegisterEmployee

#카멜 표기법 :
#       첫단어를 소문자로 시작하며 이름을 지음
#       registerEmployee

#스네이크 표기법 :
#       소문자와 _ 기호를 이용해서 이름을 지음
#       register_employee, join_member

#헝가리언 표기법
#       자료형을 의미하는 접두사를 이용해서 이름을 지음
#       strName, isMarried, boolMarried

#함수로 재작성하기

#8 자취방 구하기
def compareRoom(width,height,price):
    return(width*height)/price

roomA = compareRoom(2.5,3,27)
roomB = compareRoom(4,2,30)

if(roomA > roomB):
    print('방A가 낫네요')
else:
    print('방B가 낫네요')

#10
def computeProfit():
    c= int(input('불변자본을 입력하세요'))
    v= int(input('가변자본을 입력하세요'))
    s= int(input('잉여가치액을 입력하세요'))

    return (c+v)


print(computeProfit())

#11 환율
def getExchangeRate(country):
    rate=0
    if country=='us':
        rate = 1071
    elif country=='euro':
        rate=1390
    return rate

buyUS = 780 * getExchangeRate('us')
buyEuro = 650*getExchangeRate('euro')

if buyUS > buyEuro:
    print('유료화로 구입하는게 더 싸네요')
else:
    print('달러로 구입하는게 더 싸네요')

#12
def howManyRun(radius):
    pi=3.14
    return radius * pi

studentA = howManyRun(100)
studentB = howManyRun(90)

print('학생A는 학생B보다 %d만큼 더 뛰었다')

#17계산기
def intCalu():
    num1 = int(input('좌변값을 하나 입력하세요'))
    num2 = int(input('우변값을 하나 입력하세요'))
    fmt = "%d + %d = %d \n %d - %d = %d \n"
    fmt += "%d * %d = %d \n %d / %d = %d \n"
    fmt += "%d ** %d = %d"
    print(fmt %(num1, num2, num1 + num2, \
                num1, num2, num1 - num2, \
                num1, num2, num1 * num2, \
                num1, num2, num1 / num2, \
                num1, num2, num1 ** num2))

intCalu()


#18세금계산
def compute():

    salary=int(input('연봉입력하세요.'))
    isMarried = input('결혼했습니까? (Y/N)')
    tax = 0

    if isMarried.upper() == 'N':

        if salary >= 3000:
            tax = salary*0.25

        elif salary < 3000:
            tax = salary * 0.1

        isMarried = "아니오"

    elif isMarried.upper() == 'Y':

        if salary >= 6000:
            tax=salary * 0.25

        elif salary < 6000:
            tax=salary * 0.1

        isMarried="예"

    fmt = "연봉 : %d ,결혼여부 : %s, 세금 : %.1f"
    print(fmt % (salary, isMarried, tax))

compute()

#19 윤년여부
def isLeapYear():

    year = int(input('윤년여부를 알고싶은 년도를 입력'))

    isleap = '윤년이 아닙니다'

    if( (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) :
        isleap = '윤년입니다'

        print('%d 는 %s 입니다' %(year,isleap))

    isLeapYear()


#20 복권발행
import random

def rollretLotto():

    lotto = str(random.randint(100, 999))
    lucky = str(input('복권 숫자 3자리를 입력하세요\n'))
    match = 0
    prize ='꽝 다음 기회에!'

    for i in [0,1,2]:
        for j in [0,1,2]:
            if(lucky[i] == lotto[j]):
                match += 1

    if match == 3:
        prize = '모두 일치! 상금 1백만원!'
    if match == 2:
        prize = '2개 일치! 상금 1만원!'
    if match == 1:
        prize = '1개 일치! 상금 1천원!'

    print(prize)
    print('로또번호는?', lotto)

rollretLotto()