import random
# 카드 종류 : SPADE, DIAMOND, HEART, CLOVER 4종류
# 카드 숫자 : A,1,2,4,5,6,7,8,9,10,J,Q,K   13장
# 카드 총 수 : 52장

# 카드 종류 : SPADE, DIAMOND, HEART, CLOVER 4종류
# 카드 숫자 : A,1,2,4,5,6,7,8,9,10,J,Q,K   13장
# 카드 총 수 : 52장

def card_create():
    

def card_shuffle(cards):
    


    print("[ 카드 프로그램 ]")
    print("1. 카드생성")
    print("2. 카드섞기")
    print("3. 카드5장 나눠주기")
    print("4. 카드5장 확인하기")
    print("0. 종료")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:
        cards = card_create()
        print("카드 생성 완료")
    elif choice == 2:
        cards = card_shuffle(cards)
        print("카드 섞기 완료")
    elif choice == 3:
        players = card_share(cards)
        print("카드 5장 나눠주기 완료")
    elif choice == 4:
        card_print(players)
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")

