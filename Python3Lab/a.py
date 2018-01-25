print('***성적 처리 프로그램***')
name = input('이름을 입력하세요')
kor = int(input('국어점수는?'))
eng = int(input('영어점수는?'))
mat = int(input('수학점수는?'))
tot = kor + eng + mat
avg = tot/3
grd = '가'
if avg >= 90:
    grd = '수'
elif avg >= 80:
    grd = '우'
elif avg >= 70:
    grd = '미'
elif avg >= 60:
    grd = '양'
print('총점은:',tot, '평균은:',avg,'학점은:',grd)

print(name,kor,eng,mat,tot,avg,grd)
print('{0}{1}{2}{3}{4}{5:.2f}{6}'.format(name,kor,eng,mat,tot,avg,grd))
print('%s %d %d %d %d %.2f %s'  %(name,kor,eng,mat,tot,avg,grd))