customer = "손님"
index = 5

while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer,index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분 되었습니다.")

# while: 조건식에 만족할 때까지 계속 반복