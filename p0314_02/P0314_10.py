# k001.csv 파일에서 전국 인원수를 출력하시오.
# 적용년월,시도코드,시도명,사용건수,인원수,사용금액
f = open("k001.csv","r",encoding="utf8")

# 파일읽기
cnt = 0
sum = 0
while True:
    content = f.readline()
    if cnt == 0:
        cnt += 1
        continue
    if content == "": break
    c_list = content.split(",")
    c_list[4] = int(c_list[4])
    sum += c_list[4]
    print(c_list,len(c_list))
    # print(content,end="")
print("인원수 : ",sum)
# 파일닫기
f.close()