print('-'*35)
print('\t[학생성적프로그램]')
print('-'*35)
print('1.학생성적입력')
print('2.학생성적수정')
print('3.학생성적삭제')
print('4.학생성적전체출력')
print('5.학생검색출력')
print('6.등수처리')
print('0.프로그램종료')
print('-'*35)


# 홍길동 100 100 100
# 유관순 90  100 90 
# 두 정보를 입력을 받아서 출력해보세요

name = input("이름을 입력하세요:  ")
if name == '홍길동':
    print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print('{}\t{}\t{} \t{} \t{}  \t{}  \t{}  \t{}'.format(1,'홍길동',100,100,100,300,100.0,1))
elif name == '유관순':
    print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print('{}\t{}\t{} \t{} \t{}  \t{}  \t{}  \t{}'.format(1,'유관순',90,100,90,(90+100+90),(90+100+90)/3,1))
else:
    print('조회된 성적이 없습니다. 다시 한 번 이름을 확인해주세요.')