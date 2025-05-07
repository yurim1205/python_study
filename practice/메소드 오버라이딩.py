class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("지상 유닛 이동")
        print("{0}: {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp,speed, damage):
        Unit.__init__(self, name, hp,speed)
        self.damage = damage

    def attack(self, location):
        print("{0}: {1} 방향으로 공격. [공격력 {2}]" \
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0}: 유닛 파괴됨".format(self.name))

class Flyable:
    def __init__(self, fyling_speed):
        self.fyling_speed=fyling_speed

    def fly(self, name, location):
        print("{0}:{1} 방향으로 날아갑니다. [속도 {2}]".\
              format(name, location, self.fyling_speed))
        
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, fyling_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, fyling_speed)

    # move()를 새롭게 정의했기 때문에 메소드 오버라이딩
    # 그래서 FlyableAttackUnit는 move()를 호출하면 아래 함수가 호출됨
    def move(self, location):
        print("공중 유닛 이동")
        self.fly(self.name, location)

vulture = AttackUnit("벌쳐",80,10,20)

battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")