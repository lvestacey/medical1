from urllib import request

# urlopen()함수 
target=request.urlopen("https://www.google.com")
output=target.read()

print(output)


# BeautifulSoup
# 패키지 