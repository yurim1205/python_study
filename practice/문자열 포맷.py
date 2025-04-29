# 방법 1
print("나는 %d살이다" %26)
print("나는 %s을 좋아한다" %"파이썬")
print("Apple은 %c로 시작해요" %"A")

# %s -> 한 글자, 정수 등 상관없이 잘 출력함

print("%s색과 %s색을 좋아해요" %("초록","핑크"))

# 방법 2
print("나는 {}살 입니다" .format(20))
print("{}색과 {}색을 좋아해요" .format("초록","핑크"))
print("{1}색과 {0}색을 좋아해요" .format("초록","핑크"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아한다" .format(age=20,color="초록"))

# 방법 4
age = 26
color = "초록"
print(f"나는 {age}살이며, {color}색을 좋아한다")