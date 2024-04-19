import requests
from bs4 import BeautifulSoup

url="https://www.coupang.com/np/search?q=%EB%A0%88%EB%85%B8%EB%B2%84%202022%20%EC%95%84%EC%9D%B4%EB%94%94%EC%96%B4%ED%8C%A8%EB%93%9C%20%EC%8A%AC%EB%A6%BC%201&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res=requests.get(url,headers=headers)
res.raise_for_status


soup=BeautifulSoup(res.text,"lxml")

#with open("coupang.html","w",encoding="utf8") as f:
#    f.write(soup.prettify())
    
#print("완료")

ul_search=soup.find("ul",{"class":"search-product-list"})

# 모든 상품 검색 
lis=ul_search.find_all("li")
#print("리스트 개수 :",len(lis))

for i,li in enumerate(lis[0:20]):
    print("[",i+1,"번째 상품]")
    # 광고상품 제외 
    if "search-product__ad-badge" in li['class']:
        continue
    
    # 평점이 5.0 이상 - 실수형으로 변경: 문자와 숫자 비교 에러 
    if float(li.find("em",{"class":"rating"}).text) <5.0:
        continue
    # 평가인원수가 200명 이상 - 정수형으로 변경
    if int (li.find("span",{"class":"rating-total-count"}).text[1:-1]) <200:
        continue
    
    print("li class:",li["class"])
    # 왼쪽, 오른쪽 공백제거 
    print("상품이름 :",li.find("div",{"class":"name"}).text.strip())
    print("가격 :",li.find("strong",{"class":"price-value"}).text)
    print("평점 :",li.find("em",{"class":"rating"}).text)
    # 평가인원수 200명 이상 출력 
    
    print("평가인원수 :",li.find("span",{"class":"rating-total-count"}).text[1:-1])
    print("-"*30)
    