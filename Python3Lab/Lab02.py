salary=int(input('연봉입력하세요.'))
ismarried = input('결혼했습니까? (Y/N)')
tax = 0
if ismarried == 'Y':

    if salary >= 3000:
        tax = salary*0.25
        print(tax)
    elif salary < 3000:
        tax = salary * 0.1
        print(tax)

elif ismarried == 'N':

    if salary >= 6000:
        tax=salary * 0.25
        print(tax)
    elif salary < 6000:
        tax=salary * 0.1
        print(tax)


#19 윤년 계산
year = int(input('윤년여부를 알고싶은 년도를 입력'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('%d 는 윤년입니다' %year)
else:
    print('%d 는 윤년이 아닙니다.' %year)

# 1~100 사이 짝수

total = 0

for i in range(1,101):
    total += 1
    if (i % 2 ==0):
        print(i)

# 1~101 사이 홀수
for i in range(1,101):
    if (i % 2 ==1):
        print(i)

#십구단7단
for i in range(1, 20):
    print('7 x %d = %d' % \
          (i, 7 * i) )

# 십구단
num = int(input('출력 할 단을 입력하세요'))

for i in range(1,20):
    print('%d x %d = %d' % \
             (num, i, num * i) )

for i in range(1,101,2):
    print(i)

for i in range(2,101,2):
    print(i)

#특정코드 단순 반복 : _는 변수를 사용X 다는 의미
n=10
for _ in range(n):
    print('안녕하세요')

# 범위 지정의 또 다른 방법 : 리스트 사용
for i in [1,2,3,4,5]:
    print(i)


#i =1
#while (i<=100):
#   if(i%2 ==0):
#   print(i)
#   i += 1


#while True:
#    print('반복 중단시 ctrl+c')


#msg = '아무 메세지나 입력하세요 \n \
#중지 하시려면 "그만" 이라고 입력하세요'
#while msg != '그만':
    #    print(msg)
#    msg=input()

#문자 추출 : 문자 변수[인덱스]
#str = '123456'
#str[2]

print('#20 복권 발행')
import random

lotto = str(random.randint(100, 999))
lucky = str(input('복권 숫자 3자리를 입력하세요\n'))
match = 0;

if lotto[0] == lucky[0] or lotto[0] == lucky[1] or lotto[0] == lucky[2]:
    match += 1
if lotto[1] == lucky[0] or lotto[1] == lucky[1] or lotto[1] == lucky[2]:
    match += 1
if lotto[2] == lucky[0] or lotto[2] == lucky[1] or lotto[2] == lucky[2]:
    match += 1

msg = '꽝이군요! 다음 기회에!'
if match == 3:
    msg = '모두 일치! 상금 1백만원!'
if match == 2:
    msg = '2개 일치! 상금 1만원!'
if match == 1:
    msg = '1개 일치! 상금 1천원!'

print(msg)
print('로또번호는?', lotto)

#21 구구단
#숫자만 입력받기
#문자 - 아스키코드 값 ord()
#아시크코드 - 문자 chr()

dan = input('출력할 단을 입력하세요')
if ord(dan[0]) >= ord('0') \
        and ord(dan[0]) <= ord('9'):
    print('구구단 출력')
else:
    print('입력 오류 - 숫자만 입력하세요!')

#22 소문자를 대문자로 변환
#숫자나 대문자 입력시 오류메세지 출력

lower = input('소문자를 입력하세요')
if ord(lower[0]) >=ord('a') and \
    ord(lower[0])<=ord('z'):
    print(lower.upper())
else:
    print('소문자만 입력가능!!')
