cabinet = {3: "이유림", 5: "유림"}
print(cabinet[3])
print(cabinet[5])

print(3 in cabinet) # True
print(100 in cabinet) # False

# 키 선언을 정수가 아닌 문자열도 가능
cabinet = {"A-3":"이유림","B-5":"유림"}
print(cabinet["A-3"])

# 변경, 추가 가능
print(cabinet)
cabinet["A-3"]="유유"
cabinet["C-20"]="이"
print(cabinet)

# 키 삭제
del cabinet["A-3"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

cabinet.clear()
print(cabinet)