

# input1=int(input("1번째 숫자를 입력하세요>>"))
# input2=int(input("2번째 숫자를 입력하세요>>"))

# 함수의 return을 사용해서 입력된 두수의 사칙연산 결과값을 출력하시오. 
# 20,10
# 결과값: 30,10,200,2
def cal_result(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b

user_input_one = int(input('input num A:'))
user_input_two = int(input('input num B:'))
user_input_op = input('input op:')
print("result is", cal_result(user_input_one,user_input_two,user_input_op))





# for i in range(10):
#     sum=0
#     sum+=i # i는 지역변수 
# for i in range(5):
#     result=1
#     result+=1

# print(sum)
# print(result)

# def plus(v1,v2):
#     v1=v1+100
#     v2=v2+200
#     return v1,v2 # 함수밖에서 사용하려면 return값을 돌려줘야 함 

# # 함수호출 
# v1=1
# v2=2
# plus(v1,v2)


# # 출력 
# print(v1,v2)

