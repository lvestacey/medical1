class Card:
    kind = ""
    number = ""
    def __init__(self,kind,number):
            self.kind=kind
            self.number=number
    
# c1에 숫자를 5로 변경하시오.
# c1을 출력하시오.
# c2 "heart","A"
# 모양을 diamond 변경후 출력하시오.    


# 클래스를 이용해서 52장의 카드 생성 
c_list=[]
kind=["SPADE","DIAMOND","HEART","CLOVER"]
number=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
for i in range(4):
    for j in range(13):
        c=Card(kind[i],number[j]) # 리스트를 생성해서 리스트에 추가 
        c_list.append(c)
for i in range(52):
    print("카드출력: ",c_list[i].kind,c_list[i].number)


# 리스트를 이용해서 52장의 카드 생성 
# c_list=[]
# kind=["SPADE","DIAMOND","HEART","CLOVER"]
# number=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
# for i in range(4):
#     for j in range(13):
#         c=[kind[i],number[j]] # 리스트를 생성해서 리스트에 추가 
#         c_list.append(c)

# for i in range(4):
#     for j in range(13):
#         print("카드출력:",kind[i],number[j])

# c1 = Card("spade",1)
# c1.number=5
# print(c1.kind,c1.number)

# c2=Card("heart","A")
# c2.kind="diamond"
# print(c2.kind,c2.number)

