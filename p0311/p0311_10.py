# 함수선언 : def 이름() 
# 함수호출 : 이름()
# 함수선언 매개변수 개수는 맟춰야 함: def 이름 (매개변수) -> 이름(매개변수)
# 리턴의 결과값을 받지 않아도 되지만, 리턴의 개수는 맞춰야 함. 
# 함수내의 변수는 지역변수여서, 함수가 종료되면 사라짐. 
# 함수내의 변경된 변수값을 전역변수에 반영하고 싶은면 return으로 돌려주어야 함
# 함수 내 global 이라고 하면, 전역변수에 선언되어 있는 변수주소를 가져와서 retunr을 사용하지 않아도 됨
# 매개변수로 리스트, 딕셔너리를 사용경우 return할 필요가 없음 

def func1(a,a_list):
    a=100
    a_list[0]=100 # 지역변수 a_list=[100]
    return a

a=10
a_list=[1,2,3] # 전역변수 
# 함수호출 
a=func1(a,a_list) # 2개 이상의 데이터를 저장하는 변수- 주소값을 저장함. 

# 데이터 출력 
print(a)
print(a,a_list)


    





















# def func1():
#     global a # 전역변수를 가져옴 
#     a=100
#     print("func1 a=",a)
#     # 지역변수 값을 전역변수에 적용 
#     # 코드를 추가하시오. 
#     return a 
# # 전역변수의 값을 호출 100 
# def func2():
#     print("func2 a=",a+10)
    
# # 전역변수
# a=20

# func1() # 100 
# func2()
# print("결과값 :",a)

    




# def cal(v1,sum): # 지역변수 
#     sum=sum+500 # 지역변수
#     v1=200 # 지역변수 
#     return v1,sum

# sum=10 # 전역변수 
# v1=100 # 전역변수 
# cal(v1,sum)
# print(v1) 
# print(sum)
