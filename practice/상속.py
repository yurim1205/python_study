class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
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

firebat1 = AttackUnit("파이어뱃",50,10)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)