class Card: # 4개의 변수: kind, number, width, height
    width=0 # 클래스 변수 
    height=0 # 클래스 변수 
    
    def __init__(self,kind,number):
        self.kind=kind
        self.number=number
        Card.width=100
        Card.height=200

# 52장 카드 생성 
shape=["SPADE","DIAMOND","HEART","CLOVER"]
number=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
card_lsit=[]
for i in range(4):
    for j in range(13): 
        c=Card(shape[i],number[j]) # 객체선언 
        card_lsit.append(c) # 리스트추가 

for i in range(52):
    c=card_lsit[i] # c안에 Card 객체 
    print("카드출력 :",c.kind,c.number)

card_list=[]
for i in range(13):
    card_list.append(Card("spade",i+1))
# card_lsit.append(Card("spade","A"))
# card_lsit.append(Card("spade","2"))
# card_lsit.append(Card("spade","3"))
# card_lsit.append(Card("spade","4"))
# card_lsit.append(Card("spade","5"))
# card_lsit.append(Card("spade","6"))
# card_lsit.append(Card("spade","7"))
# card_lsit.append(Card("spade","8"))
# card_lsit.append(Card("spade","9"))
# card_lsit.append(Card("spade","10"))
# card_lsit.append(Card("spade","J"))
# card_lsit.append(Card("spade","Q"))   
# card_lsit.append(Card("spade","K"))    
print(len(card_list))
for i in range(13):
    print("리스트 출력: ",card_list[i].kind,card_list[i].number)
# print("리스트 출력: ",card_lsit[0].kind,card_lsit[0].number)
# print("리스트 출력: ",card_lsit[1].kind,card_lsit[1].number)
# print("리스트 출력: ",card_lsit[2].kind,card_lsit[2].number)
# print("리스트 출력: ",card_lsit[3].kind,card_lsit[3].number)
    
