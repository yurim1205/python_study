python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","React"))

index = python.index("n")
print(index)

# 먼저 찾은 위치의 다음 위치를 찾음
index = python.index("n", index+1)
print(index)

# 찾는 문자가 없으면
# find -> -1 반환
# index -> 오류 처리
print(python.find("Java"))
print(python.index("Java"))

print(python.count("n"))