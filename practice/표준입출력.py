# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(4), str(score).rjust(4), sep=":")

# 은행 대기순번표
for num in range(1,11):
    # zfill(3): 3 공간의 크기만큼 채움
    print("대기번호 : "+str(num).zfill(3))

# 입력값을 통해서 값을 받게 되면, 항상 문자열 형태로 저장됨
answer = input("값을 입력하세요: ")
print("입력하신 값은 " + answer + "입니다.")