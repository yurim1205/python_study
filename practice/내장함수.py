# input : 사용자에게 입력을 받는 함수
language = input("좋아하는 언어는? ")
print("{0}은 편리한 언어입니다!".format(language))

# dir: 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수,함수를 가지고 있는지 표시해줌
import random
print(dir())
import pickle
print(dir())

print(dir(random))

list = [1,2,3]
print(dir(list))