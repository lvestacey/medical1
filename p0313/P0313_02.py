
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
    
# 현재까지 입력한 숫자와 결과값을 모두 출력을 해보세요.
print("[현재까지 입력한 숫자, 결과값]")

for s in save_list:
    print("{},{} 결과값: {},{},{},{}".format(*s))

