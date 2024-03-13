import os

# 파일생성
f=open("students.txt","w",encoding="utf-8")
f.write("1,'홍길동',100,99,87,286,95.33,2\n")
f.write("2,'유관순',98,93,87,278,92.67,3")
f.close() # 파일닫기 

# # 1. 파일생성- with 사용하면 f.close() 사용하지 않아도 됨. 
# with open("students.txt","w") as f:
#     f.write("1,'홍길동',100,99,87,286,95.33,2")
#     f.write("2,'유관순',98,93,87,278,92.67,3")

# 파일읽어오기 
t_list=[]
out_f=open("students.txt","r")
while True:
    txt=out_f.readline()   # 1줄씩 읽어오기 
    if txt =="":
        break
    # print(type(txt))
    print(txt,end="")
    t_list.append(txt)
print()
print(t_list)

out_f.close()

# 파일삭제
os.remove("students.txt")

# vscode 한글인코딩설정  
# EUC-KR: 한국규약 
# vscode 터미널 한글깨짐 
# print("현재 폴더내 파일들 표시",os.listdir())

# 폴더가 존재하는 확인 
# if not os.path.exists("hello"):
#     os.mkdir("hello")
# else:
#     os.rmdir("hello")