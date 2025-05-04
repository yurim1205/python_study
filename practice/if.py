weather = input("오늘 날씨는 어때요? ")
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("좋은 하루 되세요")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("날씨가 더우니 나가지 마세요")
elif 10 <= temp and temp <30:
    print("날씨가 좋아요")
elif 0 <= temp <10:
    print("외투를 챙기세요")
else: 
    print("너무 추우니 나가지 마세요")