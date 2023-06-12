class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력: {0}, 공격력: {1}".format(self.hp, self.damage))

    def attack(self, att):
        print(att)


def attack1(att):
    print(att)


marine1 = Unit("마린", 40, 5)
marine1.attack(10)