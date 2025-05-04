# 출석번호 앞에 100을 붙이기
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["이유림","유림","림"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["kiyong"]
students = [i.upper() for i in students]
print(students)