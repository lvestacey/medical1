# 함수선어너 def 이름() 정의 
# 함수값은 return
# 함수호출 이름()
# 매개변수: 함수로 데이터전달하는 변수, 매개변수 개수는 항상 같아야 한다. 
# 가변매개변수 선언 "values, 가변매개변수는 일치하지 않아도 된다. 
# 리스트, 딕셔너리는 주소값이 전달이 된다. 

# 퀴즈 1. 
# 함수를 사용하여 두수를 입력받아, 더하기, 빼기, 곱하기 나누기 결과값을 출력하시오. 

def cal(num1,num2):
    r_list=[0]*6
    r_list[0]=num1
    r_list[1]=num1
    r_list[2]=num1+num2
    r_list[3]=num1-num2
    r_list[4]=num1*num2
    r_list[5]=num1/num2
    return r_list
    
    
save_list=[]

while True: 
    num1 = int(input("1번째 숫자를 입력하세요.>> (0.종료)"))
    if num1==0:
        break
    num2 = int(input("2번째 숫자를 입력하세요.>> "))
    print("1+2-3*4./")
    c = input("원하는 사칙연산을 입력하세요.>> ")

    # 함수호출
    r_list=cal(num1,num2)
    save_list.append(r_list)
   
    print("{},{} 결과값 : {}".format(num1,num2,*r_list)) # list일 경우 * list=list[0]