# 구구단 - 이중 for문을 사용하고 있음
# 변수를 1개 사용해야 함 
temp=0
for i in range(1,10):
    # if i==2: break
    for j in range(1,10):
        if j==5:
            temp=1
            break
            # 여기에서 프로그램을 종료하는 방법          
        print(f"{i}*{j}={i*j}")
    if temp==1: break
        
