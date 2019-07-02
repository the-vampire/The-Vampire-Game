'''
创建一个人类，其他类都继承人类
'''


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.hp = 100
        self.speed = 30


    # 人类在喝了吸血鬼的血之后可以变成吸血鬼
    # def eat(self, food):
    #     print("补充能量")
    #     if food == 'vampire_blood':
    #         self.hp = 100


    # 攻击属性
    def fight(self, weapon):
        if weapon == "wood":
            self.hp -= 40
        elif weapon == "plum":
            self.hp -= 100
        elif weapon == "vervain":
            self.hp -= 100
        elif weapon == "break_heat":
            self.hp -= 100


    # def death(self):
    #     if self.hp <= 0:
    #         print("Game Over!")


