def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 165
gender = "여자"
weigjt = round(std_weight(height/100, gender),2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weigjt))