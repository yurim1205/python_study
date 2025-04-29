subway = [10,20,30]
print(subway)

subway=["가","나","다"]
print(subway)

print(subway.index("다"))

# 맨 뒤에 요소 추가
subway.append("라")
print(subway)

# 인덱스 1 위치에 요소 추가
subway.insert(1,"마")
print(subway)

# 맨 뒤 요소 삭제
print(subway.pop())
print(subway)

subway.append("나")
print(subway)
print(subway.count("나"))

# 리스트 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 리스트 뒤집기
num_list.reverse()
print(num_list)

# 리스트 값 삭제
num_list.clear()
print(num_list)

# 리스트는 다양한 자료형과 함께 사용 가능
mix_list=["이유림",26,True]
print(mix_list)

# 리스트 확장
num_list = [5,2,4,3,1]
mix_list=["이유림",26,True]

num_list.extend(mix_list)
print(num_list)