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