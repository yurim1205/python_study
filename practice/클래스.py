class Friend:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
        print("{0} 프로필이 생성됨".format(self.name))
        print("이름 {0}, 나이 {1}".format(self.name, self.age))

friends1 = Friend("모니카",30,"cooking")
friends2 = Friend("모니카",30,"cooking")
hi = Friend("챈들러",30,"napping")
