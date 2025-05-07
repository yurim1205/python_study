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

class BuildingUnit(Unit):
    def __init__(self, name, hp, speed):
        pass

supply_depot = BuildingUnit("서플라이 디폿",500,"7시")

def game_start():
    print("새로운 게임을 시작")

def game_over():
    pass

game_start()
game_over()