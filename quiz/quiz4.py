from random import *

# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
users = range(1,21) # 1부터 20까지 숫자 생성
users = list(users)
print(users)
shuffle(users)
print(users)

winners = sample(users,4)

print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))