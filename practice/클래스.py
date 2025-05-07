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

apt1 = Friend("조이",32,"love")
print("이름: {0}, 나이: {1}".format(apt1.name, apt1.age))

apt2 = Friend("피비",31,"running")

# 외부에서 추가로 객체에 새로운 변수 생성 가능함

# 클래스 외부에서 원하는 변수에 대해서 확장 가능하고,
# 그 확장된 변수는 확장을 한 객체에서만 사용 가능함
apt2.running=True

if apt2.running ==True:
    print("{0}는 현재 조깅 중입니다.".format(apt2.name))