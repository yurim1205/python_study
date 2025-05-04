absentStu = [2,5]
no_book = [7]

for student in range(1,11):
    if student in absentStu:
        continue  # continue를 만나면 밑 문장 실행 x
    elif student in no_book:
        print("{0}은 짝이랑 같이 보렴".format(student))
        break    # 무조건 반복문 탈출
    print("{0}, 책을 읽어봐".format(student))