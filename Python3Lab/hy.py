import random

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


#19 윤년여부
def isLeapYear():

    year = int(input('윤년여부를 알고싶은 년도를 입력'))

    isleap = '윤년이 아닙니다'

    if( (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) :
        isleap = '윤년입니다'

        print('%d 는 %s 입니다' %(year,isleap))



#20 로또
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

#성적 데이터 클래스

class SungJukVO:
    def __init__(self,name,kor,eng,mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        sj = ('hy', 99, 98, 97)

#성적 처리용 클래스
class SungJukService:
    def getTotal(self,sj):
        tot = sj.kor + sj.eng + sj.mat
        return tot

    def getAverage(self,sj):
        avg = self.getTotal(sj)/3
        return avg

    def getGrade(self,sj):
        grdlist='가가가가가미양우수수'
        var = int(self.getAverage(sj)/10)
        grd = grdlist[var]
        return grd