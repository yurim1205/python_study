# score_file = open("score.txt","w",encoding="utf8")
# print("수학: 50",file=score_file)
# print("영어: 80",file=score_file)
# score_file.close()

# a: 파일에 이어쓰기
# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학: 90")
# score_file.write("\n코딩: 90")
# score_file.close()

# 파일 내용 읽어오기
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# 한 줄씩 읽어오기
# score_file = open("score.txt","r",encoding="utf8")
#    # 한 줄 읽고 커서가 다음 줄로 이동함
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 파일 내용 줄 수를 모를 때 while 사용 예제
# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() # 모든 내용을 list형태로 저장함
for line in lines:
    print(line, end="")

score_file.close()