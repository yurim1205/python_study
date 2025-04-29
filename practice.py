# 숫자 자료형 
print(5)
print(-10)
print(3.14)

# 문자열 자료형
print('풍선') 
print("나비")
print("ㅋ"*9)

# boolean 자료형 (참 / 거짓)
print(5<10)
print(False)
print(True)
print(not True)
print(not False)
print(not (5>10))

# 변수
animal = "토끼"
name = "토실"
age = 2
hobby = "먹기"
is_adult = age >= 1

print("우리집  " + animal + "의 이름은 " +name+ "이에요")
print(name + "이는 " + str(age) + "살이며, " +hobby+"를 아주 좋아해요")
print(name+"이는 어른일까요? " +str(is_adult))

# 연산자
print(1+1)
print(5*2)
print(2**3)
print(5%3)
print(5//3) # 몫
print(3==3)
print(4==2)
print(1!=3)
print(not(1!=3))

print((3>0) and (3<5))
print((3>0) & (3<5))

print((3>0) or (3>5))
print((3>0) | (3>5))

print(5>4>3) # true
print(5>4>7) # false

# 수식
print(2+3*4)
print((2+3)*4)

num = 2 + 3 * 4
print(num)
num += 2
print(num)
num *= 2
print(num)
num /= 2
print(num)
num -= 2
print(num)

# 숫자 처리 함수
print(abs(-5))
print(pow(4,2 )) # 4^2 = 16 (4의 제곱)
print(max(5,12))
print(min(5,12))
print(round(3.14)) # 반올림 함수임

from math import *
print(floor(4.99)) # 내림-4
print(ceil(3.14)) # 올림-4
print(sqrt(16)) # 제곱근-4

# 랜덤 함수(난수)
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(randint(1,25)) # 1~25 이하의 임의의 값 생성