# 클래스(사용자정의변수) # 콜백-> 함수안에 변수 넣을 수 있다. 
# 클래스 : 사용자정의 변수- 함수도 포함 
# 클래스 첫글자 대문자사용 
# 클래스: 설계도 
class Car: 
    color="white"
    door=5
    length=4710 
    width=1800
    displace=1600
    speed=0
    

# def func(): 
#     pass
# c1=Car() # 클래스 객체선언 : Car클래스에 있는 모든 변수를 사용함 
# print(c1.length)
# c2=Car() 
# c3=Car()

def upSpeed(self,sp):
    self.speed+=sp
    
def downSpeed(self,sp):
    self.speed-=sp
    
#  객체선언을 할때마다 제품(Car)이 한개씩 생산     

c1=Car() # 객체선언 
print("색상 :",c1.color)
c1.color="red"
print("변경후 생산 :",c1.cl)
c2=Car()
print("색상 :",c2.color)
    