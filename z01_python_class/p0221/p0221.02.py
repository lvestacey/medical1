print("Hello world")
print("Hello! " *3)
print("혼자 공부하다 모르면 동영상 강의를 참고하세요")

# ctrl+F5 RUN과 같은 기능
# 참/거짓
print(5>10) #False
print(5<10) # True
print(True)
print(False)
# print(true)
print(not True) # False
print(not (5>10)) # True
# "" '' 안에 있는 것은 문자열이다.
print(0*10) # 0
print("0"*10)

print(100) # 숫자
print("100") # 문자

print("100+100") # 100+100 출력
print(100+100) # 200 출력

print("숫자는 %d"%300) #%d는 정수(소숫점 표시 안하고 싶을 때) %000의 값을 입력하면 %d자리에 000의 값을 출력해준다
print("%d" %200)
print("%d+%d=%d"%(2,3,2+3)) # %d의 개수에 따라 그만큼 수를 입력해줘야 하나씩 할당이 가능하다.

# print("%d"%(100,200)) #서로 짝이 맞지 않으면 오류를 발생시킨다.
print("%d%d                  ,,sdjk   "%(20,10)) # %d 위치 그대로 숫자 출력됨 >>>2010                  ,,sdjk

print("%d*%d=%d"%(2,1,2))
print("%d*%d=%d"%(1,2,1*2))

# 깔끔한 출력
print("%d"%123)
print("%7d"%123) # 7자리 숫자를 보여줌. 빈공백으로 채움
print("%05d"%123) # 5자리 숫자를 보여줌. 빈공백은 0으로 채워짐

# %d :  정수
# %f : 실수
print("%d"%123.45)
print("%f"%123.45)
# 소숫점을 포함해서 총 7자리 출력
# 빈 공백으로 채움. 소숫점 이하는 1자리까지 표현 # alt+key 누르면 내가 원하는 줄로 이동 가능
print("%7.1f"%123.45) 
# 소숫점이하는 3자리로 표현하고 빈공백은 0으로 채움, 총 7자리
print("%07.3f"%123.45)

print("%f"%12.3456)
print("%.2f"%12.3456)


# 문자열은 %s를 사용
print("안녕하세요")
print("%s"%"반갑습니다")

# 문자는 %c
print("%c"%'a')
print("%s"%"a")

# Quize ~~
# 1) 소수점 둘째자리까지 출력하시오 (소숫점 표시는 실수이기 때문에 %f를 사용한다.)
print("%.2f"%758.12345678)

# 2) 총 10자리, 빈칸은 0으로 채워 소수점 2자리까지 출력하시오
print("%010.2f"%25.05)

# 3) 변수 150.05를 정수, 실수, 문자열로 출력하시오
print("%d"%150.15)
print("%f"%150.15)
print("%s"%"150.15")

# *을 10개 출력하시오 # 문자는 %c 사용
print("%c"%'*'*10) # 쉽게는 print("*"*10)