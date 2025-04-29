# 중복 안 됨, 순서 없음
my_set={1,2,3,3,3}
print(my_set)

java = {"이","유","림"}
python = set(["이","가"])

# 교집합
print(java&python)
print(java.intersection(python))

# 합집합
print(java|python)
print(java.union(python))

# 차집합
print(java-python)
print(java.difference(python))

python.add("나")
print(python)

java.remove("이")
print(java)