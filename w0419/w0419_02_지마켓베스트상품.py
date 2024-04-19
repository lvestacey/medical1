import requests
from bs4 import BeautifulSoup

url="https://www.gmarket.co.kr/n/best"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")


best_div=soup.find("div",{"class":"best-list"})

# 1개 bet 상품 출력 
#li01=best_div.find("li")
#print("li01순위 :",li01.p.text)
#print("제목 :",li01.find("a",{"class":"itemname"}).text)
#print("가격 :",li01.find("div",{"class":"s-price"}).strong.span.text)

lis=best_div.find_all("li")
print("베스트 상품 개수 :",len(lis))

for li in lis[0:4]:
   print("li01순위 :",li.p.text)
   print("제목 :",li.find("a",{"class":"itemname"}).text)
   print("가격 :",li.find("div",{"class":"s-price"}).strong.span.text)
