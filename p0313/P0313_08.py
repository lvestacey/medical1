from datetime import datetime
# print(datetime.now(timezone('Asia/Seoul')))

now=datetime.now()
print("시간을 포맷에 맞춰 출력하기")
# Y년을 의미, m:월 d: 일 H:시 M:분 S초 
output_a=now.strftime("%y년 %m월 %d일 %H시 %M분 %S초")
output_b=now.strftime("%y-%m월-%d일 %H시:%M분:%S초")
output_c=now.strftime("%y/%m월/%d일 %H시:%M분:%S초")
output_d=now.strftime("%y/%m월/%d일")

print(output_a)
print(output_b)
print(output_c)
print(output_d)

# print(now.year+1,"년")
# print(now.month,"월")
# print(now.day,"일")
# print(now.hour,"시")
# print(now.minutes,"분")
# print(now.second,"초")
# print()

